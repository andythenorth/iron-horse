import global_constants # expose all constants for easy passing to templates
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import graphics_processor
import graphics_processor.pipelines

from rosters import registered_rosters
from vehicles import numeric_id_defender

import inspect

class Consist(object):
    """
       'Vehicles' (appearing in buy menu) are composed as articulated consists.
       Each consist comprises one or more 'units' (visible).
       Each unit assembled from 3 'slices' (invisible-visible-invisible), which are newgrf vehicles with uids.
   """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.vehicle_module_path = inspect.stack()[2][1]
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        self.title = kwargs.get('title', None)
        self.base_numeric_id = kwargs.get('base_numeric_id', None)
        self.intro_date = kwargs.get('intro_date', None)
        self.vehicle_life = kwargs.get('vehicle_life', None)
        self.power = kwargs.get('power', 0)
        self.track_type = kwargs.get('track_type', 'RAIL')
        self.tractive_effort_coefficient = kwargs.get('tractive_effort_coefficient', 0.3) # 0.3 is recommended default value
        self.speed = kwargs.get('speed', None)
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_railtype = kwargs.get('power_by_railtype', None)
        self.visual_effect_override_by_railtype = kwargs.get('visual_effect_override_by_railtype', None)
        # arbitrary adjustments of points that can be applied to adjust buy cost and running cost, over-ride in consist as needed
        # values can be -ve or +ve to dibble specific vehicles (but total calculated points cannot exceed 255)
        self.type_base_buy_cost_points = kwargs.get('type_base_buy_cost_points', 15)
        self.type_base_running_cost_points = kwargs.get('type_base_running_cost_points', 15)
        # hangover from switching to 10/8 spritesheet and not wanting to fix existing spritesheets
        self.use_legacy_spritesheet = kwargs.get('use_legacy_spritesheet', False)
        # create a structure to hold model variants
        self.model_variants = []
        # mostly vehicles vary graphics by build year, but for date-sensitive cargo, we want to vary by current year
        self.date_variant_var = kwargs.get('date_variant_var', 'build_year')
        # create structure to hold the slices
        self.slices = []
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        self.roster_id = None
         # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get('suppress_animated_pixel_warnings', False)


    def add_model_variant(self, intro_date, end_date, spritesheet_suffix, graphics_processor=None, visual_effect_offset=None):
        variant_num = len(self.model_variants) # this will never ever ever be flakey and unreliable, right?
        self.model_variants.append(ModelVariant(intro_date, end_date, spritesheet_suffix, graphics_processor, variant_num, visual_effect_offset))

    def add_unit(self, vehicle, repeat=1):
        # vehicle ids increment by 3 because each vehicle is composed of 3 intermediate slices
        count = len(set(self.slices))
        first_slice = LeadSlice(parent_vehicle=vehicle)
        second_slice = vehicle
        third_slice = NullTrailingSlice(parent_vehicle=vehicle)
        if count == 0:
            first_slice.id = self.id # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
        else:
            first_slice.id = self.id + '_' + str(count)
        second_slice.id = self.id + '_' + str(count + 1)
        third_slice.id = self.id + '_' + str(count + 2)
        first_slice.numeric_id = self.get_and_verify_numeric_id(count)
        second_slice.numeric_id = self.get_and_verify_numeric_id(count + 1)
        third_slice.numeric_id = self.get_and_verify_numeric_id(count + 2)
        first_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][0]
        second_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][1]
        third_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][2]
        first_slice.spriterow_num = vehicle.spriterow_num

        for repeat_num in range(repeat):
            self.slices.append(first_slice)
            self.slices.append(second_slice)
            self.slices.append(third_slice)

    def get_and_verify_numeric_id(self, offset):
        numeric_id = self.base_numeric_id + offset
        # guard against the ID being too large to build in an articulated consist
        if numeric_id > 16383:
            utils.echo_message("Error: numeric_id " + str(numeric_id) + " for " + self.id + " can't be used (16383 is max ID for articulated vehicles)")
        # non-blocking guard on duplicate IDs
        for id in numeric_id_defender:
            if id == numeric_id:
                utils.echo_message("Error: consist " + self.id + " slice id collides (" + str(numeric_id) + ") with slices in another consist")
        numeric_id_defender.append(numeric_id)
        return numeric_id

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get('track_type', None) == 'NG':
            id_base = id_base + '_ng'
        result = '_'.join((id_base, kwargs['roster'], 'gen', str(kwargs['wagon_generation'])))
        return result

    def get_reduced_set_of_variant_dates(self):
        # find all the unique dates that will need a switch constructing
        years = set()
        for variant in self.model_variants:
            years.update((variant.intro_date, variant.end_date))
        years = sorted(years)
        # quick integrity check
        if years[0] != 0:
            utils.echo_message(self.id + " doesn't have at least one model variant with intro date 0 (required for nml switches to work)")
        return years

    def get_num_spritesets(self):
        return len(set([i.spritesheet_suffix for i in self.model_variants]))

    def get_variants_available_for_specific_year(self, year):
        # put the data in a format that's easy to render as switches
        result = []
        for variant in self.model_variants:
            if variant.intro_date <= year < variant.end_date:
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

    def any_slice_offers_autorefit(self):
        offers_autorefit = False
        for slice in self.slices:
            if getattr(slice, 'autorefit', False):
                offers_autorefit = True
        return offers_autorefit

    def slice_requires_variable_power(self, vehicle):
        if self.power_by_railtype is not None and vehicle.is_lead_slice_of_consist:
            return True
        else:
            return False

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
    def weight(self):
        return sum([getattr(slice, 'weight', 0) for slice in self.slices])

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
        consist_length = 4 * sum([slice.slice_length for slice in self.slices])
        if consist_length < 64:
            return consist_length
        else:
            return 64

    def render_articulated_switch(self):
        template = templates["add_articulated_parts.pynml"]
        nml_result = template(consist=self, global_constants=global_constants)
        return nml_result

    def render(self):
        # templating
        nml_result = ''
        nml_result = nml_result + self.render_articulated_switch()
        for slice in set(self.slices):
            nml_result = nml_result + slice.render()
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
        self.weight = kwargs.get('weight', None)
        # declare capacities for pax, mail and freight, as they are needed later for nml switches
        self.capacities_pax = self.get_capacity_variations(kwargs.get('capacity_pax', 0))
        self.capacities_mail = self.get_capacity_variations(kwargs.get('capacity_mail', 0)) # also used for cargos with armoured class
        self.capacities_freight = self.get_capacity_variations(kwargs.get('capacity_freight', 0))
        self.loading_speed_multiplier = kwargs.get('loading_speed_multiplier', 1)
        # spriterow_num, first row = 0
        self.spriterow_num = kwargs.get('spriterow_num', 0)
        # set defaults for props otherwise set by subclass as needed (not set by kwargs as specific models do not over-ride them)
        self.default_cargo = 'PASS' # over-ride in subclass as needed
        self.class_refit_groups = []
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = False
        self.engine_class = 'ENGINE_CLASS_STEAM' # nml constant (STEAM is sane default)
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # nml constant
        self.default_visual_effect_offset = 0 # visual effect handling is fiddly, check ModelVariant also

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # we cache the available variations on the vehicle instead of working them out every time - easier
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [int(math.ceil(capacity * multiplier)) for multiplier in global_constants.capacity_multipliers]

    @property
    def availability(self):
        # only show vehicle in buy menu if it is first vehicle in consist
        if self.is_lead_slice_of_consist:
            return "ALL_CLIMATES"
        else:
            return "NO_CLIMATE"

    @property
    def is_lead_slice_of_consist(self):
        # first slice in the complete multi-unit consist
        if self.numeric_id == self.consist.base_numeric_id:
            return True
        else:
            return False

    @property
    def is_lead_slice_of_unit(self):
        # first slice in a unit
        return isinstance(self, LeadSlice)

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC']
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
        transport_type_rate = 6 # openttd loading rates vary by transport type, look them up in wiki to find value to use here to normalise loading time to 240 ticks
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
        if self.consist.use_legacy_spritesheet:
            return global_constants.legacy_spritesheet_offsets[str(self.vehicle_length)]
        else:
            return global_constants.default_spritesheet_offsets[str(self.vehicle_length)]

    @property
    def location_of_random_bits_for_model_variant(self):
        return 'FORWARD_SELF(' + str(self.numeric_id - self.consist.base_numeric_id) + ')'

    @property
    def adjust_xoffs(self):
        # used to correct depot view x offset
        if isinstance(self, LeadSlice):
            return global_constants.xoffs_adjusts[str(self.vehicle_length)]
        else:
            return 0

    @property
    def sg_depot(self):
        if isinstance(self, LeadSlice):
            suffix = "_switch_graphics_by_year"
        else:
            suffix = "_sg_hidden"
        return self.id + suffix

    @property
    def sg_default(self):
        if isinstance(self, LeadSlice):
            suffix = "_sg_hidden"
        else:
            suffix = "_switch_graphics_by_year"
        return self.id + suffix

    def get_visual_effect_offset(self, variant):
        # no sign here of bonkers complexity just to flip smoke on flipped engines
        if variant.visual_effect_offset is None:
            if self.default_visual_effect_offset == 'FRONT':
                return int(math.floor(-0.5 * self.vehicle_length))
            else:
                return self.default_visual_effect_offset
        else:
            if variant.visual_effect_offset == 'AUTOFLIP':
                return int(math.floor(0.5 * (self.vehicle_length - self.slice_length)))
            else:
                return variant.visual_effect_offset

    def get_nml_expression_for_cargo_type_unit_refitted_to(self):
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x000000FF, 0x47]]")
        # cargo capacity is on the second slice of each 3-slice unit
        if isinstance(self, LeadSlice):
            return expression_template.substitute(offset=1)
        else:
            return expression_template.substitute(offset=0)

    def get_nml_expression_for_unit_cargo_loaded_percent(self):
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xBC]*100/var[0x61, 0, 0x0000FFFF, 0xBA]]")
        # cargo capacity is on the second slice of each 3-slice unit
        if isinstance(self, LeadSlice):
            return expression_template.substitute(offset=1)
        else:
            return expression_template.substitute(offset=0)

    def get_nml_expression_for_cargo_variant_random_switch(self, variation_num, cargo_id=None):
        switch_id = self.id + "_switch_graphics_" + str(variation_num) + ('_' + str(cargo_id) if cargo_id is not None else '')
        # get the right unit, only run triggers on the vehicle carrying cargo
        if isinstance(self, LeadSlice):
            return "BACKWARD_SELF(1)," + switch_id
        else:
            return "SELF," + switch_id + ", bitmask(TRIGGER_VEHICLE_NEW_LOAD)"

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        # offset is number of units, not number of slices
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # offset is number of units, not number of slices
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
        template_name = self.template
        template = templates[template_name]
        nml_result = template(vehicle=self, consist=self.consist, global_constants=global_constants)
        return nml_result


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per train
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, intro_date, end_date, spritesheet_suffix, graphics_processor, variant_num, visual_effect_offset):
        self.variant_num = variant_num
        self.intro_date = intro_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames
        self.graphics_processor = graphics_processor
        self.visual_effect_offset = visual_effect_offset # use digits or magic keywords, or omit

    def get_spritesheet_name(self, consist):
        return consist.id + '_' + str(self.spritesheet_suffix) + '.png'


