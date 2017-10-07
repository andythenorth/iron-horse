import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import math
import inspect # only used for deprecated attempt at partial compiles, remove (and vehicle_module_path var)
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import global_constants # expose all constants for easy passing to templates
import utils

from graphics_processor.visible_cargo import VisibleCargo, VisibleCargoCustom, VisibleCargoLiveryOnly
import graphics_processor.utils as graphics_utils

from rosters import registered_rosters
from vehicles import numeric_id_defender

class Consist(object):
    """
       'Vehicles' (appearing in buy menu) are composed as articulated consists.
       Each consist comprises one or more 'units' (visible).
   """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.vehicle_module_path = inspect.stack()[2][1]
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        self.title = kwargs.get('title', None)
        self.base_numeric_id = kwargs.get('base_numeric_id', None)
        self._intro_date = kwargs.get('intro_date', None) # private var as wagons have their own method for automated intro dates
        self.vehicle_life = kwargs.get('vehicle_life', 40)
        self.power = kwargs.get('power', 0)
        self.track_type = kwargs.get('track_type', 'RAIL')
        self.tractive_effort_coefficient = kwargs.get('tractive_effort_coefficient', 0.3) # 0.3 is recommended default value
        self._speed = kwargs.get('speed', None) # private var, can be used to over-rides default (per generation, per class) speed
        self.gen = kwargs.get('gen', None) # optional
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_railtype = kwargs.get('power_by_railtype', None)
        self.visual_effect_override_by_railtype = kwargs.get('visual_effect_override_by_railtype', None)
        self.dual_headed = 1 if kwargs.get('dual_headed', False) else 0
        # arbitrary adjustments of points that can be applied to adjust buy cost and running cost, over-ride in consist as needed
        # values can be -ve or +ve to dibble specific vehicles (but total calculated points cannot exceed 255)
        self.type_base_buy_cost_points = kwargs.get('type_base_buy_cost_points', 15)
        self.type_base_running_cost_points = kwargs.get('type_base_running_cost_points', 15)
        # create a structure to hold model variants
        self.model_variants = []
        # mostly vehicles vary graphics by build year, but for date-sensitive cargo, we want to vary by current year
        self.date_variant_var = kwargs.get('date_variant_var', 'build_year')
        # create structure to hold the units
        self.units = []
        # cargo /livery graphics options
        self.visible_cargo = VisibleCargo()
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        self.roster_id = None
         # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get('suppress_animated_pixel_warnings', False)

    def add_model_variant(self, start_date, end_date, spritesheet_suffix, graphics_processor=None, visual_effect_offset=None):
        self.model_variants.append(ModelVariant(start_date, end_date, spritesheet_suffix, graphics_processor, visual_effect_offset))

    def add_unit(self, type, repeat=1, **kwargs):
        vehicle = type(consist=self, **kwargs)
        count = len(self.unique_units)
        if count == 0:
            vehicle.id = self.id # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
        else:
            vehicle.id = self.id + '_' + str(count)
        vehicle.numeric_id = self.get_and_verify_numeric_id(count)
        vehicle.vehicle_length
        self.units.append(vehicle)

    @property
    def unique_units(self):
        # units may be repeated in the consist, sometimes we need an ordered list of unique units
        # set() doesn't preserve list order, which matters, so do it the hard way
        unique_units = []
        for unit in self.units:
            if unit not in unique_units:
                unique_units.append(unit)
        return unique_units

    def get_and_verify_numeric_id(self, offset):
        numeric_id = self.base_numeric_id + offset
        # guard against the ID being too large to build in an articulated consist
        if numeric_id > 16383:
            utils.echo_message("Error: numeric_id " + str(numeric_id) + " for " + self.id + " can't be used (16383 is max ID for articulated vehicles)")
        # non-blocking guard on duplicate IDs
        for id in numeric_id_defender:
            if id == numeric_id:
                utils.echo_message("Error: consist " + self.id + " unit id collides (" + str(numeric_id) + ") with units in another consist")
        numeric_id_defender.append(numeric_id)
        return numeric_id

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get('track_type', None) == 'NG':
            id_base = id_base + '_ng'
        result = '_'.join((id_base, kwargs['roster'], 'gen', str(kwargs['gen']) + str(kwargs['subtype'])))
        return result

    def get_reduced_set_of_variant_dates(self):
        # find all the unique dates that will need a switch constructing
        years = set()
        for variant in self.model_variants:
            years.update((variant.start_date, variant.end_date))
        years = sorted(years)
        # quick integrity check
        if years[0] != 0:
            utils.echo_message(self.id + " doesn't have at least one model variant with intro date 0 (required for nml switches to work)")
        return years

    def get_num_spritesets(self):
        # historical reasons, this used to be more complex, and is now very simple; possibly now an abstraction too far?
        return len(self.model_variants)

    def get_variants_available_for_specific_year(self, year):
        # put the data in a format that's easy to render as switches
        result = []
        for variant in self.model_variants:
            if variant.start_date <= year < variant.end_date:
                result.append(variant)
        return result # could call set() here, but I didn't bother, shouldn't be needed if model variants set up correctly

    def get_nml_random_switch_fragments_for_model_variants(self, vehicle, switch_name_substr):
        # return fragments of nml for use in switches
        result = []
        years = self.get_reduced_set_of_variant_dates()
        for index, year in enumerate(years):
            if index < len(years) - 1:
                from_date = year
                until_date = years[index + 1] - 1
                result.append(str(from_date) + '..' + str(until_date) + ':' + vehicle.id + switch_name_substr + str(from_date))
        return result

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        name = self.title.split('[')[0]
        # enforce a space if name is not empty
        if len(name) is not 0:
            name = name + ' '
        return name

    def get_str_name_suffix(self):
        # used in vehicle name string only, relies on name property value being in format "Foo [Bar]" for Name [Type Suffix]
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return 'STR_NAME_SUFFIX_' + type_suffix

    def get_name(self):
        return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def unit_requires_variable_power(self, vehicle):
        if self.power_by_railtype is not None and vehicle.is_lead_unit_of_consist:
            return True
        else:
            return False

    def get_spriterows_for_consist_or_subpart(self, units):
        # pass either list of all units in consist, or a slice of the consist starting from front (arbitrary slices not useful)
        # spriterow count is number of output sprite rows from graphics processor, to be used by nml sprite templating
        result = []
        for unit in units:
            unit_rows = []
            if unit.always_use_same_spriterow:
                unit_rows.append(('always_use_same_spriterow', 1))
            else:
                # assumes visible_cargo is used to handle any other rows, no other cases at time of writing, could be changed eh?
                unit_rows.extend(self.visible_cargo.get_output_row_counts_by_type())
            result.append(unit_rows)
        return result

    @property
    def graphics_processors(self):
        # wrapper to get the graphics processors
        template = self.id + '_template.png'
        return graphics_utils.get_composited_cargo_processors(template = template)

    @property
    def buy_cost(self):
        # stub only
        # vehicle classes should over-ride this to provide class-appropriate cost calculation
        return 0

    @property
    def running_cost(self):
        # stub only
        # vehicle classes should over-ride this to provide class-appropriate running cost calculation
        return 0

    @property
    def intro_date(self):
        # automatic intro_date, but can over-ride by passing in kwargs for consist
        if self._intro_date:
            return self._intro_date
        else:
            roster_obj = self.get_roster(self.roster_id)
            return roster_obj.intro_dates[self.gen - 1]

    @property
    def model_life(self):
        # hard-coded for now, based on 30 year generations
        # !! needs to be over-rideable for engines that span generations
        return 40

    @property
    def speed(self):
        # automatic speed, but can over-ride by passing in kwargs for consist
        if self._speed:
            return self._speed
        else:
            # !! eh this relies currently on railtypes being 'RAIL' or 'NG'
            # it only works because electric engines currently have their speed set explicitly :P
            # could be fixed by checking a list of railtypes
            roster_obj = self.get_roster(self.roster_id)
            return roster_obj.speeds[self.track_type][self.speed_class][self.gen - 1]

    @property
    def weight(self):
        return sum([getattr(unit, 'weight', 0) for unit in self.units])

    def get_roster(self, roster_id):
        for roster in registered_rosters:
            if roster_id == roster.id:
                return roster

    def get_expression_for_rosters(self):
        # the working definition is one and only one roster per vehicle
        roster = self.get_roster(self.roster_id)
        return 'param[1]==' + str(roster.numeric_id - 1)

    @property
    def buy_menu_width (self):
        # max sensible width in buy menu is 64px
        consist_length = 4 * sum([unit.vehicle_length for unit in self.units])
        if consist_length < 64:
            return consist_length
        else:
            return 64

    def render_articulated_switch(self):
        template = templates["articulated_parts.pynml"]
        nml_result = template(consist=self, global_constants=global_constants)
        return nml_result

    def render(self):
        # templating
        nml_result = ''
        if len(self.units) > 1:
            nml_result = nml_result + self.render_articulated_switch()
        for unit in self.unique_units:
            nml_result = nml_result + unit.render()
        return nml_result


