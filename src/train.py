import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src'))  # add to the module search path

import math
# only used for deprecated attempt at partial compiles, remove (and vehicle_module_path var)
import inspect
# python builtin templater might be used in some utility cases
from string import Template

# chameleon used in most template cases
from chameleon import PageTemplateLoader
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import polar_fox
import global_constants  # expose all constants for easy passing to templates
import utils

from gestalt_graphics.gestalt_graphics import (GestaltGraphics, GestaltGraphicsVisibleCargo, GestaltGraphicsBoxCarOpeningDoors,
                                               GestaltGraphicsCaboose, GestaltGraphicsCargoSpecificLivery,
                                               GestaltGraphicsConsistSpecificLivery, GestaltGraphicsCustom)
import gestalt_graphics.graphics_constants as graphics_constants

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
        # private var, used to store a name substr for engines, composed into name with other strings as needed
        self._name = kwargs.get('name', None)
        self.base_numeric_id = kwargs.get('base_numeric_id', None)
        # either gen xor intro_date is required, don't set both, one will be interpolated from the other
        self._gen = kwargs.get('gen', None)
        self._intro_date = kwargs.get('intro_date', None)
        self.vehicle_life = kwargs.get('vehicle_life', 40)
        self.power = kwargs.get('power', 0)
        self.track_type = kwargs.get('track_type', 'RAIL')
        self.tractive_effort_coefficient = kwargs.get(
            'tractive_effort_coefficient', 0.3)  # 0.3 is recommended default value
        # private var, can be used to over-rides default (per generation, per class) speed
        self._speed = kwargs.get('speed', None)
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_railtype = kwargs.get('power_by_railtype', None)
        self.visual_effect_override_by_railtype = kwargs.get(
            'visual_effect_override_by_railtype', None)
        self.dual_headed = 1 if kwargs.get('dual_headed', False) else 0
        # random_reverse means (1) randomised reversing of sprites when vehicle is built (2) player can also flip vehicle
        # random_reverse is not supported in some templates
        self.random_reverse = kwargs.get('random_reverse', False)
        self.allow_flip = self.random_reverse # random_reverse vehicles can always be flipped, but flip can also be set in other cases (by subclass)
        # arbitrary adjustments of points that can be applied to adjust buy cost and running cost, over-ride in consist as needed
        # values can be -ve or +ve to dibble specific vehicles (but total calculated points cannot exceed 255)
        self.type_base_buy_cost_points = kwargs.get(
            'type_base_buy_cost_points', 15)
        self.type_base_running_cost_points = kwargs.get(
            'type_base_running_cost_points', 15)
        # create structure to hold the units
        self.units = []
        # one default cargo for the whole consist, no mixed cargo shenanigans, it fails with auto-replace
        self.default_cargos = []
        # create a structure for cargo /livery graphics options
        self.gestalt_graphics = GestaltGraphics()
        # option to provide automatic roof for all units in the consist
        self.generate_unit_roofs = False
        # option to swap company colours (uses remap sprites in-game, rather than pixa)
        self.random_company_colour_swap = False  # over-ride in subclasses as needed
        # role is e.g. Heavy Freight, Express etc, and is used to automatically set model life as well as in docs
        self.role = kwargs.get('role', None)
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        self.roster_id = None
        # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get(
            'suppress_animated_pixel_warnings', False)
        # aids 'project management'
        self.sprites_complete = kwargs.get('sprites_complete', False)

    def add_unit(self, type, repeat=1, **kwargs):
        unit = type(consist=self, **kwargs)
        count = len(self.unique_units)
        if count == 0:
            # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
            unit.id = self.id
        else:
            unit.id = self.id + '_' + str(count)
        unit.numeric_id = self.get_and_verify_numeric_id(count)
        for repeat_num in range(repeat):
            self.units.append(unit)

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
            utils.echo_message("Error: numeric_id " + str(numeric_id) + " for " +
                               self.id + " can't be used (16383 is max ID for articulated vehicles)")
        # non-blocking guard on duplicate IDs
        for id in numeric_id_defender:
            if id == numeric_id:
                utils.echo_message("Error: consist " + self.id + " unit id collides (" +
                                   str(numeric_id) + ") with units in another consist")
        numeric_id_defender.append(numeric_id)
        return numeric_id

    @property
    def reversed_variants(self):
        # Handles 'unreversed' and optional 'reversed' variant, which if provided, will be chosen at random per consist
        # NOT the same as 'flipped' which is a player choice in-game, and handled separately
        # Previous model_variant approach for this was deprecated March 2018, needlessly complicated
        result = ['unreversed']
        if self.random_reverse:
            result.append('reversed')
        return result

    @property
    def name(self):
        return "string(STR_NAME_CONSIST, string(STR_NAME_" + self.id + "), string(" + self.str_name_suffix + "))"

    def unit_requires_variable_power(self, vehicle):
        if self.power_by_railtype is not None and vehicle.is_lead_unit_of_consist:
            return True
        else:
            return False

    def get_spriterows_for_consist_or_subpart(self, units):
        # pass either list of all units in consist, or a slice of the consist starting from front (arbitrary slices not useful)
        # spriterow count is number of output sprite rows from graphics processor
        result = []
        for unit in units:
            unit_rows = []
            if unit.always_use_same_spriterow:
                unit_rows.append(('always_use_same_spriterow', 1))
            else:
                # assumes gestalt_graphics is used to handle any other rows, no other cases at time of writing, could be changed eh?
                unit_rows.extend(
                    self.gestalt_graphics.get_output_row_counts_by_type())
            result.append(unit_rows)
        return result

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
            assert(self._gen == None), "%s consist has both gen and intro_date set, which is incorrect" % self.id
            return self._intro_date
        else:
            assert(self._gen != None), "%s consist has neither gen nor intro_date set, which is incorrect" % self.id
            return self.roster.intro_dates[self.gen - 1]

    @property
    def gen(self):
        # gen is usually set in the vehicle, but can be left unset if intro_date is set
        if self._gen:
            assert(self._intro_date == None), "%s consist has both gen and intro_date set, which is incorrect" % self.id
            return self._gen
        else:
            assert(self._intro_date != None), "%s consist has neither gen nor intro_date set, which is incorrect" % self.id
            for gen_counter, intro_date in enumerate(self.roster.intro_dates):
                if self.intro_date < intro_date:
                    return gen_counter
            # if no result is found in list, it's last gen
            return len(self.roster.intro_dates)

    @property
    def livery_2_engine_ids(self):
        # for vehicles with consist-specific liveries
        # will switch vehicle to livery 2 for specific roles of lead engine
        result = []
        for consist in self.roster.engine_consists:
            if consist.role in ['express_1', 'express_2']:
                result.append(consist.id)
        return result

    @property
    def model_life(self):
        similar_consists = []
        for consist in self.roster.engine_consists:
            if consist.role == self.role:
                # no way to avoid railtype-specific handling here
                if self.track_type in ['NG', 'METRO']:
                    # exact match required for these types
                    if self.track_type == consist.track_type:
                        similar_consists.append(consist)
                elif self.track_type in ['RAIL', 'ELRL']:
                    # for vehicle replacement purposes, RAIL and ELRL are cross-compatible
                    if consist.track_type in ['RAIL', 'ELRL']:
                        similar_consists.append(consist)
                else:
                    raise Exception('track_type for consist ' +
                                    self.id + ' unrecognised in model_life method')
        replacement_consist = None
        for consist in sorted(similar_consists, key=lambda consist: consist.intro_date):
            if consist.intro_date > self.intro_date:
                replacement_consist = consist
                break
        if replacement_consist is None:
            return 'VEHICLE_NEVER_EXPIRES'
        else:
            return replacement_consist.intro_date - self.intro_date

    @property
    def retire_early(self):
        # affects when vehicle is removed from buy menu (in combination with model life)
        # to understand why this is needed see https://newgrf-specs.tt-wiki.net/wiki/NML:Vehicles#Engine_life_cycle
        # retire at end of model life + 10 (fudge factor - no need to be more precise than that)
        return -10

    @property
    def speed(self):
        # automatic speed, but can over-ride by passing in kwargs for consist
        if self._speed:
            return self._speed
        elif self.speed_class:
            # speed by class, if speed_class is not None
            # !! eh this relies currently on railtypes being 'RAIL' or 'NG'
            # it only works because electric engines currently have their speed set explicitly :P
            # could be fixed by checking a list of railtypes
            return self.roster.speeds[self.track_type][self.speed_class][self.gen - 1]
        else:
            # assume no speed limit
            return None

    @property
    def weight(self):
        return sum([getattr(unit, 'weight', 0) for unit in self.units])

    @property
    def roster(self):
        for roster in registered_rosters:
            if roster.id == self.roster_id:
                return roster

    def get_expression_for_rosters(self):
        # the working definition is one and only one roster per vehicle
        return 'param[1]==' + str(self.roster.numeric_id - 1)

    def get_nml_expression_for_default_cargos(self):
        # sometimes first default cargo is not available, so we use a list
        # this avoids unwanted cases like box cars defaulting to mail when goods cargo not available
        # if there is only one default cargo, the list just has one entry, that's no problem
        if len(self.default_cargos) == 1:
            return self.default_cargos[0]
        else:
            # build stacked ternary operators for cargos
            result = self.default_cargos[-1]
            for cargo in reversed(self.default_cargos[0:-1]):
                result = 'cargotype_available("' + \
                    cargo + '")?' + cargo + ':' + result
            return result

    @property
    def buy_menu_x_loc(self):
        # automatic buy menu sprite if single-unit consist
        # extend this to check an auto_buy_menu_sprite property if manual over-rides are needed in future
        if len(self.units) == 1:
            return global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[6][0]
        else:
            return 316  # hard-coded default case

    @property
    def buy_menu_width(self):
        # max sensible width in buy menu is 64px
        consist_length = 4 * sum([unit.vehicle_length for unit in self.units])
        if consist_length < 64:
            return consist_length
        else:
            return 64

    def render_articulated_switch(self):
        if len(self.units) > 1:
            template = templates["articulated_parts.pynml"]
            nml_result = template(
                consist=self, global_constants=global_constants)
            return nml_result
        else:
            return ''

    def render(self):
        # templating
        nml_result = ''
        if len(self.units) > 1:
            nml_result = nml_result + self.render_articulated_switch()
        for unit in self.unique_units:
            nml_result = nml_result + unit.render()
        return nml_result


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
            utils.echo_message("Consist " + self.id +
                               " has power > 8000hp, which is too much")
        power_cost_points = self.power / 100

        # Up to 20 points for speed up to 80mph. 1 point per 2mph
        speed_cost_points = min(self.speed, 80) / 2

        # Up to 80 points for speed above 80mph up to 200mph. 1 point per 1.5mph
        if self.speed > 200:
            utils.echo_message("Consist " + self.id +
                               " has speed > 200, which is too much")
        high_speed_cost_points = max((self.speed - 80), 0) / 1.5

        # Up to 40 points for intro date after 1870. 1 point per 4 years.
        # Intro dates capped at 2030, this isn't a hard limit, but raise a warning
        if self.intro_date > 2030:
            utils.echo_message("Consist " + self.id +
                               " has intro_date > 2030, which is too much")
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