class GraphicsProcessorFactory(object):
    # simple class which wraps graphics_processor, which uses pixa library
    # pipeline_name refers to a pipeline class which defines how the processing is done
    # may be reused across consists, so don't store consist info in the pipeline, pass it to pipeline at render time
    # this is kind of factory-pattern-ish, but don't make too much of that, it's not important
    def __init__(self, pipeline_name, options):
        self.pipeline_name = pipeline_name
        self.options = options
        self.pipeline = graphics_processor.registered_pipelines[pipeline_name]


class LeadSlice(Train):
    """
    Lead slice for a unit (invisible, minimal props).
    """
    def __init__(self, parent_vehicle):
        super(LeadSlice, self).__init__(consist=parent_vehicle.consist)
        self.parent_vehicle = parent_vehicle
        self.template = parent_vehicle.template
        self.speed = 0
        self.weight = 0
        self.vehicle_length = parent_vehicle.vehicle_length
        self.engine_class = parent_vehicle.engine_class
        self.visual_effect = parent_vehicle.visual_effect
        self.default_visual_effect_offset = parent_vehicle.default_visual_effect_offset
        self.default_cargo = parent_vehicle.default_cargo # breaks auto-replace if omitted
        # if needed, provide default capacity (set as property) so lead vehicle has same refittability as trailing slices
        # this prevents an issue with auto-refit
        if self.parent_vehicle.default_cargo_capacities[0] != 0:
            self.default_cargo_capacities = [1]
        else:
            self.default_cargo_capacities = [0]
        # actual capacity determined by cb checking cargo type, set all of these to 0
        self.capacities_pax = [0, 0, 0]
        self.capacities_freight = [0, 0, 0]
        self.capacities_mail = [0, 0, 0]
        # copy the refittability info from parent
        self.class_refit_groups = parent_vehicle.class_refit_groups
        self.label_refits_allowed = parent_vehicle.label_refits_allowed
        self.label_refits_disallowed = parent_vehicle.label_refits_disallowed
        self.cargo_age_period = parent_vehicle.cargo_age_period
        self.autorefit = parent_vehicle.autorefit
        if isinstance(parent_vehicle, CombineCar):
            self.capacities_pax = parent_vehicle.capacities_pax
            self.default_cargo_capacities = self.capacities_pax
            self.default_cargo = 'PASS'
            self.class_refit_groups = ['pax']
            # Jank for ECS tourists, parent vehicle disallows TOUR (to prevent tourists in mail compartment).
            # Then TOUR is re-allowed here, also necesary to clear the disallowed labels property.
            self.label_refits_allowed = ['TOUR']
            self.label_refits_disallowed = []