class Train(object):
    """Base class for all types of trains"""
    def __init__(self, **kwargs):
        self.consist = kwargs.get('consist')

        # setup properties for this train
        self.numeric_id = kwargs.get('numeric_id', None)
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self.vehicle_length = kwargs.get('vehicle_length', None)
        self.speed = kwargs.get('speed', 0)
        self._weight = kwargs.get('weight', None)
        self._capacity_pax = kwargs.get('capacity_pax', 0)
        self._capacity_mail = kwargs.get('capacity_mail', 0)
        self._capacity_freight = kwargs.get('capacity_freight', 0)
        self.loading_speed_multiplier = kwargs.get('loading_speed_multiplier', 1)
        # spriterow_num, first row = 0
        self.spriterow_num = kwargs.get('spriterow_num', 0)
        # set defaults for props otherwise set by subclass as needed (not set by kwargs as specific models do not over-ride them)
        self.default_cargo = 'PASS' # over-ride in subclass as needed
        self.class_refit_groups = []
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.engine_class = 'ENGINE_CLASS_STEAM' # nml constant (STEAM is sane default)
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # nml constant
        self.default_visual_effect_offset = 0 # visual effect handling is fiddly, check ModelVariant also
        # optional - some consists have sequences like A1-B-A2, where A1 and A2 look the same but have different IDs for implementation reasons
        # avoid duplicating sprites on the spritesheet by forcing A2 to use A1's spriterow_num, fiddly eh?
        # ugly, but eh.  Zero-indexed, based on position in units[]
        # watch out for repeated vehicles in the consist when calculating the value for this)
        # !! I don't really like this solution, might be better to have the graphics processor duplicate this?, with a simple map of [source:duplicate_to]
        self.unit_num_providing_spriterow_num = kwargs.get('unit_num_providing_spriterow_num', None)
        # optional - force always using same spriterow
        # for cases where the template handles cargo, but some units in the consist might not show cargo, e.g. tractor units etc
        # can also be used to suppress compile failures during testing when spritesheet is unfinished (missing rows etc)
        self.always_use_same_spriterow = kwargs.get('always_use_same_spriterow', False)
        # only set if the graphics processor requires it to generate cargo sprites
        # defines the size of cargo sprite to use
        # if the vehicle cargo area is not an OTTD unit length, use the next size up and the masking will sort it out
        # some longer vehicles may place multiple shorter cargo sprites, e.g. 7/8 vehicle, 2 * 4/8 cargo sprites (with some overlapping)
        self.cargo_length = kwargs.get('cargo_length', None)

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [int(math.ceil(capacity * multiplier)) for multiplier in global_constants.capacity_multipliers]

    @property
    def capacities_pax(self):
        return self.get_capacity_variations(self._capacity_pax)

    @property
    def capacities_mail(self):
        return self.get_capacity_variations(self._capacity_mail)

    @property
    def capacities_freight(self):
        return self.get_capacity_variations(self._capacity_freight)

    @property
    def has_cargo_capacity(self):
        if self._capacity_pax is not 0 or self._capacity_mail is not 0 or self._capacity_freight is not 0:
            return True
        else:
            return False

    @property
    def weight(self):
        # weight can be set explicitly or by methods on subclasses
        return self._weight

    @property
    def default_cargo_capacity(self):
        if self.has_cargo_capacity:
            if self.default_cargo == 'PASS':
                return self.capacities_pax[1]
            elif self.default_cargo == 'MAIL':
                return self.capacities_mail[1]
            else:
                return self.capacities_freight[1]
        else:
            return 0

    @property
    def availability(self):
        # only show vehicle in buy menu if it is first vehicle in consist
        if self.is_lead_unit_of_consist:
            return "ALL_CLIMATES"
        else:
            return "NO_CLIMATE"

    @property
    def is_lead_unit_of_consist(self):
        # first unit in the complete multi-unit consist
        if self.numeric_id == self.consist.base_numeric_id:
            return True
        else:
            return False

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC', 'TRAIN_FLAG_FLIP']
        if self.autorefit == True:
            special_flags.append('TRAIN_FLAG_AUTOREFIT')
        return ','.join(special_flags)

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [cargo_classes.append(cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes)) # use set() here to dedupe

    def get_loading_speed(self, cargo_type, capacity_param):
        # ottd vehicles load at different rates depending on type,
        # normalise default loading time for this set to 240 ticks, regardless of capacity
        # openttd loading rates vary by transport type, look them up in wiki to find value to use here to normalise loading time to 240 ticks
        transport_type_rate = 6 # this is (240 / loading frequency in ticks for transport type) from wiki
        capacities = getattr(self, 'capacities_' + cargo_type)
        return int(self.loading_speed_multiplier * math.ceil(capacities[capacity_param] / transport_type_rate))

    @property
    def running_cost_base(self):
        return {'ENGINE_CLASS_STEAM': 'RUNNING_COST_STEAM',
                           'ENGINE_CLASS_DIESEL': 'RUNNING_COST_DIESEL',
                           'ENGINE_CLASS_ELECTRIC': 'RUNNING_COST_ELECTRIC'}[self.engine_class]

    @property
    def offsets(self):
        # offsets can also be over-ridden on a per-model basis by providing this property in the model class
        return global_constants.default_spritesheet_offsets[str(self.vehicle_length)]

    @property
    def vehicle_nml_template(self):
        if not self.always_use_same_spriterow:
            if self.consist.visible_cargo.nml_template:
                return self.consist.visible_cargo.nml_template
        # default case
        return 'vehicle_default.pynml'

    @property
    def location_of_random_bits_for_model_variant(self):
        return 'FORWARD_SELF(' + str(self.numeric_id - self.consist.base_numeric_id) + ')'

    def get_visual_effect_offset(self, variant):
        # no sign here of bonkers complexity just to flip smoke on flipped engines
        if variant.visual_effect_offset is None:
            if self.default_visual_effect_offset == 'FRONT':
                return int(math.floor(-0.5 * self.vehicle_length))
            else:
                return self.default_visual_effect_offset
        else:
            if variant.visual_effect_offset == 'AUTOFLIP':
                print("get_visual_effect_offset() 'AUTOFLIP' detection is silly, and needs refactored")
                return int(math.floor(0.5 * (self.vehicle_length - self.vehicle_length))) # !! this is legacy and will now result in 0 always
            else:
                return variant.visual_effect_offset

    def get_nml_expression_for_cargo_variant_random_switch(self, variation_num, cargo_id=None):
        # having a method to calculate the nml for this is overkill
        # legacy of multi-part vehicles, where the trigger needed to be run on an adjacent vehicle
        # this could be unpicked and moved directly into the templates
        switch_id = self.id + "_switch_graphics_" + str(variation_num) + ('_' + str(cargo_id) if cargo_id is not None else '')
        return "SELF," + switch_id + ", bitmask(TRIGGER_VEHICLE_NEW_LOAD)"

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        # offset is number of units
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # offset is number of units
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ','.join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ','.join(self.label_refits_disallowed)

    def get_cargo_suffix(self):
        return 'string(' + self.cargo_units_refit_menu + ')'

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " + i + " which is not defined in the cargo table")

    def render_cargo_capacity(self):
        template = templates["capacity_switches.pynml"]
        return template(vehicle=self)

    def render(self):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        # templating
        template_name = self.vehicle_nml_template
        template = templates[template_name]
        nml_result = template(vehicle=self, consist=self.consist, global_constants=global_constants)
        return nml_result


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per train
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, start_date, end_date, spritesheet_suffix, graphics_processor, visual_effect_offset):
        self.start_date = start_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames
        self.graphics_processor = graphics_processor
        self.visual_effect_offset = visual_effect_offset # used to move effects around when flipping vehicle - might be a better way?

    def get_spritesheet_name(self, consist):
        return consist.id + '_' + str(self.spritesheet_suffix) + '.png'