class PassengerEngineConsist(EngineConsist):
    """
    Consist of engines / units that has passenger capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = ['PASS']


class PassengerEngineRailcarConsist(PassengerEngineConsist):
    """
    Consist for a pax railcar.  Just a sparse subclass to force the gestalt_graphics and allow_flip
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # Graphics configuration
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="pax_railcars")


class MailEngineConsist(EngineConsist):
    """
    Consist of engines / units that has mail (and express freight) capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ['TOUR']
        self.default_cargos = ['MAIL']


class MailEngineRailcarConsist(MailEngineConsist):
    """
    Consist for a mail railcar.  Just a sparse subclass to force the gestalt_graphics and allow_flip
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # Graphics configuration
        # by design, mail railcars don't change livery in a pax consist, but do have mail / freight liveries
        spriterow_group_mappings = {'mail': {'default': 0, 'first': 1, 'last': 2, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="mail_railcars")

class CarConsist(Consist):
    """
    Intermediate class for car (wagon) consists to subclass from, provides sparse properties, most are declared in subclasses.
    """

    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs['id'] = id
        super().__init__(**kwargs)

        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get('roster', None)
        self.roster.register_wagon_consist(self)

        self.speed_class = 'freight'  # over-ride this for, e.g. fast_freight consists
        self.subtype = kwargs['subtype']
        self.weight_factor = 0.5  # over-ride in sub-class as needed
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        self.cargo_age_period = kwargs.get(
            'cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        # assume all wagons randomly swap CC, revert to False in wagon subclasses as needed
        self.random_company_colour_swap = True
        # default value, adjust this in subclasses to modify buy cost for more complex cars
        self.capacity_cost_factor = 1
        # default value, adjust this in subclasses to modify run cost for more complex cars
        self.run_cost_divisor = 8

    @property
    def buy_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        capacity_factors = []
        for unit in self.units:
            capacity_factors.append(
                unit.default_cargo_capacity * self.capacity_cost_factor)
        cost = cost + sum(capacity_factors)
        return 0.5 * cost  # dibble all the things

    @property
    def running_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        return cost / self.run_cost_divisor

    @property
    def model_life(self):
        # automatically span wagon model life across gap to next generation
        roster_gens_for_class = sorted(set(
            [wagon.gen for wagon in self.roster.wagon_consists[self.base_id] if wagon.subtype == self.subtype]))
        this_index = roster_gens_for_class.index(self.gen)
        if this_index == len(roster_gens_for_class) - 1:
            return 'VEHICLE_NEVER_EXPIRES'
        else:
            next_gen = roster_gens_for_class[roster_gens_for_class.index(
                self.gen) + 1]
            gen_span = next_gen - self.gen
            return 10 + (30 * gen_span)

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get('track_type', None) == 'NG':
            id_base = id_base + '_ng'
        result = '_'.join((id_base, kwargs['roster'], 'gen', str(
            kwargs['gen']) + str(kwargs['subtype'])))
        return result

    def get_wagon_title_class_str(self):
        return 'STR_NAME_SUFFIX_' + self.base_id.upper()

    def get_wagon_title_subtype_str(self):
        if self.subtype == 'A':
            subtype_str = 'STR_NAME_SUFFIX_SMALL'
        elif self.subtype == 'B':
            subtype_str = 'STR_NAME_SUFFIX_MEDIUM'
        elif self.subtype == 'C':
            subtype_str = 'STR_NAME_SUFFIX_LARGE'
        return subtype_str

    @property
    def name(self):
        return "string(STR_NAME_CONSIST, string(" + self.get_wagon_title_class_str() + "), string(" + self.get_wagon_title_subtype_str() + "))"


class BoxCarConsist(CarConsist):
    """
    Box car, van - express, piece goods cargos, other selected cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'box_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = global_constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['box']
        # Graphics configuration
        self.generate_unit_roofs = True
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(recolour_maps=graphics_constants.box_livery_recolour_maps)


class CabooseCarConsist(CarConsist):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """

    def __init__(self, **kwargs):
        self.base_id = 'caboose_car'
        super().__init__(**kwargs)
        self.speed_class = None  # no speed limit
        # refit nothing, don't mess with this, it breaks auto-replace
        self.class_refit_groups = []
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        # liveries swap CC on user-flip, so no swapping CC randomly
        self.random_company_colour_swap = False
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(num_generations=len(self.roster.intro_dates),
                                                       recolour_maps=graphics_constants.caboose_livery_recolour_maps)


class CoveredHopperCarConsist(CarConsist):
    """
    Bulk cargos needing covered protection.
    """

    def __init__(self, **kwargs):
        self.base_id = 'covered_hopper_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ', 'SUGR', 'FMSP', 'RFPR', 'CLAY', 'BDMT',
                                     'BEAN', 'NITR', 'RUBR', 'SAND', 'POTA', 'QLME', 'SASH', 'CMNT', 'KAOL', 'FERT', 'SALT', 'CBLK']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['covered_hopper']
        self.loading_speed_multiplier = 2


class DumpCarConsist(CarConsist):
    """
    Limited set of bulk (mineral) cargos, same set as hopper cars.
    """

    def __init__(self, **kwargs):
        self.base_id = 'dump_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['dump_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_dump_bulk']
        self.default_cargos = global_constants.default_cargos['dump']
        self.loading_speed_multiplier = 2
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class EdiblesTankCarConsist(CarConsist):
    """
    Wine, milk, water etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'edibles_tank_car'
        super().__init__(**kwargs)
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.speed_class = 'fast_freight'
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = ['FOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_edible_liquids']
        self.default_cargos = global_constants.default_cargos['edibles_tank']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2
        self.capacity_cost_factor = 1.5


class FlatCarConsist(CarConsist):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """

    def __init__(self, **kwargs):
        self.base_id = 'flat_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_flatbed_freight']
        self.default_cargos = global_constants.default_cargos['flat']
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='flat')