class NullTrailingSlice(object):
    """
    Trailing slice for a unit (invisible, minimal props).
    """
    def __init__(self, parent_vehicle):
        self.id = global_constants.null_trailing_slice_id
        self.numeric_id = global_constants.null_trailing_slice_numeric_id
        # provide default capacity (set as property) so leads vehicle has same refittability as trailing slices, this prevents an issue with auto-refit
        self.default_cargo_capacities = [1]
        # set a bunch of props to default / zero values
        self.capacities_pax = [0, 0, 0]
        self.capacities_freight = [0, 0, 0]
        self.capacities_mail = [0, 0, 0]
        self.default_cargo = parent_vehicle.default_cargo
        # copy the refittability info from parent
        self.class_refit_groups = parent_vehicle.class_refit_groups
        self.label_refits_allowed = parent_vehicle.label_refits_allowed
        self.label_refits_disallowed = parent_vehicle.label_refits_disallowed
        self.cargo_age_period = parent_vehicle.cargo_age_period
        self.autorefit = parent_vehicle.autorefit

    def render(self):
        template = templates['null_trailing_slice.pynml']
        return template(vehicle=self, global_constants=global_constants)


class EngineConsist(Consist):
    """
    Intermediate class for engine consists to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to engine consists.
    """
    def __init__(self, **kwargs):
        super(EngineConsist, self).__init__(**kwargs)

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
        # self.template = '' # provide in subclass
        # self.default_cargo = '' # provide in subclass
        # some of these are probably redundant, as they need to be handled in the subclass
        self.track_type = kwargs.get('track_type', 'RAIL') # !! might be redundant? needs cleaning up ??
        self.num_cargo_rows = kwargs.get('num_cargo_rows', None)
        self.generic_cargo_rows = kwargs.get('generic_cargo_rows', [0]) # optional, the rows to use if no cargo label is matched
        self.cargo_graphics_mappings = kwargs.get('cargo_graphics_mappings', None)
        self.class_refit_groups = kwargs.get('class_refit_groups', None)
        self.label_refits_allowed = kwargs.get('label_refits_allowed', None) # use None here as default, forces explicit declaration in subclass
        self.label_refits_disallowed = kwargs.get('label_refits_disallowed', None)
        self.autorefit = kwargs.get('autorefit', None)
        self.default_capacity_type = kwargs.get('default_capacity_type', None)
        self.loading_speed_multiplier = kwargs.get('loading_speed_multiplier', 1)
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self.date_variant_var = kwargs.get('date_variant_var', None)


        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get('roster', None)
        roster_obj = self.get_roster(self.roster_id)  # roster_obj for local reference only, don't persist this

        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs['id'] = id
        self.wagon_generation = kwargs.get('wagon_generation', None)
        super(WagonConsist, self).__init__(**kwargs)

        roster_obj.register_wagon_consist(self)

        if kwargs.get('speed', None):
            self.speed = kwargs['speed']
        else:
            # eh this is ugly, but it works
            if self.track_type == 'NG':
                if self.wagon_generation == 1:
                    self.speed = roster_obj.speeds['ng_gen_1_wagon_speeds'][speedy]
                elif self.wagon_generation == 2:
                    self.speed = roster_obj.speeds['ng_gen_2_wagon_speeds'][speedy]
                elif self.wagon_generation == 3:
                    self.speed = roster_obj.speeds['ng_gen_3_wagon_speeds'][speedy]
            else:
                if self.wagon_generation == 1:
                    self.speed = roster_obj.speeds['gen_1_wagon_speeds'][speedy]
                elif self.wagon_generation == 2:
                    self.speed = roster_obj.speeds['gen_2_wagon_speeds'][speedy]
                elif self.wagon_generation == 3:
                    self.speed = roster_obj.speeds['gen_3_wagon_speeds'][speedy]

    @property
    def buy_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        capacity_factors = []
        for slice in self.slices:
            if slice.default_cargo == 'PASS':
                # pax coaches have seats and stuff, are expensive to build
                capacity_factors.append(3 * getattr(slice, 'capacities_pax', 0)[1])
            elif slice.default_cargo == 'MAIL':
                # mail cars have pax-grade eqpt, but no seats etc, so moderately expensive
                capacity_factors.append(2 * getattr(slice, 'capacities_mail', 0)[1])
            else:
                capacity_factors.append(getattr(slice, 'capacities_freight', 0)[1])
        cost = cost + sum(capacity_factors)
        return 0.5 * cost # dibble all the things

    @property
    def running_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        if self.slices[0].default_cargo == 'PASS':
            return cost / 4
        elif self.slices[0].default_cargo == 'MAIL':
            return cost / 7
        else:
            return cost / 8