class EngineConsist(Consist):
    """
    Intermediate class for engine consists to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to engine consists.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_engine_cost_points(self):
        # Up to 80 points for power. 1 point per 100hp
        # Power is therefore capped at 8000hp by design, this isn't a hard limit, but raise a warning
        if self.power > 8000:
            utils.echo_message("Consist " + self.id + " has power > 8000hp, which is too much")
        power_cost_points = self.power / 100

        # Up to 20 points for speed up to 80mph. 1 point per 2mph
        speed_cost_points = min(self.speed, 80) / 2

        # Up to 80 points for speed above 80mph up to 200mph. 1 point per 1.5mph
        if self.speed > 200:
            utils.echo_message("Consist " + self.id + " has speed > 200, which is too much")
        high_speed_cost_points = max((self.speed - 80), 0) / 1.5

        # Up to 40 points for intro date after 1870. 1 point per 4 years.
        # Intro dates capped at 2030, this isn't a hard limit, but raise a warning
        if self.intro_date > 2030:
            utils.echo_message("Consist " + self.id + " has intro_date > 2030, which is too much")
        date_cost_points = max((self.intro_date - 1870), 0) / 4

        return power_cost_points + speed_cost_points + high_speed_cost_points + date_cost_points

    @property
    def buy_cost(self):
        # type_base_buy_cost_points is an arbitrary adjustment that can be applied on a type-by-type basis,
        return self.get_engine_cost_points() + self.type_base_buy_cost_points

    @property
    def running_cost(self):
        # type_base_running_cost_points is an arbitrary adjustment that can be applied on a type-by-type basis,
        return self.get_engine_cost_points() + self.type_base_running_cost_points


class WagonConsist(Consist):
    """
    Intermediate class for wagon consists to subclass from, provides sparse properties, most are declared in subclasses.
    """
    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        self.date_variant_var = kwargs.get('date_variant_var', None)

        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get('roster', None)
        roster_obj = self.get_roster(self.roster_id)  # roster_obj for local reference only, don't persist this

        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs['id'] = id
        super().__init__(**kwargs)

        roster_obj.register_wagon_consist(self)

        self.speed_class = 'freight' # over-ride this for, e.g. 'express' consists
        self.subtype = kwargs['subtype']
        self.weight_factor = 0.5 # over-ride in sub-class as needed
        self.loading_speed_multiplier = kwargs.get('loading_speed_multiplier', 1)
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)


    @property
    def buy_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        capacity_factors = []
        for unit in self.units:
            if unit.default_cargo == 'PASS':
                # pax coaches have seats and stuff, are expensive to build
                capacity_factors.append(3 * unit.default_cargo_capacity)
            elif unit.default_cargo == 'MAIL':
                # mail cars have pax-grade eqpt, but no seats etc, so moderately expensive
                capacity_factors.append(2 * unit.default_cargo_capacity)
            else:
                capacity_factors.append(unit.default_cargo_capacity)
        cost = cost + sum(capacity_factors)
        return 0.5 * cost # dibble all the things

    @property
    def running_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        if self.units[0].default_cargo == 'PASS':
            return cost / 4
        elif self.units[0].default_cargo == 'MAIL':
            return cost / 7
        else:
            return cost / 8

    @property
    def model_life(self):
        # automatically span wagon model life across gap to next generation
        roster_obj = self.get_roster(self.roster_id)
        roster_gens_for_class = sorted(set([wagon.gen for wagon in roster_obj.wagon_consists[self.base_id] if wagon.subtype == self.subtype]))
        this_index = roster_gens_for_class.index(self.gen)
        if this_index == len(roster_gens_for_class) - 1:
            return 'VEHICLE_NEVER_EXPIRES'
        else:
            next_gen = roster_gens_for_class[roster_gens_for_class.index(self.gen) + 1]
            gen_span = next_gen - self.gen
            return 10 + (30 * gen_span)

class BoxConsist(WagonConsist):
    """
    Box car, van - express, piece goods cargos, other selected cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'box_car'
        super().__init__(**kwargs)
        self.title = '[Box Car]'
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'GOOD'