class FruitVegCarConsist(CarConsist):
    """
    Fruit and vegetables, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'fruit_veg_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['fruit_veg']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.capacity_cost_factor = 1.5
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            recolour_maps=graphics_constants.fruit_veg_livery_recolour_maps)


class HopperCarConsist(CarConsist):
    """
    Limited set of bulk (mineral) cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'hopper_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['dump_freight']
        self.label_refits_allowed = []  # none needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_dump_bulk']
        self.default_cargos = global_constants.default_cargos['hopper']
        self.loading_speed_multiplier = 2
        self.capacity_cost_factor = 1.5
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class IntermodalCarConsist(CarConsist):
    """
    Specialist intermodal (containers), limited range of cargos. Match cargos and speed to BoxCarConsist
    """

    def __init__(self, **kwargs):
        self.base_id = 'intermodal_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = global_constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['box']
        self.loading_speed_multiplier = 2


class LivestockCarConsist(CarConsist):
    """
    Livestock, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'livestock_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['LVST']
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = ['LVST']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.capacity_cost_factor = 1.5
        self.run_cost_divisor = 7
        # Graphics configuration
        self.generate_unit_roofs = True
        self.gestalt_graphics = GestaltGraphicsCargoSpecificLivery(
            recolour_maps=graphics_constants.livestock_livery_recolour_maps)


class MailCarConsist(CarConsist):
    """
    Mail cars - also handle express freight, valuables.
    """

    def __init__(self, **kwargs):
        self.base_id = 'mail_car'
        super().__init__(**kwargs)
        self.speed_class = 'pax_mail'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['mail']
        self.random_company_colour_swap = False
        self.capacity_cost_factor = 1.5
        self.run_cost_divisor = 7
        self.allow_flip = True
        # Graphics configuration
        # longer mail cars get an additional sprite option in the consist ruleset; shorter mail cars don't as it's TMWFTLB
        bonus_sprites = 1 if self.subtype == 'C' else 0
        spriterow_group_mappings = {'mail': {'default': 0, 'first': bonus_sprites, 'last': bonus_sprites, 'special': 0},
                                    'pax': {'default': 0, 'first': 0, 'last': 0, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset='mail_cars')


class MetalCarConsist(CarConsist):
    """
    Specialist heavy haul metal transport e.g. torpedo car, ladle, etc
    High capacity, not very fast, refits to small subset of finished metal cargos (and slag, which bends the rules a bit).
    """

    def __init__(self, **kwargs):
        self.base_id = 'metal_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['STEL', 'COPR', 'IRON', 'SLAG', 'METL']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['metal']
        self.loading_speed_multiplier = 2
        self.capacity_cost_factor = 1.5
        self.run_cost_divisor = 7
        # !! probably want some capacity multiplier here, metal cars have higher capacity per unit length (at high cost!)


class OpenCarConsist(CarConsist):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        self.base_id = 'open_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['open']
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True,
                                                            piece='open')


class PassengerCarConsistBase(CarConsist):
    """
    Common base class for passenger cars.
    """

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = 'pax_mail'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['pax']
        self.random_company_colour_swap = False
        self.allow_flip = True
        # Graphics configuration
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset='pax_cars')


class PassengerCarConsist(PassengerCarConsistBase):
    """
    Standard pax car.
    """

    def __init__(self, **kwargs):
        self.base_id = 'passenger_car'
        super().__init__(**kwargs)
        self.capacity_cost_factor = 2
        self.run_cost_divisor = 5


class PassengerLuxuryCarConsist(PassengerCarConsistBase):
    """
    Improved decay rate and lower capacity per unit length compared to standard pax car.
    Possibly random sprites for restaurant car, observation car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'luxury_passenger_car'
        super().__init__(**kwargs)
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.capacity_cost_factor = 3
        self.run_cost_divisor = 3