class BoxConsist(WagonConsist):
    """
    Van - express, piece goods cargos, other selected cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'box_car'
        super(BoxConsist, self).__init__(**kwargs)
        self.template = 'car_with_open_doors_during_loading.pynml'
        self.cargo_graphics_mappings = {} # template needs this, but box car has zero cargo-specific graphics, all generic
        self.num_cargo_rows = 1 # template needs this, but box car has zero cargo-specific graphics, all generic
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_capacity_type = 'capacity_freight'

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class CabooseConsist(WagonConsist):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """
    def __init__(self, **kwargs):
        self.base_id = 'caboose_car'
        super(CabooseConsist, self).__init__(**kwargs)
        self.template = 'train.pynml'
        # no graphics processing - don't random colour cabeese, I tried it, looks daft
        self.class_refit_groups = [] # refit nothing, don't mess with this, it breaks auto-replace
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'GOOD' # unwanted side-effect of this is that caboose replaceable by anything refitting goods
        self.default_capacity_type = 'capacity_freight'


class CombineConsist(WagonConsist):
    """
    Novelty single-coach with both pax and mail, for use on very small trains, bit of a hack.
    """
    def __init__(self, **kwargs):
        self.base_id = 'combine_car'
        super(CombineConsist, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.autorefit = True
        self.default_cargo = 'MAIL'
        self.default_capacity_type = 'capacity_mail'


class CoveredHopperConsist(WagonConsist):
    """
    Bulk powder / pellet cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'covered_hopper_car'
        super(CoveredHopperConsist, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['covered_hopper_freight']
        self.label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ', 'FOOD', 'SUGR', 'FMSP', 'RFPR', 'CLAY', 'BDMT', 'BEAN', 'NITR', 'RUBR', 'SAND']
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GRAI'
        self.default_capacity_type = 'capacity_freight'
        self.loading_speed_multiplier = 2

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class EdiblesTankConsist(WagonConsist):
    """
    Wine, milk, water etc.
    """
    def __init__(self, **kwargs):
        self.base_id = 'edibles_tank_car'
        super(EdiblesTankConsist, self).__init__(**kwargs)
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.template = 'train.pynml'
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = ['FOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_edible_liquids']
        self.autorefit = True
        self.default_cargo = 'WATR'
        self.default_capacity_type = 'capacity_freight'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class FlatConsist(WagonConsist):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """
    def __init__(self, **kwargs):
        self.base_id = 'flat_car'
        super(FlatConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        # cargo rows 0 indexed - 0 = first set of loaded sprites
        self.cargo_graphics_mappings = {'STEL': [1, 2, 3], 'WOOD': [4], 'WDPR': [5], 'ENSP': [6], 'FMSP': [6], 'MNSP': [6], 'GOOD': [0, 6]}
        self.num_cargo_rows = 7
        self.class_refit_groups = ['flatcar_freight']
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight']
        self.autorefit = True
        self.default_cargo = 'STEL'
        self.default_capacity_type = 'capacity_freight'

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class FruitConsist(WagonConsist):
    """
    Fruit cargo, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'fruit_car'
        super(FruitConsist, self).__init__(**kwargs)
        self.template = 'car_with_open_doors_during_loading.pynml'
        self.cargo_graphics_mappings = {} # template needs this, but box car has zero cargo-specific graphics, all generic
        self.num_cargo_rows = 1 # template needs this, but box car has zero cargo-specific graphics, all generic
        self.class_refit_groups = []
        self.label_refits_allowed = ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS']
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'FRUT'
        self.default_capacity_type = 'capacity_freight'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class HopperConsist(WagonConsist):
    """
    Limited set of bulk (mineral) cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'hopper_car'
        super(HopperConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        # cargo rows 0 indexed - 0 = first set of loaded sprites
        # GRVL is in first position as it is re-used for generic unknown cargos
        # hoppers *do* transport SCMT in this set, realism is not relevant here, went back and forth on this a few times :P
        self.cargo_graphics_mappings = {'GRVL': [0], 'IORE': [1], 'CORE': [2], 'AORE': [3],
                                   'SAND': [4], 'COAL': [5], 'CLAY': [6], 'SCMT': [7], 'PHOS': [8],
                                   'CASS': [9], 'LIME': [10], 'MNO2': [11], 'NITR': [12],
                                   'PORE': [13], 'POTA': [14], 'SGBT': [15]}
        self.num_cargo_rows = 16 # update if more cargo graphic variations are added
        self.class_refit_groups = ['hopper_freight']
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight']
        self.autorefit = True
        self.default_cargo = 'COAL'
        self.default_capacity_type = 'capacity_freight'
        self.loading_speed_multiplier = 2


class IntermodalConsist(WagonConsist):
    """
    Specialist intermodal (containers), limited range of cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'intermodal_flat_car'
        super(IntermodalConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        self.cargo_graphics_mappings = {}
        self.num_cargo_rows = 3
        self.generic_cargo_rows = [0, 1, 2]
        self.class_refit_groups = ['express_freight', 'packaged_freight']
        #label_refits_allowed = list(cargo_graphics_mappings.keys())
        # maintain other sets (e.g. Squid etc) when changing container refits
        self.label_refits_allowed = ['FRUT','WATR']
        self.label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD']
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_capacity_type = 'capacity_freight'
        self.loading_speed_multiplier = 2


class LivestockConsist(WagonConsist):
    """
    Livestock, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'livestock_car'
        super(LivestockConsist, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = []
        self.label_refits_allowed = ['LVST']
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'LVST'
        self.default_capacity_type = 'capacity_freight'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD


class MailConsist(WagonConsist):
    """
    Express freight - mail, valuables etc.
    """
    def __init__(self, **kwargs):
        self.base_id = 'mail_car'
        super(MailConsist, self).__init__(**kwargs)
        self.template = 'car_with_open_doors_during_loading.pynml'
        self.cargo_graphics_mappings = {} # template needs this, but mail car has zero cargo-specific graphics, all generic
        self.num_cargo_rows = 1 # template needs this, but mail car has zero cargo-specific graphics, all generic
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.autorefit = True
        self.default_cargo = 'MAIL'
        self.default_capacity_type = 'capacity_mail'


class MetalConsist(WagonConsist):
    """
    Specialist heavy haul metal transport e.g. torpedo car, ladle, etc
    High capacity, not very fast, refits to small subset of finished metal cargos.
    """
    def __init__(self, **kwargs):
        self.base_id = 'metal_car'
        super(MetalConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        self.cargo_graphics_mappings = {}
        self.num_cargo_rows = 1
        self.generic_cargo_rows = [0]
        self.class_refit_groups = []
        self.label_refits_allowed = ['STEL', 'COPR']
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'STEL'
        self.default_capacity_type = 'capacity_freight'
        self.loading_speed_multiplier = 2


class OpenConsist(WagonConsist):
    """
    General cargo - refits everything except mail, pax.
    """
    def __init__(self, **kwargs):
        self.base_id = 'open_car'
        super(OpenConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        b = 1 # bulk cargo start row
        # cargo rows 0 indexed - 0 = first set of loaded sprites
        self.cargo_graphics_mappings = {'GRVL': [b], 'IORE': [b + 1], 'CORE': [b + 2], 'AORE': [b + 3],
                                   'SAND': [b + 4], 'COAL': [b + 5], 'CLAY': [b + 6], 'SCMT': [b + 7], 'PHOS': [b + 8],
                                   'CASS': [b + 9], 'LIME': [b + 10], 'MNO2': [b + 11], 'NITR': [b + 12],
                                   'PORE': [b + 13], 'POTA': [b + 14], 'SGBT': [b + 15]}
        self.num_cargo_rows = 17 # update this when adding cargo graphics
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases']
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_capacity_type = 'capacity_freight'

    @property
    def graphics_processors(self):
        recolour_maps = graphics_processor.utils.get_bulk_cargo_recolour_maps()
        graphics_options_master = {'template': 'filename.png',
                                   'recolour_maps': (recolour_maps),
                                   'copy_block_top_offset': 90,
                                   'num_rows_per_unit': 2,
                                   'num_unit_types': 1}

        graphics_options_1 = dict((k, v) for (k, v) in graphics_options_master.items())
        graphics_options_1['template'] = self.id + '_template_0.png'
        graphics_options_2 = dict((k, v) for (k, v) in graphics_options_1.items())
        graphics_options_2['swap_company_colours'] = True
        pass_through = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options_1)
        swap_company_colours = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options_2)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class PassengerConsist(WagonConsist):
    """
    Passenger coach or wagon
    """
    def __init__(self, **kwargs):
        self.base_id = 'passenger_car'
        super(PassengerConsist, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.cargo_graphics_mappings = {} # template needs this, but reefer car has zero cargo-specific graphics, all generic
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'PASS'
        self.default_capacity_type = 'capacity_pax'


class ReeferConsist(WagonConsist):
    """
    Refrigerated cargos, with improved decay rate
    """
    def __init__(self, **kwargs):
        self.base_id = 'reefer_car'
        super(ReeferConsist, self).__init__(**kwargs)
        self.template = 'car_with_open_doors_during_loading.pynml'
        self.cargo_graphics_mappings = {} # template needs this, but reefer car has zero cargo-specific graphics, all generic
        self.num_cargo_rows = 1 # template needs this, but box car has zero cargo-specific graphics, all generic
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'FOOD'
        self.default_capacity_type = 'capacity_freight'
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class SuppliesConsist(WagonConsist):
    """
    Specialist vehicle for supplies and building materials
    """
    def __init__(self, **kwargs):
        self.base_id = 'supplies_car'
        super(SuppliesConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        # cargo rows 0 indexed - 0 = first set of loaded sprites
        self.cargo_graphics_mappings = {'ENSP': [0, 1, 2, 3, 4], 'FMSP': [0, 1, 2, 3, 4], 'VEHI': [0, 1, 2, 3, 4], 'BDMT': [0, 1]}
        self.num_cargo_rows = 5
        self.class_refit_groups = []
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'ENSP'
        self.default_capacity_type = 'capacity_freight'
        self.date_variant_var = 'current_year'

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class TankConsist(WagonConsist):
    """
    All non-edible liquid cargos
    """
    def __init__(self, **kwargs):
        self.base_id = 'tank_car'
        super(TankConsist, self).__init__(**kwargs)
        self.template = 'car_with_cargo_specific_liveries.pynml'
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they also change livery at stations if refitted between certain cargo types <shrug>
        self.cargo_graphics_mappings = {'OIL_': [0], 'PETR': [1], 'RFPR': [2]}
        self.num_cargo_rows = 3 # update if more cargo graphic variations are added
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label['edible_liquids']
        self.autorefit = True
        self.default_cargo = 'OIL_'
        self.default_capacity_type = 'capacity_freight'
        self.loading_speed_multiplier = 3

    # !! tank cars need a different graphics processor, dedicated to recolouring livery per supported cargo
    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class VehicleTransporterConsist(WagonConsist):
    """
    Transports vehicles cargo
    """
    def __init__(self, **kwargs):
        self.base_id = 'vehicle_transporter_car'
        super(VehicleTransporterConsist, self).__init__(**kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        # cargo rows 0 indexed - 0 = first set of loaded sprites
        self.cargo_graphics_mappings = {'VEHI': [0, 1]}
        self.num_cargo_rows = 2
        self.class_refit_groups = []
        self.label_refits_allowed = list(self.cargo_graphics_mappings.keys())
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'VEHI'
        self.default_capacity_type = 'capacity_freight'
        self.date_variant_var = 'current_year'

    @property
    def graphics_processors(self):
        options = {'template': self.id + '_template_0.png'}
        pass_through = GraphicsProcessorFactory('pass_through_pipeline', options)
        swap_company_colours = GraphicsProcessorFactory('swap_company_colours_pipeline', options)
        return {'pass_through': pass_through, 'swap_company_colours': swap_company_colours}


class Wagon(Train):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by Train with useful defaults.
    """
    def __init__(self, **kwargs):
        super(Wagon, self).__init__(**kwargs)
        self.consist = kwargs['consist']
        self.template = self.consist.template
        self.class_refit_groups = self.consist.class_refit_groups
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        if hasattr(self.consist, 'autorefit'):
            self.autorefit = self.consist.autorefit
        self.default_cargo = self.consist.default_cargo
        self.default_cargo_capacities = self.get_capacity_variations(kwargs.get(self.consist.default_capacity_type, 0))
        if hasattr(self.consist, 'loading_speed_multiplier'):
            self.loading_speed_multiplier = self.consist.loading_speed_multiplier
        if hasattr(self.consist, 'cargo_age_period'):
            self.cargo_age_period = self.consist.cargo_age_period


class SteamLoco(Train):
    """
    Steam Locomotive.
    """
    def __init__(self, **kwargs):
        super(SteamLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.visual_effect = 'VISUAL_EFFECT_STEAM'
        self.default_visual_effect_offset = 'FRONT'


class SteamLocoTender(Train):
    """
    Steam Locomotive Tender.
    """
    def __init__(self, **kwargs):
        super(SteamLocoTender, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]


class DieselLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, **kwargs):
        super(DieselLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class DieselRailcar(Train):
    """
    Diesel Railcar (Single Unit).
    """
    def __init__(self, **kwargs):
        super(DieselRailcar, self).__init__(**kwargs)
        self.template = 'railcar.pynml'
        self.default_cargo_capacities = [0]
        self.class_refit_groups = ['pax', 'mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]
        self.default_cargo_capacities = self.capacities_pax
        self.default_cargo = 'PASS'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class ElectricLoco(Train):
    """
    Electric Locomotive.
    """
    def __init__(self, **kwargs):
        super(ElectricLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
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
        super(ElectroDieselLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'
        self.consist.visual_effect_override_by_railtype = {'ELRL': 'VISUAL_EFFECT_ELECTRIC'}


class CargoSprinter(Train):
    """
    Freight Multiple Unit.
    """
    def __init__(self, **kwargs):
        super(CargoSprinter, self).__init__(**kwargs)
        self.template = 'cargo_sprinter.pynml'
        self.default_cargo_capacities = [0]
        # refits should match those of the intermodal cars
        self.class_refit_groups = ['express_freight', 'packaged_freight']
        self.label_refits_allowed = ['FRUT','WATR']
        self.label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD']
        self.autorefit = True
        self.default_cargo_capacities = self.capacities_freight
        self.loading_speed_multiplier = 2
        self.default_cargo = 'GOOD'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # intended - positioning smoke correctly for this vehicle type is too fiddly
        self.consist.num_random_cargo_variants = kwargs.get('num_random_cargo_variants')
        self.consist.cargos_with_tanktainer_graphics = kwargs.get('cargos_with_tanktainer_graphics')


class MailCar(Wagon):
    """
    Mail Carriage.
    """
    def __init__(self, **kwargs):
        super(MailCar, self).__init__(**kwargs)
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]


class CombineCar(Wagon):
    """
    Carriage that offers capacity for both passengers (fixed) and mail / express cargo (refittable)
    """
    # this class is sparse - it exists to make special case handling easy by checking class type
    # combine car needs to set capacity_mail, capacity_freight, and capacity_pax
    # pax capacity is non-refittable and applied to lead slice of the unit
    def __init__(self, **kwargs):
        super(CombineCar, self).__init__(**kwargs)


class BoxCar(Wagon):
    """
    Box Car.
    """
    # this sub-class only exists to handle the mail capacity, otherwise it's a standard wagon
    def __init__(self, **kwargs):
        super(BoxCar, self).__init__(**kwargs)
        self.capacities_mail = [int(2.0 * capacity) for capacity in self.capacities_freight]


class MetroPaxUnit(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super(MetroPaxUnit, self).__init__(**kwargs)
        self.template = 'metro_mu.pynml'
        self.default_cargo_capacities = self.capacities_pax
        self.default_cargo = "PASS"
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'


class MetroCargoUnit(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super(MetroCargoUnit, self).__init__(**kwargs)
        self.template = 'metro_mu.pynml'
        self.default_cargo_capacities = [0]
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]
        self.default_cargo_capacities = self.capacities_mail
        self.default_cargo = "MAIL"
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'