class CabooseConsist(WagonConsist):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """
    def __init__(self, **kwargs):
        self.base_id = 'caboose_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        # no graphics processing - don't random colour cabeese, I tried it, looks daft
        self.class_refit_groups = [] # refit nothing, don't mess with this, it breaks auto-replace
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargo = 'GOOD' # unwanted side-effect of this is that caboose replaceable by anything refitting goods


class CoveredHopperConsist(WagonConsist):
    """
    Bulk powder / pellet cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'covered_hopper_car'
        super().__init__(**kwargs)
        self.title = '[Covered Hopper Car]'
        self.class_refit_groups = ['covered_hopper_freight']
        self.label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ', 'FOOD', 'SUGR', 'FMSP', 'RFPR', 'CLAY', 'BDMT', 'BEAN', 'NITR', 'RUBR', 'SAND', 'POTA', 'QLME', 'SASH', 'CMNT', 'KAOL', 'FERT']
        self.label_refits_disallowed = []
        self.default_cargo = 'GRAI'
        self.loading_speed_multiplier = 2


class DumpConsist(WagonConsist):
    """
    Limited set of bulk (mineral) cargos, same set as hopper cars.
    """
    def __init__(self, **kwargs):
        self.base_id = 'dump_car'
        super().__init__(**kwargs)
        self.title = '[Dump Car]'
        self.class_refit_groups = ['hopper_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight']
        self.default_cargo = 'IORE'
        self.loading_speed_multiplier = 2
        # Cargo Graphics
        self.visible_cargo.bulk = True