class ReeferCarConsist(CarConsist):
    """
    Refrigerated cargos, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'reefer_car'
        super().__init__(**kwargs)
        self.speed_class = 'fast_freight'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['reefer']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.capacity_cost_factor = 1.5
        self.run_cost_divisor = 6
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            recolour_maps=graphics_constants.refrigerated_livery_recolour_maps)


class SiloCarConsist(CarConsist):
    """
    Powder bulk cargos needing protection and special equipment for unloading.
    """

    def __init__(self, **kwargs):
        self.base_id = 'silo_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = [
            'FOOD', 'SUGR', 'FMSP', 'RFPR', 'BDMT', 'RUBR', 'QLME', 'SASH', 'CMNT']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['silo']
        self.loading_speed_multiplier = 2
        self.capacity_cost_factor = 1.5
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCargoSpecificLivery(
            recolour_maps=graphics_constants.silo_livery_recolour_maps)


class StakeCarConsist(CarConsist):
    """
    Specialist transporter for logs, pipes and similar
    """

    def __init__(self, **kwargs):
        self.base_id = 'stake_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        # limited refits by design eh
        self.label_refits_allowed = ['WOOD', 'WDPR', 'PIPE']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['stake']
        self.loading_speed_multiplier = 2
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCustom({'WOOD': [0]},
                                                      'vehicle_with_visible_cargo.pynml',
                                                      generic_rows=[0])


class SuppliesCarConsist(CarConsist):
    """
    Specialist vehicle for supplies and building materials
    """

    def __init__(self, **kwargs):
        self.base_id = 'supplies_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['ENSP', 'FMSP', 'VEHI']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['supplies']


class TankCarConsist(CarConsist):
    """
    All non-edible liquid cargos
    """

    def __init__(self, **kwargs):
        self.base_id = 'tank_car'
        super().__init__(**kwargs)
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they also change livery at stations if refitted between certain cargo types <shrug>
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = []
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'edible_liquids']
        self.default_cargos = global_constants.default_cargos['tank']
        self.loading_speed_multiplier = 3
        self.gestalt_graphics.tanker = True
        self.capacity_cost_factor = 1.5
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCargoSpecificLivery(
            recolour_maps=polar_fox.constants.tanker_livery_recolour_maps)


class VehicleTransporterCarConsist(CarConsist):
    """
    Transports vehicles cargo
    """

    def __init__(self, **kwargs):
        self.base_id = 'vehicle_transporter_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['VEHI']
        self.label_refits_disallowed = []
        self.default_cargos = ['VEHI']


class Train(object):
    """Base class for all types of trains"""

    def __init__(self, **kwargs):
        self.consist = kwargs.get('consist')

        # setup properties for this train
        self.numeric_id = kwargs.get('numeric_id', None)
        self.cargo_age_period = kwargs.get(
            'cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self.vehicle_length = kwargs.get('vehicle_length', None)
        self._weight = kwargs.get('weight', None)
        self.capacity = kwargs.get('capacity', 0)
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        # spriterow_num allows assigning sprites for multi-part vehicles, and is not supported in all vehicle templates (by design - TMWFTLB to support)
        self.spriterow_num = kwargs.get('spriterow_num', 0) # first row = 0;
        # set defaults for props otherwise set by subclass as needed (not set by kwargs as specific models do not over-ride them)
        self.class_refit_groups = []
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.tilt_bonus = False  # over-ride in subclass as needed
        # nml constant (STEAM is sane default)
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.visual_effect = 'VISUAL_EFFECT_DISABLE'  # nml constant
        # optional, use to over-ride automatic effect positioning
        self._visual_effect_offset = kwargs.get('visual_effect_offset', None)
        # optional - some consists have sequences like A1-B-A2, where A1 and A2 look the same but have different IDs for implementation reasons
        # avoid duplicating sprites on the spritesheet by forcing A2 to use A1's spriterow_num, fiddly eh?
        # ugly, but eh.  Zero-indexed, based on position in units[]
        # watch out for repeated vehicles in the consist when calculating the value for this)
        # !! I don't really like this solution, might be better to have the graphics processor duplicate this?, with a simple map of [source:duplicate_to]
        self.unit_num_providing_spriterow_num = kwargs.get(
            'unit_num_providing_spriterow_num', None)
        # optional - force always using same spriterow
        # for cases where the template handles cargo, but some units in the consist might not show cargo, e.g. tractor units etc
        # can also be used to suppress compile failures during testing when spritesheet is unfinished (missing rows etc)
        self.always_use_same_spriterow = kwargs.get(
            'always_use_same_spriterow', False)
        # optional -only set if the graphics processor requires it to generate cargo sprites
        # defines the size of cargo sprite to use
        # if the vehicle cargo area is not an OTTD unit length, use the next size up and the masking will sort it out
        # some longer vehicles may place multiple shorter cargo sprites, e.g. 7/8 vehicle, 2 * 4/8 cargo sprites (with some overlapping)
        self.cargo_length = kwargs.get('cargo_length', None)
        # optional - only set if the graphics processor generates the vehicle chassis
        self.chassis = kwargs.get('chassis', 'test')
        # optional - only set if the graphics processor generates the vehicle roof
        self.roof = kwargs.get('roof', None)
        # 'symmetric' or 'asymmetric'?
        # defaults to symmetric, over-ride in sub-classes or per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [int(math.ceil(capacity * multiplier)) for multiplier in global_constants.capacity_multipliers]

    @property
    def capacities(self):
        return self.get_capacity_variations(self.capacity)

    @property
    def default_cargo_capacity(self):
        return self.capacities[1]

    @property
    def has_cargo_capacity(self):
        if self.default_cargo_capacity is not 0:
            return True
        else:
            return False

    @property
    def weight(self):
        # weight can be set explicitly or by methods on subclasses
        return self._weight

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
    def symmetry_type(self):
        assert(self._symmetry_type in ['symmetric', 'asymmetric']), "symmetry_type '%s' is invalid in %s" % (
            self.symmetry_type, self.consist.id)
        return self._symmetry_type

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC']
        if self.consist.allow_flip:
            special_flags.append('TRAIN_FLAG_FLIP')
        if self.autorefit:
            special_flags.append('TRAIN_FLAG_AUTOREFIT')
        if self.tilt_bonus:
            special_flags.append('TRAIN_FLAG_TILT')
        return ','.join(special_flags)

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [cargo_classes.append(
                cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes))  # use set() here to dedupe

    def get_loading_speed(self, cargo_type, capacity_param):
        # ottd vehicles load at different rates depending on type,
        # normalise default loading time for this set to 240 ticks, regardless of capacity
        # openttd loading rates vary by transport type, look them up in wiki to find value to use here to normalise loading time to 240 ticks
        # this is (240 / loading frequency in ticks for transport type) from wiki
        transport_type_rate = 6
        return int(self.loading_speed_multiplier * math.ceil(self.capacities[capacity_param] / transport_type_rate))

    @property
    def running_cost_base(self):
        return {'ENGINE_CLASS_STEAM': 'RUNNING_COST_STEAM',
                'ENGINE_CLASS_DIESEL': 'RUNNING_COST_DIESEL',
                'ENGINE_CLASS_ELECTRIC': 'RUNNING_COST_ELECTRIC'}[self.engine_class]

    def get_offsets(self, flipped=False):
        # offsets can also be over-ridden on a per-model basis by providing this property in the model class
        base_offsets = global_constants.default_spritesheet_offsets[str(
            self.vehicle_length)]
        if flipped:
            flipped_offsets = list(base_offsets[4:8])
            flipped_offsets.extend(base_offsets[0:4])
            return flipped_offsets
        else:
            return base_offsets

    @property
    def vehicle_nml_template(self):
        if not self.always_use_same_spriterow:
            if self.consist.gestalt_graphics.nml_template:
                return self.consist.gestalt_graphics.nml_template
        # default case
        return 'vehicle_default.pynml'

    @property
    def location_of_random_bits_for_random_variant(self):
        return 'FORWARD_SELF(' + str(self.numeric_id - self.consist.base_numeric_id) + ')'

    @property
    def unit_requires_visual_effect(self):
        # tiny compile optimisation
        if self.visual_effect is not 'VISUAL_EFFECT_DISABLE':
            return True
        else:
            return False

    @property
    def visual_effect_offset(self):
        # over-ride this in subclasses as needed (e.g. to move steam engine smoke to front by default
        # vehicles can also over-ride this on init (stored on each model_variant as _visual_effect_offset)
        return 0

    def get_visual_effect_offset(self, reversed_variant):
        # probably-too-magical handling of visual effect offsets
        result = self._visual_effect_offset
        if result is None:
            result = self.visual_effect_offset
        if reversed_variant == 'reversed':
            # sprites will be reversed for this vehicle, so flip the offset location
            result = result * -1
        return result

    def get_nml_for_visual_effect_and_powered_cb(self):
        # ridiculous compile micro-optimisation, some random switches will be dropped if only 1 model variant
        if len(self.consist.reversed_variants) > 1:
            return self.id + "_switch_visual_effect_and_powered_variants"
        else:
            return self.id + "_switch_visual_effect_and_powered_by_variant_" + self.consist.reversed_variants[0]

    def get_nml_for_graphics_switch(self):
        # ridiculous compile micro-optimisation, some random switches will be dropped if only 1 model variant
        if len(self.consist.reversed_variants) > 1:
            return self.id + "_switch_graphics"
        else:
            return self.id + "_switch_graphics_" + self.consist.reversed_variants[0]

    def get_nml_expression_for_cargo_variant_random_switch(self, cargo_id=None):
        # having a method to calculate the nml for this is overkill
        # legacy of multi-part vehicles, where the trigger needed to be run on an adjacent vehicle
        # this could be unpicked and moved directly into the templates
        switch_id = self.id + "_switch_graphics" + ('_' + str(cargo_id) if cargo_id is not None else '')
        return "SELF," + switch_id + ", bitmask(TRIGGER_VEHICLE_NEW_LOAD)"

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        # offset is number of units
        expression_template = Template(
            "[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # offset is number of units
        expression_template = Template(
            "[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ','.join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ','.join(self.label_refits_disallowed)

    def get_cargo_suffix(self):
        return 'string(' + self.cargo_units_refit_menu + ')'

    def assert_random_reverse(self):
        # some templates don't support the random_reverse (by design, they're symmetrical sprites, and reversing bloats the template)
        if self.consist.random_reverse:
            if hasattr(self.consist, 'gestalt_graphics'):
                for nml_template in ['vehicle_with_visible_cargo.pynml',
                                     'vehicle_box_car_with_opening_doors.pynml',
                                     'vehicle_caboose.pynml',
                                     'vehicle_with_cargo_specific_liveries.pynml',
                                     'vehicle_with_consist_specific_liveries.pynml']:
                    assert self.consist.gestalt_graphics.nml_template != nml_template, \
                        "%s has 'random_reverse set True, which isn't supported by nml_template %s" % (self.consist.id, nml_template)

    def assert_auto_flip(self):
        # some templates don't support the auto_flip (by design, they're symmetrical sprites with no livery flip hax, flipping bloats template)
        if self.consist.random_reverse:
            if hasattr(self.consist, 'gestalt_graphics'):
                for nml_template in ['vehicle_with_visible_cargo.pynml',
                                     'vehicle_caboose.pynml',
                                     'vehicle_with_cargo_specific_liveries.pynml',
                                     'vehicle_box_car_with_opening_doors.pynml']:
                    assert self.consist.gestalt_graphics.nml_template != nml_template, \
                        "%s has 'allow_flip set True, which isn't supported by nml_template %s" % (self.consist.id, nml_template)

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " +
                                   i + " which is not defined in the cargo table")

    def render(self):
        # integrity tests
        self.assert_auto_flip()
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        self.assert_random_reverse()
        # test interpolated gen and intro_date
        assert(self.consist.gen), '%s consist.gen is None, which is invalid.  Set gen or intro_date' % self.id
        assert(self.consist.intro_date), '%s consist.gen is None, which is invalid.  Set gen or intro_date' % self.id
        # templating
        template_name = self.vehicle_nml_template
        template = templates[template_name]
        nml_result = template(
            vehicle=self, consist=self.consist, global_constants=global_constants)
        return nml_result


class SteamEngineUnit(Train):
    """
    Unit for a steam engine, with smoke
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.visual_effect = 'VISUAL_EFFECT_STEAM'
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_STEAM'
        self._symmetry_type = 'asymmetric'  # assume all steam engines are asymmetric

    @property
    def visual_effect_offset(self):
        # force steam engine smoke to front by default, can also over-ride per unit for more precise positioning
        return int(math.floor(-0.5 * self.vehicle_length))


class SteamEngineTenderUnit(Train):
    """
    Unit for a steam engine tender.
    Arguably this class is pointless, as it is just passthrough.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # assume all steam engine tenders are asymmetric
        self._symmetry_type = 'asymmetric'


class DieselEngineUnit(Train):
    """
    Unit for a diesel engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_DIESEL'
        # most diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class DieselRailcarUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to force the symmetry type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # diesel railcars are all symmetric
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')


class ElectricEngineUnit(Train):
    """
    Unit for an electric engine.
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
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        # almost all electric engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class ElectroDieselEngineUnit(Train):
    """
    Unit for a bi-mode Locomotive - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'
        self.consist.visual_effect_override_by_railtype = {
            'ELRL': 'VISUAL_EFFECT_ELECTRIC'}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRODIESEL'
        # almost all electro-diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class ElectricPaxUnit(Train):
    """
    Unit for a high-speed, high-power pax electric train, intended to be 2-car, with template magic for cabs etc
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
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        self.tilt_bonus = True
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'


class MetroUnit(Train):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_METRO'
        # metros are asymmetric, with cab at one end of each vehicle only
        self._symmetry_type = 'asymmetric'


class CargoSprinter(Train):
    """
    Unit for a diesel-powered dedicated freight train.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # refits should match those of the intermodal cars
        self.class_refit_groups = ['express_freight', 'packaged_freight']
        self.label_refits_allowed = ['FRUT', 'WATR']
        self.label_refits_disallowed = ['FISH', 'LVST', 'OIL_', 'TOUR', 'WOOD']
        self.loading_speed_multiplier = 2
        self.default_cargos = ['GOOD']
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        # intended - positioning smoke correctly for this vehicle type is too fiddly
        self.visual_effect = 'VISUAL_EFFECT_DISABLE'
        # cargo sprinters are asymmetric, with cab at one end of each vehicle only
        self._symmetry_type = 'asymmetric'
        """
        # legacy graphics processing - needs recreated as GestaltGraphics
        self.consist.recolour_maps = graphics_constants.container_recolour_maps
        self.consist.num_random_cargo_variants = len(self.consist.recolour_maps)
        self.consist.cargos_with_tanktainer_graphics = ['BEER', 'MILK', 'WATR'] # !! unfinished currently??
         # ugh, the graphics consists are applied to the consist in all other cases,
         # but CargoSprinter doesn't have a dedicated consist subclass, so processors are on the unit, with this nasty passthrough
        """


class TrainCar(Train):
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
        if hasattr(self.consist, 'loading_speed_multiplier'):
            self.loading_speed_multiplier = self.consist.loading_speed_multiplier
        if hasattr(self.consist, 'cargo_age_period'):
            self.cargo_age_period = self.consist.cargo_age_period
        if self.consist.generate_unit_roofs:
            self.roof = str(4 * self.vehicle_length) + 'px'
        # most wagons are symmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')

    @property
    def weight(self):
        # set weight based on capacity  * a multiplier from consist (default 0.5 or so)
        return self.consist.weight_factor * self.default_cargo_capacity


class FreightCar(TrainCar):
    """
    Freight wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs.get('capacity', None) is not None:
            print(self.consist.id, ' has a capacity set in init - possibly incorrect',
                  kwargs.get('capacity', None))
        # magic to set freight car capacity subject to length
        self.capacity = kwargs['vehicle_length'] * \
            self.consist.roster.freight_car_capacity_per_unit_length[
                self.consist.track_type][self.consist.gen - 1]


class CabooseCar(TrainCar):
    """
    Caboose Car. This sub-class only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def weight(self):
        # special handling of weight
        return 5 * self.vehicle_length