class EdiblesTankConsist(WagonConsist):
    """
    Wine, milk, water etc.
    """
    def __init__(self, **kwargs):
        self.base_id = 'edibles_tank_car'
        super().__init__(**kwargs)
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.title = '[Edibles Tank Car]'
        self.speed_class = 'express'
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = ['FOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_edible_liquids']
        self.default_cargo = 'WATR'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2


class FlatConsist(WagonConsist):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """
    def __init__(self, **kwargs):
        self.base_id = 'flat_car'
        super().__init__(**kwargs)
        self.title = '[Flat Car]'
        self.class_refit_groups = ['flatcar_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight']
        self.default_cargo = 'STEL'
        # Cargo graphics
        self.visible_cargo.piece = True


class FruitVegConsist(WagonConsist):
    """
    Fruit and vegetables, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'fruit_veg_car'
        super().__init__(**kwargs)
        self.title = '[Fruit Car]'
        self.class_refit_groups = []
        self.label_refits_allowed = ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS']
        self.label_refits_disallowed = []
        self.default_cargo = 'FRUT'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD


class HopperConsist(WagonConsist):
    """
    Limited set of bulk (mineral) cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'hopper_car'
        super().__init__(**kwargs)
        self.title = '[Hopper Car]'
        self.class_refit_groups = ['hopper_freight']
        self.label_refits_allowed = [] # none needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight']
        self.default_cargo = 'COAL'
        self.loading_speed_multiplier = 2
        # Cargo graphics
        self.visible_cargo.bulk = True


class IntermodalConsist(WagonConsist):
    """
    Specialist intermodal (containers), limited range of cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'intermodal_car'
        super().__init__(**kwargs)
        self.title = '[Intermodal Car]'
        self.speed_class = 'express'
        self.class_refit_groups = ['express_freight', 'packaged_freight']
        #label_refits_allowed = list(cargo_graphics_mappings.keys())
        # maintain other sets (e.g. Squid etc) when changing container refits
        self.label_refits_allowed = ['FRUT','WATR']
        self.label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD']
        self.default_cargo = 'GOOD'
        self.loading_speed_multiplier = 2


class LivestockConsist(WagonConsist):
    """
    Livestock, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'livestock_car'
        super().__init__(**kwargs)
        self.title = '[Livestock Car]'
        self.class_refit_groups = []
        self.label_refits_allowed = ['LVST']
        self.label_refits_disallowed = []
        self.default_cargo = 'LVST'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD


class StakeConsist(WagonConsist):
    """
    Specialist log (wood) transporter
    """
    def __init__(self, **kwargs):
        self.base_id = 'stake_car'
        super().__init__(**kwargs)
        self.title = '[Stake Car]'
        self.class_refit_groups = ['flatcar_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight']
        self.default_cargo = 'WOOD'
        self.loading_speed_multiplier = 2
        # Cargo graphics
        self.visible_cargo = VisibleCargoCustom({'WOOD': [0]},
                                                'vehicle_with_visible_cargo.pynml',
                                                generic_rows = [0])


class MailConsist(WagonConsist):
    """
    Common base class for mail cars.
    Mail cars also handle express freight, valuables.
    """
    def __init__(self, **kwargs):
        self.base_id = 'mail_car'
        super().__init__(**kwargs)
        self.title = '[Mail Car]'
        self.speed_class = 'express'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'MAIL'


class MetalConsist(WagonConsist):
    """
    Specialist heavy haul metal transport e.g. torpedo car, ladle, etc
    High capacity, not very fast, refits to small subset of finished metal cargos (and slag, which bends the rules a bit).
    """
    def __init__(self, **kwargs):
        self.base_id = 'metal_car'
        super().__init__(**kwargs)
        self.title = '[Metal Car]'
        self.class_refit_groups = []
        self.label_refits_allowed = ['STEL', 'COPR', 'IRON', 'SLAG', 'METL']
        self.label_refits_disallowed = []
        self.default_cargo = 'STEL'
        self.loading_speed_multiplier = 2


class OpenConsist(WagonConsist):
    """
    General cargo - refits everything except mail, pax.
    """
    def __init__(self, **kwargs):
        self.base_id = 'open_car'
        super().__init__(**kwargs)
        self.title = '[Open Car]'
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargo = 'GOOD'
        # Cargo Graphics
        self.visible_cargo.bulk = True
        self.visible_cargo.piece = True


class PassengerConsistBase(WagonConsist):
    """
    Common base class for passenger cars.
    """
    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'PASS'


class PassengerConsist(PassengerConsistBase):
    """
    Standard pax car.
    """
    def __init__(self, **kwargs):
        self.base_id = 'passenger_car'
        super().__init__(**kwargs)
        self.title = '[Passenger Car]'


class PassengerLuxuryConsist(PassengerConsistBase):
    """
    Improved decay rate and lower capacity per unit length compared to standard pax car.
    Possibly random sprites for restaurant car, observation car etc.
    """
    def __init__(self, **kwargs):
        self.base_id = 'luxury_passenger_car'
        super().__init__(**kwargs)
        self.title = '[Luxury Passenger Car]'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD


class ReeferConsist(WagonConsist):
    """
    Refrigerated cargos, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'reefer_car'
        super().__init__(**kwargs)
        self.title = '[Reefer Car]'
        self.speed_class = 'express'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargo = 'FOOD'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD


class SuppliesConsist(WagonConsist):
    """
    Specialist vehicle for supplies and building materials
    """
    def __init__(self, **kwargs):
        self.base_id = 'supplies_car'
        super().__init__(**kwargs)
        self.title = '[Supplies Car]'
        self.class_refit_groups = []
        self.label_refits_allowed = ['ENSP', 'FMSP', 'VEHI', 'BDMT']
        self.label_refits_disallowed = []
        self.default_cargo = 'ENSP'
        self.date_variant_var = 'current_year'
        # Cargo graphics
        self.visible_cargo = VisibleCargoCustom({'ENSP': [0], 'FMSP': [0], 'VEHI': [0], 'BDMT': [0]},
                                                'vehicle_with_visible_cargo.pynml',
                                                generic_rows = [0])


class TankConsist(WagonConsist):
    """
    All non-edible liquid cargos
    """
    def __init__(self, **kwargs):
        self.base_id = 'tank_car'
        super().__init__(**kwargs)
        self.title = '[Tank Car]'
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they also change livery at stations if refitted between certain cargo types <shrug>
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = []
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['edible_liquids']
        self.default_cargo = 'OIL_'
        self.loading_speed_multiplier = 3
        self.visible_cargo = VisibleCargoLiveryOnly()
        self.visible_cargo.tanker = True


class VehicleTransporterConsist(WagonConsist):
    """
    Transports vehicles cargo
    """
    def __init__(self, **kwargs):
        self.base_id = 'vehicle_transporter_car'
        super().__init__(**kwargs)
        self.title = '[Vehicle Transporter Car]'
        self.class_refit_groups = []
        self.label_refits_allowed = ['VEHI']
        self.label_refits_disallowed = []
        self.default_cargo = 'VEHI'
        self.date_variant_var = 'current_year'


class Wagon(Train):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by Train with useful defaults.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist = kwargs['consist']
        self.class_refit_groups = self.consist.class_refit_groups
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.default_cargo = self.consist.default_cargo
        if hasattr(self.consist, 'loading_speed_multiplier'):
            self.loading_speed_multiplier = self.consist.loading_speed_multiplier
        if hasattr(self.consist, 'cargo_age_period'):
            self.cargo_age_period = self.consist.cargo_age_period

    @property
    def weight(self):
        # set weight based on capacity  * a multiplier from consist (default 0.5 or so)
         return self.consist.weight_factor * self.default_cargo_capacity


class SteamLoco(Train):
    """
    Steam Locomotive.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.visual_effect = 'VISUAL_EFFECT_STEAM'
        self.default_visual_effect_offset = 'FRONT'


class SteamLocoTender(Train):
    """
    Steam Locomotive Tender.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DieselLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class DieselRailcar(Train):
    """
    Diesel Railcar (Single Unit).
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['pax', 'mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self._capacity_mail = int(0.75 * self._capacity_pax)
        self._capacity_freight = int(0.75 * self._capacity_pax)
        self.default_cargo = 'PASS'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class ElectricLoco(Train):
    """
    Electric Locomotive.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(kwargs['consist'], 'track_type'):
            # all NG vehicles should set 'NG' only, this class then over-rides that to electrified NG as needed
            # why? this might be daft?
            if kwargs['consist'].track_type == "NG":
                kwargs['consist'].track_type = "ELNG"
            else:
                kwargs['consist'].track_type = "ELRL"
        else:
            kwargs['consist'].track_type = "ELRL"
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'


class ElectroDieselLoco(Train):
    """
    Bi-mode Locomotive - operates on electrical power or diesel.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'
        self.consist.visual_effect_override_by_railtype = {'ELRL': 'VISUAL_EFFECT_ELECTRIC'}


class CargoSprinter(Train):
    """
    Freight Multiple Unit.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # refits should match those of the intermodal cars
        self.class_refit_groups = ['express_freight', 'packaged_freight']
        self.label_refits_allowed = ['FRUT','WATR']
        self.label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD']
        self.loading_speed_multiplier = 2
        self.default_cargo = 'GOOD'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # intended - positioning smoke correctly for this vehicle type is too fiddly
        """
        # graphics processor stuff also used at __init__ time
        self.consist.recolour_maps = graphics_constants.container_recolour_maps
        self.consist.num_random_cargo_variants = len(self.consist.recolour_maps)
        self.consist.cargos_with_tanktainer_graphics = ['BEER', 'MILK', 'WATR'] # !! unfinished currently??
         # ugh, the graphics consists are applied to the consist in all other cases,
         # but CargoSprinter doesn't have a dedicated consist subclass, so processors are on the unit, with this nasty passthrough
        self.consist.graphics_processors = self.graphics_processors

    @property
    def graphics_processors(self):
        graphics_options = {'template': 'cargo_sprinter_template_0.png',
                           'recolour_maps': self.consist.recolour_maps,
                           'copy_block_top_offset': 0,
                           'num_rows_per_unit': 3,
                           'num_unit_types': 3}
        return GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options)
    """

class PassengerCar(Wagon):
    """
    Passenger Carriage.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._capacity_pax = kwargs.get('capacity', None)


class MailCar(Wagon):
    """
    Mail Carriage.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._capacity_mail = kwargs.get('capacity', None)
        self._capacity_freight = int(0.5 * self._capacity_mail)


class FreightCar(Wagon):
    """
    Freight wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs.get('capacity', None) is not None:
             print(self.consist.id, kwargs.get('capacity', None))
        roster_obj = self.consist.get_roster(self.consist.roster_id)
        self._capacity_freight = kwargs['vehicle_length'] * roster_obj.freight_car_capacity_per_unit_length[self.consist.track_type][self.consist.gen - 1]


class BoxCar(FreightCar):
    """
    Box Car. This sub-class only exists to handle the mail capacity, in other respects it's just a standard wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._capacity_mail = int(2.0 * self._capacity_freight)


class CabooseCar(FreightCar):
    """
    Caboose Car. This sub-class only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def weight(self):
        # special handling of weight
        return 5 * self.vehicle_length


class MetroPaxUnit(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargo = "PASS"
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'


class MetroCargoUnit(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self._capacity_mail = kwargs.get('capacity', None)
        self._capacity_freight = int(0.5 * self._capacity_mail)
        self.default_cargo = "MAIL"
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'

