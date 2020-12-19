import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src'))  # add to the module search path

import math
import random
# python builtin templater might be used in some utility cases
from string import Template

import polar_fox
import global_constants  # expose all constants for easy passing to templates
import utils

from gestalt_graphics.gestalt_graphics import (GestaltGraphics, GestaltGraphicsVisibleCargo, GestaltGraphicsBoxCarOpeningDoors, GestaltGraphicsEngine,
                                               GestaltGraphicsCaboose, GestaltGraphicsSimpleBodyColourRemaps, GestaltGraphicsOnlyAddPantographs,
                                               GestaltGraphicsConsistSpecificLivery, GestaltGraphicsIntermodal, GestaltGraphicsCustom, GestaltGraphicsVehicleTransporter)
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
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        # private var, used to store a name substr for engines, composed into name with other strings as needed
        self._name = kwargs.get('name', None)
        self.base_numeric_id = kwargs.get('base_numeric_id', None)
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get('roster_id') # just fail if there's no roster
        # either gen xor intro_date is required, don't set both, one will be interpolated from the other
        self._intro_date = kwargs.get('intro_date', None)
        self._gen = kwargs.get('gen', None)
        # if gen is used, the calculated intro date can be adjusted with +ve or -ve offset
        self.intro_date_offset = kwargs.get('intro_date_offset', None)
        # used for synchronising / desynchronising intro dates for groups vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147
        self._intro_date_days_offset = None # defined in subclasses, no need for instances to define this
        self.vehicle_life = kwargs.get('vehicle_life', 40)
        #  most consists are automatically replaced by the next consist in the role tree
        # ocasionally we need to merge two branches of the role, in this case set replacement consist id
        self._replacement_consist_id = kwargs.get('replacement_consist_id', None)
        self.power = kwargs.get('power', 0)
        self.base_track_type = kwargs.get('base_track_type', 'RAIL')
        # modify base_track_type for electric engines when writing out the actual rail type
        # without this, RAIL and ELRL have to be specially handled whenever a list of compatible consists is wanted
        # this *does* need a specific flag, can't rely on unit visual effect or unit engine type props - they are used for other things
        self.requires_electric_rails = False # set by unit subclasses as needed, not a kwarg
        self.tractive_effort_coefficient = kwargs.get('tractive_effort_coefficient', 0.3)  # 0.3 is recommended default value
        # private var, can be used to over-rides default (per generation, per class) speed
        self._speed = kwargs.get('speed', None)
        # default cargo age period, over-ride in subclass as needed
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_railtype = kwargs.get('power_by_railtype', None)
        # some engines require pantograph sprites composited, don't bother setting this unless required
        self.pantograph_type = kwargs.get('pantograph_type', None)
        self.dual_headed = kwargs.get('dual_headed', False)
        self.tilt_bonus = False  # over-ride in subclass as needed
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        self.buy_menu_hint_wagons_add_power = False
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        self.easter_egg_haulage_speed_bonus = kwargs.get('easter_egg_haulage_speed_bonus', False)
        # simple buy menu hint flag for driving cabs
        self.buy_menu_hint_driving_cab = False
        # random_reverse means (1) randomised reversing of sprites when vehicle is built (2) player can also flip vehicle
        # random_reverse is not supported in some templates
        self.random_reverse = kwargs.get('random_reverse', False)
        self.allow_flip = self.random_reverse # random_reverse vehicles can always be flipped, but flip can also be set in other cases (by subclass)
        # just a simple buy cost tweak, only use when needed
        self.electro_diesel_buy_cost_malus = None
        # arbitrary multiplier to the calculated buy cost, e.g. 1.1, 0.9 etc
        # set to 1 by default, over-ride in subclasses as needed
        self.buy_cost_adjustment_factor = 1
        # fixed (baseline) buy costs on this subtype, 10 points
        # leave this alone except for edge cases (e.g. driving van trailers which are implemented as engines, but need wagon costs)
        self.fixed_buy_cost_points = 10
        # arbitrary multiplier to the calculated run cost, e.g. 1.1, 0.9 etc
        # set to 1 by default, over-ride in subclasses as needed
        self.floating_run_cost_multiplier = 1
        # fixed (baseline) run costs on this subtype, 100 points
        self.fixed_run_cost_points = 30 # default, over-ride in subclass as needed
        # create structure to hold the units
        self.units = []
        # one default cargo for the whole consist, no mixed cargo shenanigans, it fails with auto-replace
        self.default_cargos = []
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        # create a structure for cargo /livery graphics options
        self.gestalt_graphics = GestaltGraphics()
        # option to provide automatic roof for all units in the consist, leave as None for no generation
        self.roof_type = None
        # role is e.g. Heavy Freight, Express etc, and is used to automatically set model life as well as in docs
        self.role = kwargs.get('role', None)
        # role child branch num places this vehicle on a specific child branch of the tech tree, where the role is the parent branch
        # 1..n for branches with calculated replacements, -1..-n for jokers which are not automatically replaced in the tree, 0 reserved
        self.role_child_branch_num = kwargs.get('role_child_branch_num', 0)
        # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get(
            'suppress_animated_pixel_warnings', False)
        # extended description (and a cite from a made up person) for docs etc
        self.description = """""" # to be set per vehicle, multi-line supported
        self._cite = "" # optional, set per subclass as needed
        # for 'inspired by' stuff
        self.foamer_facts = """""" # to be set per vehicle, multi-line supported
        # occasionally we want to force a specific spriterow for docs, not needed often, set in kwargs as needed, see also buy_menu_spriterow_num
        self.docs_image_spriterow = kwargs.get('docs_image_spriterow', 0) # 0 indexed spriterows, position in generated spritesheet
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

    @property
    def unique_spriterow_nums(self):
        # find the unique spriterow numbers, used in graphics generation
        result = []
        for unit in set([unit.spriterow_num for unit in self.units]):
            result.append(unit)
            # extend with alternative cc livery if present, spritesheet format assumes unit_1_default, unit_1_alternative_cc_livery, unit_2_default, unit_2_alternative_cc_livery if present
            if self.gestalt_graphics.alternative_cc_livery is not None:
                result.append(unit + 1)
        return result

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
        if self.str_name_suffix is not None:
            return "string(STR_NAME_CONSIST_PARENTHESES, string(STR_NAME_" + self.id + "), string(" + self.str_name_suffix + "))"
        else:
            return "string(STR_NAME_" + self.id + ")"

    def engine_varies_power_by_railtype(self, vehicle):
        if self.power_by_railtype is not None and vehicle.is_lead_unit_of_consist:
            # as of Dec 2018, can't use both variable power and wagon power
            # that could be changed if https://github.com/OpenTTD/OpenTTD/pull/7000 is done
            # would require quite a bit of refactoring though eh
            assert(self.wagons_add_power == False), "%s consist has both engine_varies_power_by_railtype and power_by_railtype, which conflict" % self.id
            return True
        else:
            return False

    def get_spriterows_for_consist_or_subpart(self, units):
        # pass either list of all units in consist, or a slice of the consist starting from front (arbitrary slices not useful)
        result = []
        for unit in units:
            unit_rows = []
            # assumes gestalt_graphics is used to handle all row types, no other cases at time of writing, could be changed eh?
            unit_rows.extend(
                self.gestalt_graphics.get_output_row_types())
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
            assert(self.intro_date_offset == None), "%s consist has both intro_date and intro_date_offset set, which is incorrect" % self.id
            return self._intro_date
        else:
            assert(self._gen != None), "%s consist has neither gen nor intro_date set, which is incorrect" % self.id
            result = self.roster.intro_dates[self.base_track_type][self.gen - 1]
            if self.intro_date_offset is not None:
                result = result + self.intro_date_offset
            return result

    @property
    def intro_date_days_offset(self):
        # days offset is used to control *synchronising* (or not) intro dates across groups of vehicles where needed
        # see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        # this does *not* use the role group mapping in global constants, as it's more fragmented to avoid too many new vehicle messages at once
        # JOKERS: note that not all jokers have to be in the jokers group here, they can be in other groups if intro dates need to sync
        role_to_role_groups_mapping = {'express_core': {'express': [1], 'heavy_express': [1]},
                                       'express_non_core': {'branch_express': [1, 2], 'express': [2], 'heavy_express': [2, 3, 4], 'luxury_pax_railcar': [-1]},
                                       'driving_cab': {'driving_cab_express': [-1]},
                                       'freight_core': {'freight': [1], 'heavy_freight':[1]},
                                       'freight_non_core': {'branch_freight': [1], 'freight': [2], 'heavy_freight': [2, 3, 4]},
                                       'hst': {'hst': [1, 2]},
                                       'jokers': {'gronk!': [-1, -2], 'express': [-1], 'heavy_express': [-1, -2, -3], 'freight': [-1, -2], 'branch_freight': [-1], 'heavy_freight': [-1, -2, -3, -4], 'snoughplough!': [-1]},
                                       'metro': {'mail_metro': [1], 'pax_metro': [1]},
                                       'railcar': {'mail_railcar': [1, 2, -1, -2], 'pax_railcar': [1, 2]},
                                       'very_high_speed': {'very_high_speed': [1, 2]},
                                       'universal': {'universal': [1]}}
        if self.gen == 1:
            # to ensure a fully playable roster is available for gen 1, force the days offset to 0
            # for explanation see https://www.tt-forums.net/viewtopic.php?f=26&t=68616&start=460#p1224299
            return 0
        elif self._intro_date_days_offset is not None:
            # offset defined in class (probably a wagon)
            return self._intro_date_days_offset
        else:
            result = None
            # assume role is defined (_probably_ fine)
            for group_key, group_role_list in role_to_role_groups_mapping.items():
                if self.role in group_role_list.keys():
                    if self.role_child_branch_num in group_role_list[self.role]:
                        result = global_constants.intro_date_offsets_by_role_group[group_key]
            # check we actually got a result
            assert(result != None), 'no role group found for role %s for consist %s' % (self.role,  self.id)
        return result

    @property
    def gen(self):
        # gen is usually set in the vehicle, but can be left unset if intro_date is set
        if self._gen:
            assert(self._intro_date == None), "%s consist has both gen and intro_date set, which is incorrect" % self.id
            return self._gen
        else:
            assert(self._intro_date != None), "%s consist has neither gen nor intro_date set, which is incorrect" % self.id
            for gen_counter, intro_date in enumerate(self.roster.intro_dates[self.base_track_type]):
                if self.intro_date < intro_date:
                    return gen_counter
            # if no result is found in list, it's last gen
            return len(self.roster.intro_dates[self.base_track_type])

    @property
    def equivalent_ids_alt_var_41(self):
        # only implemented in subclasses that require it - easiest thing when writing it, change if needed
        return None

    @property
    def engine_consists_for_caboose_cars(self):
        # caboose cars adjust livery depending on engine
        # this could be renamed for use with non-caboose types if ever needed
        result = []
        for consist in self.roster.engine_consists:
            if self.base_track_type == consist.base_track_type:
                result.append(consist)
        return result

    @property
    def replacement_consist(self):
        # option exists to force a replacement consist, this is used to merge tech tree branches
        if self.role_child_branch_num == 0:
            print('OOF', self.id, self.role_child_branch_num)

        if self._replacement_consist_id is not None:
            for consist in  self.roster.engine_consists:
                if consist.id == self._replacement_consist_id:
                    return consist
            # if we don't return a valid result, that's an error, probably a broken replacement id
            raise Exception('replacement consist id ' + self._replacement_consist_id +  ' not found for consist ' + self.id)
        else:
            similar_consists = []
            replacement_consist = None
            for consist in self.roster.engine_consists:
                if (consist.role == self.role) and (consist.role_child_branch_num == self.role_child_branch_num) and (consist.base_track_type == self.base_track_type):
                    similar_consists.append(consist)
            for consist in sorted(similar_consists, key=lambda consist: consist.intro_date):
                if consist.intro_date > self.intro_date:
                    replacement_consist = consist
                    break
            return replacement_consist

    @property
    def replaces_consists(self):
        # note that this depends on replacement_consist property in other consists, and may not work in all cases
        # a consist can replace more than one other consist
        result = []
        for consist in self.roster.engine_consists:
            if consist.replacement_consist is not None:
                if consist.replacement_consist.id == self.id:
                    result.append(consist)
        return result

    @property
    def similar_consists(self):
        # quite a crude guess at similar engines by role
        result = []
        for consist in self.roster.engine_consists:
            if (consist.base_track_type == self.base_track_type) and (consist.gen == self.gen) and (consist != self):
                if (consist.role == self.role) or (0 <= (consist.power - self.power) < 500) or (0 <= (self.power - consist.power) < 500):
                    result.append(consist)
        return result

    @property
    def model_life(self):
        if self.replacement_consist is None:
            return 'VEHICLE_NEVER_EXPIRES'
        else:
            return self.replacement_consist.intro_date - self.intro_date

    @property
    def retire_early(self):
        # affects when vehicle is removed from buy menu (in combination with model life)
        # to understand why this is needed see https://newgrf-specs.tt-wiki.net/wiki/NML:Vehicles#Engine_life_cycle
        # retire at end of model life + 10 (fudge factor - no need to be more precise than that)
        return -10

    @property
    def track_type(self):
        # are you sure you don't want base_track_type instead?
        # track_type handles converting base_track_type to ELRL, ELNG etc as needed for electric engines
        # it's often more convenient to use base_track_type prop, which treats ELRL and RAIL as same (for example)
        eltrack_type_mapping = {'RAIL': 'ELRL',
                                'NG': 'ELNG',
                                'METRO': 'METRO'} # assume METRO is always METRO, whether electric flag is set or not
        if self.requires_electric_rails:
            return eltrack_type_mapping[self.base_track_type]
        else:
            return self.base_track_type

    def get_speed_by_class(self, speed_class):
        # automatic speed, but can over-ride by passing in kwargs for consist
        speed_track_type_mapping = {'RAIL':'RAIL', 'ELRL':'RAIL', 'NG':'NG', 'ELNG':'NG', 'METRO':'METRO'}
        speeds_by_track_type = self.roster.speeds[speed_track_type_mapping[self.base_track_type]]
        return speeds_by_track_type[speed_class][self.gen - 1]

    @property
    def speed(self):
        if self._speed:
            return self._speed
        elif getattr(self, 'speed_class', None):
            # speed by class, if speed_class is set explicitly (and not None)
            # !! this doesn't handle RAIL / ELRL correctly
            # could be fixed by checking a list of railtypes
            return self.get_speed_by_class(self.speed_class)
        elif self.role:
            # first check for express roles, which are determined by multiple role groups
            for role_group_mapping_key in ['express', 'driving_cab', 'luxury_railcar']:
                group_roles = global_constants.role_group_mapping[role_group_mapping_key]
                if self.role in group_roles:
                    return self.get_speed_by_class('express')
            # then check other specific roles
            if self.role in ['mail_railcar', 'pax_railcar']:
                return self.get_speed_by_class('railcar')
            elif self.role in ['hst']:
                return self.get_speed_by_class('hst')
            elif self.role in ['very_high_speed']:
                return self.get_speed_by_class('very_high_speed')
            else:
                return self.get_speed_by_class('standard')
        else:
            # assume no speed limit
            return None

    @property
    def power_speed_ratio(self):
        # used in docs, as a way of comparing performance between vehicles, especially across generations in same branch of tech tree
        # see also: http://cs.trains.com/trn/f/111/t/188661.aspx
        # "on a 1% grade, MPH / 18.75 = HP (per ton); the HP requirement will increase roughly proportionally to the grade and speed."
        if self.power is None or self.speed is None:
            return None
        else:
            return int(self.power / self.speed)

    @property
    def weight(self):
        return sum([getattr(unit, 'weight', 0) for unit in self.units])

    @property
    def length(self):
        # total length of the consist
        return sum([unit.vehicle_length for unit in self.units])

    @property
    def roster(self):
        for roster in registered_rosters:
            if roster.id == self.roster_id:
                return roster
        else:
            raise Exception('no roster found for ', self.id)

    def get_expression_for_availability(self):
        result = []
        # rosters: the working definition is one and only one roster per vehicle
        result.append('param[1]==' + str(self.roster.numeric_id - 1))
        if self.joker:
             result.append('param_simplified_gameplay==0')
        return ' && '.join(result)

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
        if len(self.units) > 1:
            return 360  # custom buy menu sprite
        else:
            # default to just using 6th angle of vehicle
            return global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[6][0]

    @property
    def buy_menu_width(self):
        # max sensible width in buy menu is 64px
        if 4 * self.length < 64:
            return 4 * self.length
        else:
            return 64

    def get_buy_menu_format(self, vehicle):
        # keep the template logic simple, present strings for a switch/case tree
        # variable_power and wagons_add_power are mutually exclusive (asserted by engine_varies_power_by_railtype as of August 2019)
        if self.engine_varies_power_by_railtype(vehicle):
            return 'variable_power'
        elif self.buy_menu_hint_wagons_add_power:
            return 'wagons_add_power'
        elif self.buy_menu_hint_driving_cab:
            return 'driving_cab'
        else:
            return 'default'

    def get_buy_menu_string(self, vehicle):
        result = []
        # optional string if engine varies power by railtype
        if self.engine_varies_power_by_railtype(vehicle):
            result.append('STR_POWER_BY_RAILTYPE')
        # optional string if dedicated wagons add power
        if self.buy_menu_hint_wagons_add_power:
            result.append(self.buy_menu_distributed_power_substring)

        # engines will always show a role string
        result.append(self.buy_menu_role_string)

        # driving cab hint comes after role string
        if self.buy_menu_hint_driving_cab:
            result.append('STR_BUY_MENU_HINT_DRIVING_CAB')

        if len(result) == 1:
            return 'STR_BUY_MENU_WRAPPER_ONE_SUBSTR, string(' + result[0] + ')'
        if len(result) == 2:
            return 'STR_BUY_MENU_WRAPPER_TWO_SUBSTR, string(' + result[0] + '), string(' + result[1] + ')'
        # should never be reached, extend this if we do
        raise Exception('Unsupported number of buy menu strings for ', self.id)

    @property
    def buy_menu_role_string(self):
        for role_group, roles in global_constants.role_group_mapping.items():
            if self.role in roles:
                return 'STR_ROLE, string(' + global_constants.role_string_mapping[role_group] + ')'
        raise Exception('no role string found for ', self.id)

    @property
    def cite(self):
        # this assumes that NG and Metro always return the same, irrespective of consist cite
        # that makes sense for Pony roster, but might not work in other rosters, deal with that if it comes up eh?
        # don't like how much content (text) is in code here, but eh
        if self.base_track_type == 'NG':
            cite_name = "Roberto Flange"
            cite_titles = ["Narrow Gauge Superintendent", "Works Manager (Narrow Gauge)", "Traction Controller, Narrow Gauge Lines"]
        elif self.base_track_type == 'METRO':
            cite_name = "JJ Transit"
            cite_titles = ["Superintendent (Metro Division)", "Chief Engineer, Mass Mobility Systems"]
        else:
            if self._cite == "Arabella Unit":
                cite_name = self._cite
                cite_titles = ["General Manager (Railcars)", "Senior Engineer, Self-Propelled Traction", "Director, Suburban and Rural Lines"]
            elif self._cite == "Dr Constance Speed":
                cite_name = self._cite
                cite_titles = ["Lead Engineer, High Speed Projects", "Director, Future Traction Concepts", ]
            else:
                cite_name = "Mr Train"
                cite_titles = ["Acting Superintendent of Engines", "Provisional Chief Engineer", "Interim Head of Works", "Transitional General Manager (Traction)"]
        return cite_name + ', ' + random.choice(cite_titles)

    def render_articulated_switch(self, templates):
        if len(self.units) > 1:
            template = templates["articulated_parts.pynml"]
            nml_result = template(
                consist=self, global_constants=global_constants)
            return nml_result
        else:
            return ''

    def assert_speed(self):
        # speed is assumed to be limited to 200mph
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.speed is not None:
            if self.speed > 200:
                utils.echo_message("Consist " + self.id + " has speed > 200, which is too much")

    def assert_power(self):
        # power is assumed to be limited to 10,000hp
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.speed is not None:
            if self.power > 10000:
                utils.echo_message("Consist " + self.id + " has power > 10000hp, which is too much")

    def assert_weight(self):
        # weight is assumed to be limited to 500t
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.weight is not None:
            if self.weight > 500:
                utils.echo_message("Consist " + self.id + " has weight > 500t, which is too much")

    def assert_description_foamer_facts(self):
        # if these are too noisy, comment them out temporarily
        if self.power > 0:
            if len(self.description) == 0:
                utils.echo_message("Consist " + self.id + " has no description")
            if len(self.foamer_facts) == 0:
                utils.echo_message("Consist " + self.id + " has no foamer_facts")
            if '.' in self.foamer_facts:
                utils.echo_message("Consist " + self.id + " foamer_facts has a '.' in it.")


    def render(self, templates):
        self.assert_speed()
        self.assert_power()
        # templating
        nml_result = ''
        if len(self.units) > 1:
            nml_result = nml_result + self.render_articulated_switch(templates)
        for unit in self.unique_units:
            nml_result = nml_result + unit.render(templates)
        return nml_result


class EngineConsist(Consist):
    """
    Intermediate class for engine consists to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to engine consists.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # arbitrary multiplier to floating run costs (factors are speed, power, weight)
        # adjust per subtype as needed
        self.floating_run_cost_multiplier = 8.5
        # fixed (baseline) run costs on this subtype, or more rarely instances can over-ride this
        self.fixed_run_cost_points = kwargs.get('fixed_run_cost_points', 180)
        # Graphics configuration only as required
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        alternative_cc_livery = self.roster.livery_presets.get(kwargs.get('alternative_cc_livery', None), None)
        self.gestalt_graphics = GestaltGraphicsEngine(pantograph_type=self.pantograph_type,
                                                      alternative_cc_livery=alternative_cc_livery,
                                                      default_livery_extra_docs_examples = kwargs.get('default_livery_extra_docs_examples', []))

    @property
    def buy_cost(self):
        # max speed = 200mph by design - see assert_speed()
        # multiplier for speed, max value will be 25
        speed_cost_points = self.speed / 8
        # max power 10000hp by design - see assert_power()
        # malus for electric engines, ~33% higher equipment costs
        # !! this is an abuse of requires_electric_rails, but it's _probably_ fine :P
        if self.requires_electric_rails:
            power_factor = self.power / 800
        # malus for complex electro-diesels, ~33% higher equipment costs, based on elrl power
        # this sometimes causes a steep jump from non-electro-diesels in a tech tree (due to power jump), but eh, fine
        elif self.electro_diesel_buy_cost_malus is not None:
            power_factor = (self.electro_diesel_buy_cost_malus * self.power_by_railtype['ELRL']) / 750
        # multiplier for non-electric power, max value will be 10
        else:
            power_factor = self.power / 1000
        # basic cost from speed, power, subclass factor (e.g. engine with pax capacity might cost more to buy)
        buy_cost_points = speed_cost_points * power_factor * self.buy_cost_adjustment_factor
        # if I set cost base as high as I want for engines, wagon costs aren't fine grained enough
        # so just apply arbitrary multiplier to engine costs, which works
        buy_cost_points = 2 * buy_cost_points
        # start from an arbitrary baseline of 10 points, add points for gen, cost points, seems to work
        # cap to int for nml
        return int(self.fixed_buy_cost_points + self.gen + buy_cost_points)

    @property
    def running_cost(self):
        # algorithmic calculation of engine run costs
        # as of Feb 2019, it's fixed cost (set by subtype) + floating costs (derived from power, speed, weight)
        # note some string to handle NG trains, which tend to have a smaller range of speed, cost, power
        is_NG = True if self.base_track_type == 'NG' else False
        # max speed = 200mph by design - see assert_speed() - (NG assumes 100mph max)
        # multiplier for speed, max value will be 12.5
        speed_cost_factor = self.speed / (8 if is_NG else 16)
        # max power 10000hp by design - see assert_power() - (NG assumes 4000hp max)
        # multiplier for power, max value will be ~18
        power_factor = self.power / (250 if is_NG else 555)
        # max weight = 500t by design - see assert_weight() - (NG assumes 200t max)
        # multiplier for weight, max value will be 8
        weight_factor = self.weight / (32 if is_NG else 62.5)

        # !! this is an abuse of requires_electric_rails, but it's _probably_ fine :P
        if self.requires_electric_rails:
            if 'railcar' in self.role:
                # massive bonus to el railcars
                power_factor = 0.33 * power_factor
            else:
                # small bonus to electric engines
                # they already tend to be lighter per unit power (so cheaper to run) than similar power types
                power_factor = 0.75 * power_factor

        # basic cost from speed, power, weight
        floating_run_cost_points = speed_cost_factor * power_factor * weight_factor
        # then multiply by a factor specific to the subtype, so that we can control how much floating costs matter for this subtype
        # be aware that engines cost base is nerfed down, otherwise, wagon costs aren't fine grained enough
        # this means that floating_run_cost_multiplier might need to be > 3 to reset the base cost nerf
        floating_run_cost_points = floating_run_cost_points * self.floating_run_cost_multiplier
        fixed_run_cost_points = self.fixed_run_cost_points
        # add floating cost to the fixed (baseline) cost (which is arbitrary points, range 0-200-ish)
        # do an arbitrary calculation using gen to give the results I want (tried values in a spreadsheet until looked right)
        # the aim is to space costs widely across types within a generation, but only have slight increase (or flat) across generations of same type
        gen_multiplier = 8.52 - math.pow(1.22, self.gen)
        run_cost = gen_multiplier * (fixed_run_cost_points + floating_run_cost_points)
        # freight engines get a run cost bonus as they'll often be sat waiting for loads, so balance (also super realism!!)
        # doing this is preferable to doing variable run costs, which are weird and confusing (can't trust the costs showin in vehicle window)
        if self.role in ['heavy_freight']: # smaller bonus for heavy_freight
            run_cost = 0.9 * run_cost
        elif self.role in ['branch_freight', 'freight']: # bigger bonus for other freight
            run_cost = 0.8 * run_cost
        # massive bonus for NG
        if is_NG:
            run_cost = 0.33 * run_cost
        # cap to int for nml
        return int(run_cost)

    @property
    def joker(self):
        # jokers are bonus vehicles (mostly) engines which don't fit strict tech tree progression
        # for engines, jokers use -ve value for role_child_branch_num, tech tree vehicles use +ve
        return self.role_child_branch_num < 0


class AutoCoachCombineConsist(EngineConsist):
    """
    Consist for an articulated auto coach combine (mail + pax).  Implemented as Engine so it can lead a consist in-game.
    To keep implementation simple + crude, first unit should be dedicated mail type, second unit should be dedicated pax type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = 'driving_cab_express'
        self.role_child_branch_num = -1 # driving cab cars are probably jokers?
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = False # articulated innit (even needed?)
        # confer tiny power value to make this one an engine so it can lead.
        self.power = 10 # use 10 not 1, because 1 looks weird when added to engine HP
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0
        # ....buy costs adjusted to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_buy_cost_points = 6 # to reduce it from engine factor
        # ....run costs nerfed down to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_run_cost_points = 43
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_autocoach.pynml')


class MailEngineConsist(EngineConsist):
    """
    Consist of engines / units that has mail (and express freight) capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ['TOUR']
        self.default_cargos = polar_fox.constants.default_cargos['mail']
        # increased buy costs for having extra doors and stuff eh?
        self.buy_cost_adjustment_factor = 1.4
        # ...but reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 84


class MailEngineCabbageDVTConsist(MailEngineConsist):
    """
    Consist for a mail DVT / cabbage.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = 'driving_cab_express'
        self.role_child_branch_num = -1 # driving cab cars are probably jokers?
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = True
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        self.power = 300
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0.1
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1 # to reduce it from engine factor
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {'mail': {'default': 0, 'first': 0, 'last': 1, 'special': 0},
                                    'pax': {'default': 0, 'first': 0, 'last': 1, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='driving_cab_cars')


class MailEngineCargoSprinterEngineConsist(MailEngineConsist):
    """
    Consist for a cab motor unit for Cargo Sprinter express freight unit.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # non-standard cite
        self._cite = "Arabella Unit"
        """"
        # !! this type needs new graphics processing and/or template rules if it is to handle masking containers around the cabs
        # Graphics configuration
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # all position variants resolve to same spriterow
        spriterow_group_mappings = {'mail': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='railcars_3_unit_sets')
        """
        # Graphics configuration
        # NOTE that cargo sprinter will NOT randomise containers on load as of Dec 2020 - there is a bug with rear unit running unwanted triggers and re-randomising in depots etc
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_cargo_sprinter.pynml',
                                                      flag_switch_set_layers_register_more_sprites=True,
                                                      cargo_label_mapping=GestaltGraphicsIntermodal().cargo_label_mapping)

    @property
    def platform_type(self):
        # !! cargo sprinters all default currently, extend as needed
        return 'default'


class MailEngineMetroConsist(MailEngineConsist):
    """
    Consist for a mail metro train.  Just a sparse subclass to force the gestalt_graphics
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # this will knock standard age period down, so this train is only profitable over short routes
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_METRO_MALUS
        # buy costs increased above baseline, account for 2 units + underground nonsense
        self.buy_cost_adjustment_factor = 2
        # metro should only be effective over short distances
        # ....run cost multiplier is adjusted up from pax base for underground nonsense, also account for 2 units
        self.floating_run_cost_multiplier = 26
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # Graphics configuration
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 1, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="metro")


class MailEngineRailcarConsist(MailEngineConsist):
    """
    Consist for a mail railcar.  Just a sparse subclass to force the gestalt_graphics and allow_flip.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # by design, mail railcars don't change livery in a pax consist, but do have 2 liveries, matching mail cars for this generation
        # position variants
        # * unit with driving cabs both ends
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no driving cabs (OPTIONAL - only provided for 4-unit sets)
        # Rules are 2 unit sets of 3 unit sets (4 could also be supported, but isn't at time of writing)
        if kwargs.get('use_3_unit_sets', False):
            consist_ruleset = 'railcars_3_unit_sets'
            spriterow_group_mappings = {'mail': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        else:
            consist_ruleset = 'railcars_2_unit_sets'
            spriterow_group_mappings = {'mail': {'default': 0, 'first': 1, 'last': 2, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset=consist_ruleset,
                                                                     pantograph_type=self.pantograph_type)

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # this is intended for pax railcars, but mail railcars share templating in some cases, so stub in this result to prevent unwanted behaviour
        # mail railcars generally do not combine with anything other than their own ID, this is just a compatibility stub
        result = []
        result.append(self.base_numeric_id)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range (len(result), 16):
            result.append(-1)
        return result


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
         # increased buy costs for having seats and stuff eh?
        self.buy_cost_adjustment_factor = 1.8
        # ...but reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 84


class PassengerHSTCabEngineConsist(PassengerEngineConsist):
    """
    Consist for a dual-headed HST (high speed train).
    May or may not have capacity (set per vehicle).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # always dual-head
        self.dual_headed = True
        # moderate cargo age bonus
        self.cargo_age_period = 4 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.2
        # higher speed should only be effective over longer distances
        # ....run cost multiplier is adjusted up from pax base for high speed
        self.floating_run_cost_multiplier = 16
        # ...adjust fixed run costs on this subtype to look about right
        self.fixed_run_cost_points = 160
        # non-standard cite
        self._cite = "Dr Constance Speed"


class PassengerEngineLuxuryRailcarConsist(PassengerEngineConsist):
    """
    Consist for a luxury pax railcar (single unit, combinable).
    Intended for express-speed, high-power long-distance EMUs, use railcars for short / slow / commuter routes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # this won't make much difference except over *very* long routes, but set it anyway
        self.cargo_age_period = 8 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.3
        # to avoid these railcars being super-bargain cheap, add a cost malus compared to standard railcars (still less than standard engines)
        self.fixed_run_cost_points = 140
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="railcars_4_unit_sets",
                                                                     pantograph_type=self.pantograph_type)

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to luxury pax railcars and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of luxury_passenger_railcar_trailer_car trailers
        result = []
        # this will catch self also
        for consist in self.roster.engine_consists:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type) and (consist.role in ['luxury_pax_railcar']):
                result.append(consist.base_numeric_id)
        for consist in self.roster.wagon_consists['luxury_passenger_railcar_trailer_car']:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type):
                result.append(consist.base_numeric_id)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range (len(result), 16):
            result.append(-1)
        return result


class PassengerEngineMetroConsist(PassengerEngineConsist):
    """
    Consist for a pax metro train.  Just a sparse subclass to force the gestalt_graphics
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # this will knock standard age period down, so this train is only profitable over short routes
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_METRO_MALUS
        # buy costs increased above baseline, account for 2 units + underground nonsense
        self.buy_cost_adjustment_factor = 2
        # metro should only be effective over short distances
        # ....run cost multiplier is adjusted up from pax base for underground nonsense, also account for 2 units
        self.floating_run_cost_multiplier = 26
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # Graphics configuration
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 1, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="metro")


class PassengerEngineRailcarConsist(PassengerEngineConsist):
    """
    Consist for a pax railcar (single unit, combinable).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # this will knock standard age period down, so this train is less profitable over ~128 tiles than a similar luxury train
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_STANDARD_PAX_MALUS
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="railcars_3_unit_sets",
                                                                     pantograph_type=self.pantograph_type)

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to pax railcars and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of pax_railcar and pax railcar trailers
        result = []
        # assume diesel and electric railcars are combinable, this isn't a specific design intent, but stops annoying bugs when both are combined in one consist with trailers
        # this will create edge cases if diesel and electric MUs have different liveries set, can't have everything perfect eh?
        # this will catch self also
        for consist in self.roster.engine_consists:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type) and (consist.role in ['pax_railcar']):
                result.append(consist.base_numeric_id)
        for consist in self.roster.wagon_consists['passenger_railcar_trailer_car']:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type):
                result.append(consist.base_numeric_id)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range (len(result), 16):
            result.append(-1)
        return result


class PassengerVeryHighSpeedCabEngineConsist(PassengerEngineConsist):
    """
    Consist for a cab (leading) motor very high speed train (TGV etc).
    This has power by default and would usually be set as a dual-headed engine.
    Adding specific middle engines (with correct ID) will increase power for this engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # implemented as a list to allow multiple middle vehicles, e.g. double-deck, mail etc
        # but...theoretical as of Dec 2018 as nml power template doesn't support iterating over multiple middle vehicles
        self.middle_id = self.id.split('_cab')[0] + '_middle'
        self.buy_menu_hint_wagons_add_power = True
        self.tilt_bonus = True
        # moderate cargo age bonus
        self.cargo_age_period = 1.33 * global_constants.CARGO_AGE_PERIOD
        # note that buy costs are actually adjusted down from pax base, to account for distributed traction etc
        self.buy_cost_adjustment_factor = 0.95
        # high speed should only be effective over longer distances
        # ....run cost multiplier is adjusted up from pax base
        # but allow that every vehicle will have powered run costs, so not too high eh?
        self.floating_run_cost_multiplier = 17
        # ...and high fixed (baseline) run costs on this subtype
        self.fixed_run_cost_points = 200
        # train_flag_mu solely used for ottd livery (company colour) selection
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        # non-standard cite
        self._cite = "Dr Constance Speed"
        """
        # !! this type needs new graphics processing and/or template rules if it is to handle opening doors
        # !! box car variant expects symmetry
        # !! pax variant handles asymmetry differently to what is needed for the dual-head routine
        # !! pax variant graphics generation can be made to work (with clunky hax) but the template would need still new rulesets for that
        # !! writing a new processor and a template for doors probably isn't very hard (give all default vehicles option for opening doors?)
        # Graphics configuration
        # self.roof_type = 'pax_mail_smooth'
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # all position variants resolve to same spriterow
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 0, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="pax_cars",
                                                                     pantograph_type=self.pantograph_type)
        """

    @property
    def buy_menu_distributed_power_substring(self):
        return 'STR_WAGONS_ADD_POWER_CAB'

    @property
    def buy_menu_distributed_power_name_substring(self):
        return self.middle_id

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.power


class PassengerVeryHighSpeedMiddleEngineConsist(PassengerEngineConsist):
    """
    Consist for an intermediate motor unit for very high speed train (TGV etc).
    When added to the correct cab engine, this vehicle will cause cab power to increase.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cab_id = self.id.split('_middle')[0] + '_cab'
        self.wagons_add_power = True
        self.buy_menu_hint_wagons_add_power = True
        self.tilt_bonus = True
        # moderate cargo age bonus
        self.cargo_age_period = 1.33 * global_constants.CARGO_AGE_PERIOD
        # train_flag_mu solely used for ottd livery (company colour) selection
        # eh as of Feb 2019, OpenTTD won't actually use this for middle cars, as not engines
        # this means the buy menu won't match, but wagons will match anyway when attached to cab
        # prop left in place in case that ever gets changed :P
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        self.roof_type = 'pax_mail_smooth'
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * default unit
        # * unit with pantograph - leading end
        # * unit with pantograph -  rear end
        # * restaurant unit
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="pax_cars",
                                                                     pantograph_type=self.pantograph_type)

    @property
    def cab_consist(self):
        # fetch the consist for the cab engine
        for engine_consist in self.roster.engine_consists:
            if engine_consist.id == self.cab_id:
                return engine_consist

    @property
    def cab_power(self):
        # match middle engine power to cab engine power
        return self.cab_consist.power

    @property
    def buy_cost(self):
        # match middle engine buy cost to cab engine buy cost
        # engine and wagon base costs are set differently, attempt to compensate for that
        # !! this does not account for wagon costs currently, just engine
        # 6.25 is a magic number, 2 is to double the factor for each base cost adjustment step
        adjustment_factor = 6.25 * 2 * abs(global_constants.PR_BUILD_VEHICLE_TRAIN)
        return int(self.cab_consist.buy_cost * adjustment_factor)

    @property
    def running_cost(self):
        # match middle engine running cost to cab engine running cost
        return self.cab_consist.running_cost

    @property
    def buy_menu_distributed_power_substring(self):
        return 'STR_WAGONS_ADD_POWER_MIDDLE'

    @property
    def buy_menu_distributed_power_name_substring(self):
        return self.cab_id

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.cab_consist.power


class SnowploughEngineConsist(EngineConsist):
    """
    Consist for a snowplough.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = 'snoughplough!' # blame Pikka eh?
        self.role_child_branch_num = -1
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = True
        # nerf power and TE down to minimal values, these confer a tiny performance boost to the train, 'operational efficiency' :P
        self.power = 100
        self.tractive_effort_coefficient = 0.1
        # give it mail / express capacity so it has some purpose :P
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ['TOUR']
        self.default_cargos = polar_fox.constants.default_cargos['mail']
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1 # to reduce it from engine factor
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_snowplough.pynml')


class CarConsist(Consist):
    """
    Intermediate class for car (wagon) consists to subclass from, provides sparse properties, most are declared in subclasses.
    """

    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs['id'] = id
        super().__init__(**kwargs)
        self.roster.register_wagon_consist(self)

        self._joker = False # over-ride this in sub-class as needed
        self.speed_class = 'standard'  # over-ride this in sub-class for, e.g. express freight consists
        self.subtype = kwargs['subtype']
        # Weight factor: over-ride in sub-class as needed
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type == 'NG' else 1
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        # used to synchronise / desynchronise groups of vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        # default all to car consists to 'universal' offset, over-ride in subclasses as needed
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['universal']
        # assume all wagons randomly swap CC, revert to False in wagon subclasses as needed
        self.use_colour_randomisation_strategies = True
        # set to 2 in subclass if 2cc should be randomised - can't randomise both, too fiddly
        self.cc_num_to_randomise = 1
        # over-ride in subclasses to select specific randomisation strategy for vehicle type
        self.auto_colour_randomisation_strategy_num = 0 # 0 is default
        # over-ride in subclasses to suppress base colour parameter (and always use company colours)
        self.use_wagon_base_colour_parameter = True

    @property
    def buy_cost(self):
        if self.speed is not None:
            speed_cost_points = self.speed
        else:
            # assume unlimited speed costs about same as 160mph
            speed_cost_points = 160
        length_cost_factor = self.length / 8
        # Horse allows some variation in wagon buy costs, reflecting equipment etc
        buy_cost_points = speed_cost_points * length_cost_factor * self.buy_cost_adjustment_factor
        # multiply it all by 1.66, seems to work about right
        buy_cost_points = 1.66 * buy_cost_points
        # int for nml
        return int(buy_cost_points)

    @property
    def running_cost(self):
        if self.speed is not None:
            speed_cost_points = self.speed
        else:
            # assume unlimited speed costs about same as 160mph
            speed_cost_points = 160
        # start from an arbitrary baseline and add speed cost
        run_cost_points = 100 + speed_cost_points
        # multiply by length, so the 8/8 cost is always twice 4/8 etc
        # (length is also an adequate proxy for capacity)
        length_cost_factor = self.length / 8
        run_cost_points = run_cost_points * length_cost_factor
        # multiply up by arbitrary amount, to where I want wagon run costs to be
        # (base cost is set deliberately low to allow small increments for fine-grained control)
        run_cost_points = 1.2 * run_cost_points * self.floating_run_cost_multiplier
        # narrow gauge gets a massive bonus - NG wagons are lower cap, so earn relatively much less / length
        if self.base_track_type == 'NG':
            run_cost_points = 0.2 * run_cost_points
        # arbitrary factor for minor cost inflation by generation (above and beyond speed and length increases)
        # small balance against later game trains that are more profitable due increased average network speed resulting in faster transit times (clearing junctions etc faster)
        run_cost_points = math.pow(1.1, self.gen) * run_cost_points
        # cap to int for nml
        return int(run_cost_points)

    @property
    def model_life(self):
        # automatically span wagon model life across gap to next generation
        # FYI next generation might be +n, not +1
        # this has to handle the cases of
        # - subtype that is the end of the tree for that type and should always be available
        # - subtype that ends but *should* be replaced by another subtype that continues the tree
        # - subtype where there is a generation gap in the tree, but the subtype continues across the gap

        tree_permissive = []
        tree_strict = []
        for wagon in self.roster.wagon_consists[self.base_id]:
            if wagon.base_track_type == self.base_track_type:
                tree_permissive.append(wagon.gen)
                if wagon.subtype == self.subtype:
                    tree_strict.append(wagon.gen)

        tree_permissive = sorted(set(tree_permissive))
        tree_strict = sorted(set(tree_strict))

        if tree_permissive.index(self.gen) == len(tree_permissive) - 1:
            # this is the last generation of this type, on this track type, so keep it around
            # note that there may also be other subtypes in this generation, but they'll all be the last of the type
            return 'VEHICLE_NEVER_EXPIRES'

        if tree_strict.index(self.gen) != len(tree_strict) - 1:
            # this is not the last of this subtype, so span strictly over to the next of this subtype
            next_gen = tree_strict[tree_strict.index(self.gen) + 1]
        else:
            # this is the last of this subtype, but there are other later generations of other subtypes
            next_gen = tree_permissive[tree_permissive.index(self.gen) + 1]
        next_gen_intro_date = self.roster.intro_dates[self.base_track_type][next_gen-1]
        return next_gen_intro_date - self.intro_date


    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get('base_track_type', None) == 'NG':
            id_base = id_base + '_ng'
        result = '_'.join((id_base, kwargs['roster_id'], 'gen', str(
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
        elif self.subtype == 'D':
            subtype_str = 'STR_NAME_SUFFIX_TWIN'
        return subtype_str

    @property
    def name(self):
        if self.subtype == 'U':
            # subtype U is a hack to indicate there is only one subtype for this wagon, so no suffix needed
            return "string(STR_NAME_CONSIST_PLAIN, string(" + self.get_wagon_title_class_str() + "))"
        else:
            return "string(STR_NAME_CONSIST_PARENTHESES, string(" + self.get_wagon_title_class_str() + "), string(" + self.get_wagon_title_subtype_str() + "))"

    @property
    def joker(self):
        # jokers are bonus vehicles (mostly) engines which don't fit strict tech tree progression
        # for cars, jokers are mid-length 'B' vehicles and/or rules from the sub-class
        if self.subtype == 'B' or self._joker == True:
            return True
        else:
            return False


class AlignmentCarConsist(CarConsist):
    """
    For checking sprite alignment
    """

    def __init__(self, **kwargs):
        self.base_id = 'alignment_car'
        super().__init__(**kwargs)
        self.speed_class = None  # no speed limit
        # refit nothing
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.buy_cost_adjustment_factor = 0 # free
        # no random CC, no flip
        self.use_colour_randomisation_strategies = False
        self.allow_flip = False


class BolsterCarConsist(CarConsist):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    def __init__(self, **kwargs):
        self.base_id = 'bolster_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # none needed
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['long_products']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['long_products']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='long_products')


class BoxCarConsist(CarConsist):
    """
    Box car, van - express, piece goods cargos, other selected cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'box_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['box']
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='box_car',
                                                                  recolour_maps=graphics_constants.box_livery_recolour_maps)


class BulkheadFlatCarConsist(CarConsist):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    def __init__(self, **kwargs):
        self.base_id = 'bulkhead_flat_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['plate']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='flat')


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
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.buy_cost_adjustment_factor = 0.75 # chop down caboose costs, they're just eye candy eh
        # liveries swap CC on user-flip, so no swapping CC randomly
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(num_generations=len(self.roster.intro_dates[self.base_track_type]),
                                                       recolour_maps=graphics_constants.caboose_livery_recolour_maps)


class CarbonBlackHopperCarConsist(CarConsist):
    """
    Dedicated covered hopper car for carbon black.  No other cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'carbon_black_hopper_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ['CBLK']
        self.label_refits_disallowed = []
        self.default_cargos = []
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.carbon_black_hopper_car_livery_recolour_maps)


class CoilBuggyCarConsist(CarConsist):
    """
    Dedicated (steel mill) buggy car for coils. Not a standard railcar. No other refits.
    """
    # note does NOT subclass CoilCarConsistBase - different type of consist
    def __init__(self, **kwargs):
        self.base_id = 'coil_buggy_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # none needed
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['cold_metal']
        self.label_refits_disallowed = [] # none needed
        self.default_cargos = polar_fox.constants.default_cargos['metal']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2 # double the default weight
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        self._joker = True
        # CC is swapped randomly (player can't choose), player can't flip as vehicle is articulated
        self.allow_flip = False
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_with_visible_cargo.pynml',
                                                      cargo_row_map={}, # leave blank, all default to same
                                                      generic_rows=[0],
                                                      unique_spritesets=[['empty', 'flipped', 10], ['loading_0', 'flipped', 40], ['loaded_0', 'flipped', 40],
                                                                         ['empty', 'unflipped', 10], ['loading_0', 'unflipped', 40], ['loaded_0', 'unflipped', 40]])


class CoilCarConsistBase(CarConsist):
    """
    Coil car - for finished metals (steel, copper etc).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['cold_metal']
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['metal']
        self.buy_cost_adjustment_factor = 1.1
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True


class CoilCarCoveredConsist(CoilCarConsistBase):
    """
    Covered coil car.  No visible cargo.
    """
    def __init__(self, **kwargs):
        self.base_id = 'coil_car_covered'
        super().__init__(**kwargs)
        self.cc_num_to_randomise = 2
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(body_recolour_map=graphics_constants.body_recolour_CC2,
                                                            piece='coil',
                                                            has_cover=True)


class CoilCarUncoveredConsist(CoilCarConsistBase):
    """
    Uncovered coil car.  Visible cargo.
    """
    def __init__(self, **kwargs):
        self.base_id = 'coil_car_uncovered'
        super().__init__(**kwargs)
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='coil')


class CoveredHopperCarConsistBase(CarConsist):
    """
    Bulk cargos needing covered protection.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['covered_hoppers']
        self.label_refits_disallowed = []
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True


class CoveredHopperCarConsist(CoveredHopperCarConsistBase):
    """
    Defaults to salt/potash type cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'covered_hopper_car'
        super().__init__(**kwargs)
        self.default_cargos = ['SALT', 'SAND', 'POTA'] # !! needs updated
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.covered_hopper_car_livery_recolour_maps)


class CoveredHopperCarGrainConsist(CoveredHopperCarConsistBase):
    """
    Defaults to grain/farm type cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'grain_hopper_car'
        super().__init__(**kwargs)
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['covered_hoppers']
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.grain_hopper_car_livery_recolour_maps)


class CoveredHopperCarPelletConsist(CoveredHopperCarConsistBase):
    """
    Defaults to grain/farm type cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'pellet_hopper_car'
        super().__init__(**kwargs)
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['covered_hoppers']
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.pellet_hopper_car_livery_recolour_maps)


class CryoTankCarConsist(CarConsist):
    """
    Specialist tank cars for gases, e.g. Oxygen, Chlorine etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = 'cryo_tank_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['cryo_gases']
        self.default_cargos = polar_fox.constants.default_cargos['cryo_gases']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=polar_fox.constants.cryo_tanker_livery_recolour_maps)


class CurtainSideCarBoxConsist(CarConsist):
    """
    Curtain side box car - same refits as box car.
    *Not* tarpaulin car which is curtain roof flat.
    """

    def __init__(self, **kwargs):
        self.base_id = 'curtain_side_box_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['box']
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='curtain_side_box_car',
                                                                  recolour_maps=graphics_constants.curtain_side_livery_recolour_maps)


class DumpCarConsistBase(CarConsist):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos, same set as hopper cars.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['dump_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_dump_bulk']
        self.default_cargos = polar_fox.constants.default_cargos['dump']
        self.loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class DumpCarConsist(DumpCarConsistBase):
    """
    Standard (Low Side) Dump Car.
    """

    def __init__(self, **kwargs):
        self.base_id = 'dump_car'
        super().__init__(**kwargs)


class DumpCarHighSideConsist(DumpCarConsistBase):
    """
    High Side Dump Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = 'dump_car_high_side'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['dump_high_sides']
        self._joker = True
        self.cc_num_to_randomise = 2


class DumpCarScrapMetalConsist(DumpCarConsistBase):
    """
    Scrap Metal Car
    Same as standard dump car, but different appearance and default cargos.
    The classname breaks convention (would usually be ScrapMetalCar), this is to keep all dump car subclasses togther).
    """

    def __init__(self, **kwargs):
        self.base_id = 'scrap_metal_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['dump_scrap']


class DumpCarScrapMetalHighSideConsist(DumpCarConsistBase):
    """
    High Side Scrap Metal Car
    Same as standard dump car, but different appearance and default cargos.
    The classname breaks convention (would usually be ScrapMetalCar), this is to keep all dump car subclasses togther).
    """

    def __init__(self, **kwargs):
        self.base_id = 'scrap_metal_car_high_side'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['dump_scrap']


class EdiblesTankCarConsist(CarConsist):
    """
    Wine, milk, water etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = 'edibles_tank_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = [] # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['edible_liquids']
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['edibles_tank']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['food_wagons']
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = 1 # single base colour unless flipped
        # Graphics configuration
        # only one livery, but recolour gestalt used to automate adding chassis
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.edibles_tank_car_livery_recolour_maps)


class ExpressCarConsist(CarConsist):
    """
    Express cars - express freight, valuables, mails.
    """

    def __init__(self, **kwargs):
        self.base_id = 'express_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['express']
        # adjust weight factor because express car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self.floating_run_cost_multiplier = 1.66
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['express_core']
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = 1 # single base colour unless flipped
        self.use_wagon_base_colour_parameter = False
        # Graphics configuration
        if self.gen in [1]:
            self.roof_type = 'pax_mail_clerestory'
        elif self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='express_car',
                                                                  recolour_maps=graphics_constants.box_livery_recolour_maps)


class ExpressIntermodalCarConsist(CarConsist):
    """
    Express intermodal container cars - express freight, valuables, mails.
    """
    def __init__(self, **kwargs):
        self.base_id = 'express_intermodal_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['express']
        # adjust weight factor because express intermodal car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self.floating_run_cost_multiplier = 1.66 # more than box car, less than mail car
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['express_core']
        self._joker = True
        # intermodal containers can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        # player can still flip to the second livery
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        # !! note to future, if e.g. NA Horse needs longer express intermodal sets, set the consist_ruleset conditionally by checking roster
        self.gestalt_graphics = GestaltGraphicsIntermodal(consist_ruleset='2_unit_sets')

    @property
    # account for variable floor heights, well cars, etc
    def platform_type(self):
        # !! express intermodal all default currently, extend as needed
        return 'default'


class FlatCarConsist(CarConsist):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """

    def __init__(self, **kwargs):
        self.base_id = 'flat_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['flat']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='flat')


class FruitVegCarConsist(CarConsist):
    """
    Fruit and vegetables, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'fruit_veg_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['fruit_veg']
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['fruit_veg']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='box_car',
                                                                  recolour_maps=graphics_constants.fruit_veg_livery_recolour_maps)


class HopperCarConsistBase(CarConsist):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['dump_freight']
        self.label_refits_allowed = []  # none needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_dump_bulk']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class HopperCarConsist(HopperCarConsistBase):
    """
    Defaults to coal.  Doesn't need a cargo-indicative name.
    """

    def __init__(self, **kwargs):
        self.base_id = 'hopper_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['hopper']


class HopperCarOreConsist(HopperCarConsistBase):
    """
    Defaults to iron ore.
    The classname breaks convention (would usually be OreHopper), this is to keep all hopper subclasses togther).
    """

    def __init__(self, **kwargs):
        self.base_id = 'ore_hopper_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['ore_hopper'] # !! needs updated


class HopperCarRockConsist(HopperCarConsistBase):
    """
    Defaults to rock/stone-type cargos.
    The classname breaks convention (would usually be OreHopper), this is to keep all hopper subclasses togther).
    """

    def __init__(self, **kwargs):
        self.base_id = 'rock_hopper_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['rock_hopper']
        self._joker = True


class IngotCarConsist(CarConsist):
    """
    Dedicated car for steel / iron ingots. A steel mill ingot buggy, not a standard railcar. No other refits.
    """

    def __init__(self, **kwargs):
        self.base_id = 'ingot_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # none needed
        self.label_refits_allowed = ['IRON', 'CSTI', 'STCB']
        self.label_refits_disallowed = [] # none needed
        self.default_cargos = ['IRON']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2 # double the default weight
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        self._joker = True
        # CC is swapped randomly (player can't choose), player can't flip as vehicle is articulated
        self.allow_flip = False
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_with_visible_cargo.pynml',
                                                      cargo_row_map={}, # leave blank, all default to same
                                                      generic_rows=[0],
                                                      unique_spritesets=[['empty', 'flipped', 10], ['loading_0', 'flipped', 40], ['loaded_0', 'flipped', 70],
                                                                         ['empty', 'unflipped', 10], ['loading_0', 'unflipped', 40], ['loaded_0', 'unflipped', 70]])


class IntermodalCarConsistBase(CarConsist):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['box']
        self.loading_speed_multiplier = 2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # intermodal containers can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        # player can still flip to the second livery
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        # various rulesets are supported, per consist, (or could be extended to checks per roster)
        if kwargs.get('consist_ruleset', None) is not None:
            consist_ruleset = kwargs.get('consist_ruleset')
        else:
            consist_ruleset = '4_unit_sets'
        self.gestalt_graphics = GestaltGraphicsIntermodal(consist_ruleset=consist_ruleset)


class IntermodalCarConsist(IntermodalCarConsistBase):
    """
    Default intermodal car - simple flat platform at default height.
    """

    def __init__(self, **kwargs):
        self.base_id = 'intermodal_car'
        super().__init__(**kwargs)

    @property
    def platform_type(self):
        # the 'default' for NG is the same as for low_floor so just re-use that for now
        if self.track_type == 'NG':
            return 'low_floor'
        else:
            return 'default'


class IntermodalLowFloorCarConsist(IntermodalCarConsistBase):
    """
    Low floor intermodal car - simple flat platform at height -1
    """

    def __init__(self, **kwargs):
        self.base_id = 'low_floor_intermodal_car'
        super().__init__(**kwargs)
        self.platform_type = 'low_floor' # note that NG does not support low_floor, it already is low_floor


class LivestockCarConsist(CarConsist):
    """
    Livestock, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'livestock_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # no classes, use explicit labels
        self.label_refits_allowed = ['LVST']
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = ['LVST']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        self.cc_num_to_randomise = 2
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='livestock_car',
                                                                  recolour_maps=graphics_constants.livestock_livery_recolour_maps)


class LogCarConsist(CarConsist):
    """
    Specialist transporter for logs
    """

    def __init__(self, **kwargs):
        self.base_id = 'log_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # no classes, use explicit labels
        # limited refits by design eh
        self.label_refits_allowed = ['WOOD']
        self.label_refits_disallowed = []
        self.default_cargos = ['WOOD']
        self.loading_speed_multiplier = 2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        self.cc_num_to_randomise = 2
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='tree_length_logs')


class MailCarConsist(CarConsist):
    """
    Mail cars - also handle express freight, valuables.
    """

    def __init__(self, **kwargs):
        self.base_id = 'mail_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['mail']
        # adjust weight factor because mail car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self.floating_run_cost_multiplier = 3
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['express_core']
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        if self.gen in [1]:
            self.roof_type = 'pax_mail_clerestory'
        elif self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # mail cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # * solid block can be used, but looks like freight cars, so duotone liveries are preferred (see caboose cars for inspiration)
        # position based variants
        # longer mail cars get an additional sprite option in the consist ruleset; shorter mail cars don't as it's TMWFTLB
        # * windows or similar variation for first, last vehicles (maybe also every nth vehicle?)
        brake_car_sprites = 1 if self.subtype in ['B', 'C'] else 0
        bonus_sprites = 2 if self.subtype in ['C'] else 0
        spriterow_group_mappings = {'mail': {'default': 0, 'first': brake_car_sprites, 'last': brake_car_sprites, 'special': bonus_sprites},
                                    'pax': {'default': 0, 'first': 0, 'last': 0, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='mail_cars')


class OpenCarConsist(CarConsist):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        self.base_id = 'open_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['open']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True,
                                                            piece='open')


class PassengerCarConsistBase(CarConsist):
    """
    Common base class for passenger cars.
    """
    # very specific flag used by graphics chain to detect other pax cars (could have used prop 25 userbits, but eh, screw that :)
    report_as_pax_car_to_neighbouring_vehicle_in_rulesets = True

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['pax']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['express_core']
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # roof configuration
        if self.gen in [1]:
            self.roof_type = 'pax_mail_clerestory'
        elif self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'


class PassengerCarConsist(PassengerCarConsistBase):
    """
    Standard pax car.
    Position-dependent sprites for brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'passenger_car'
        super().__init__(**kwargs)
        # this will knock standard age period down, so this train is less profitable over ~128 tiles than a similar luxuryy train
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_STANDARD_PAX_MALUS
        self.buy_cost_adjustment_factor = 1.3
        self.floating_run_cost_multiplier = 4
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type == 'NG' else 1.5
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special (restaurant) coaches from PassengerCarConsistBase Dec 2018, overkill
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='pax_cars')


class PassengerHSTCarConsist(PassengerCarConsistBase):
    """
    Trailer dedicated for HST-type trains (no wagon attach, but matching stats and livery).
    Moderately improved decay rate compared to standard pax car.
    Position-dependent sprites for restaurant car, brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'hst_passenger_car'
        super().__init__(**kwargs)
        self.speed_class = 'hst'
        # used to get insert the name of the parent into vehicle name
        self.cab_id = kwargs['cab_id'] # cab_id must be passed, do not mask errors with .get()
        # this won't make much difference except over *very* long routes, but set it anyway
        # moderate cargo age bonus
        self.cargo_age_period = 4 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.66
        self.floating_run_cost_multiplier = 4.75
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['hst']
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type == 'NG' else 1.6
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (restaurant) coach
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='pax_cars')

    @property
    def name(self):
        # special name handling to use the cab name
        # !! this doesn't work in the docs,
        # !! really for this kind of stuff, there needs to be a python tree/list of strings, then render to nml, html etc later
        # !! buy menu text kinda does that, but would need to convert all names to do this
        return "string(STR_NAME_CONSIST_COMPOUND, string(STR_NAME_" + self.cab_id + "), string(STR_NAME_SUFFIX_HST_PASSENGER_CAR))"


class PassengerLuxuryCarConsist(PassengerCarConsistBase):
    """
    Improved decay rate and lower capacity per unit length compared to standard pax car.
    Position-dependent sprites for restaurant car, brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'luxury_passenger_car'
        super().__init__(**kwargs)
        # this won't make much difference except over *very* long routes, but set it anyway
        self.cargo_age_period = 8 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.6
        self.floating_run_cost_multiplier = 5
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type == 'NG' else 2
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (restaurant) coach
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset='pax_cars')


class PassengerRailcarTrailerCarConsist(PassengerCarConsistBase):
    """
    Unpowered passenger trailer car for railcars.
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'passenger_railcar_trailer_car'
        super().__init__(**kwargs)
          # PassengerCarConsistBase sets 'express', but railcar trailers should over-ride this back to 'standard'
        self.speed_class = 'railcar'
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # this will knock standard age period down, so this train is less profitable over ~128 tiles than a similar luxuryy train
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_STANDARD_PAX_MALUS
        self.buy_cost_adjustment_factor = 1.3
        self.floating_run_cost_multiplier = 4.75
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['railcar']
        self._joker = True
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type == 'NG' else 1.5
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # 2 liveries, should match liveries of railcars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="railcars_3_unit_sets",
                                                                     pantograph_type=self.pantograph_type)

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to pax railcar trailers and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of pax_railcar and pax railcar trailers
        result = []
        result.append(self.base_numeric_id)
        for consist in self.roster.engine_consists:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type) and (consist.role in ['pax_railcar']):
                result.append(consist.base_numeric_id)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range (len(result), 16):
            result.append(-1)
        return result


class PassengerLuxuryRailcarTrailerCarConsist(PassengerCarConsistBase):
    """
    Unpowered passenger trailer car for luxury railcars.
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'luxury_passenger_railcar_trailer_car'
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # this won't make much difference except over *very* long routes, but set it anyway
        self.cargo_age_period = 8 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.3
        self.floating_run_cost_multiplier = 5
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['express_non_core']
        self._joker = True
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type == 'NG' else 1.5
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings,
                                                                     consist_ruleset="railcars_4_unit_sets",
                                                                     pantograph_type=self.pantograph_type)

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to pax railcar trailers and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of pax_railcar and pax railcar trailers
        result = []
        result.append(self.base_numeric_id)
        for consist in self.roster.engine_consists:
            if (consist.gen == self.gen) and (consist.base_track_type == self.base_track_type) and (consist.role in ['luxury_pax_railcar']):
                result.append(consist.base_numeric_id)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range (len(result), 16):
            result.append(-1)
        return result


class PlateCarConsist(CarConsist):
    """
    Low-side wagon - variant on flat wagon, refits same
    """

    def __init__(self, **kwargs):
        self.base_id = 'plate_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['plate']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='flat')


class ReeferCarConsist(CarConsist):
    """
    Refrigerated cargos, with improved decay rate
    """

    def __init__(self, **kwargs):
        self.base_id = 'reefer_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['reefer']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.66
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['food_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = 1 # single base colour unless flipped
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='box_car',
                                                                  recolour_maps=graphics_constants.refrigerated_livery_recolour_maps)


class SiloCarConsistBase(CarConsist):
    """
    Powder bulk cargos needing protection and special equipment for unloading.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ['SUGR', 'FMSP', 'RFPR', 'BDMT', 'QLME', 'SASH', 'CMNT', 'CBLK', 'SAND'] # move to Polar Fox (maybe??)
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos['silo']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True


class SiloCarConsist(SiloCarConsistBase):
    """
    Standard silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = 'silo_car'
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.silo_livery_recolour_maps)


class SiloCarCementConsist(SiloCarConsistBase):
    """
    Cement-coloured silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = 'cement_silo_car'
        super().__init__(**kwargs)
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.cement_silo_livery_recolour_maps)


class SlagLadleCarConsist(CarConsist):
    """
    Dedicated car for iron / steel slag.  No other refits.
    """

    def __init__(self, **kwargs):
        self.base_id = 'slag_ladle_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # none needed
        self.label_refits_allowed = ['SLAG']
        self.label_refits_disallowed = [] # none needed
        self.default_cargos = ['SLAG']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2 # double the default weight
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        self._joker = True
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_with_visible_cargo.pynml',
                                                      cargo_row_map={'SLAG': [0]},
                                                      generic_rows=[0],
                                                      unique_spritesets=[['empty', 'flipped', 10], ['loading_0', 'flipped', 40], ['loaded_0', 'flipped', 70],
                                                                         ['empty', 'unflipped', 10], ['loading_0', 'unflipped', 40], ['loaded_0', 'unflipped', 70]])

class SlidingRoofCarConsist(CarConsist):
    """
    Sliding roof van - sfins2 holdall and similar - same refits as flat, not van (experimental)
    """

    def __init__(self, **kwargs):
        self.base_id = 'sliding_roof_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['flat']
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(body_recolour_map=graphics_constants.sliding_roof_car_body_recolour_map,
                                                            piece='flat',
                                                            has_cover=True)


class SlidingWallCarConsist(CarConsist):
    """
    Sliding wall van - (cargowagon, habfiss, thrall, pullman all-door car etc) - same refits as box car.
    """

    def __init__(self, **kwargs):
        self.base_id = 'sliding_wall_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['box']
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = 1 # single base colour unless flipped
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='sliding_wall_car',
                                                                  recolour_maps=graphics_constants.sliding_wall_livery_recolour_maps)


class TankCarConsistBase(CarConsist):
    """
    All non-edible liquid cargos
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they may also change livery at stations if refitted between certain cargo types <shrug>
        super().__init__(**kwargs)
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_generic_liquids']
        self.loading_speed_multiplier = 3
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        # allow flipping, used to flip company colour
        self.allow_flip = True


class TankCarConsist(TankCarConsistBase):
    """
    Standard tank car
    """

    def __init__(self, **kwargs):
        self.base_id = 'tank_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['tank']
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=polar_fox.constants.tanker_livery_recolour_maps)


class TankCarProductConsist(TankCarConsistBase):
    """
    Shinier version of the standard tank car, same refits, different defaults
    """

    def __init__(self, **kwargs):
        self.base_id = 'product_tank_car'
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos['product_tank']
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(recolour_maps=graphics_constants.product_tank_car_livery_recolour_maps)


class TarpaulinCarConsist(CarConsist):
    """
    Tarpaulin car - a graphical alternative to flat car, with identical refits
    """

    def __init__(self, **kwargs):
        self.base_id = 'tarpaulin_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['flatbed_freight']
        self.label_refits_allowed = ['GOOD']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_flatbed_freight']
        self.default_cargos = polar_fox.constants.default_cargos['flat']
        self.buy_cost_adjustment_factor = 1.1
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(body_recolour_map=graphics_constants.tarpaulin_car_body_recolour_map,
                                                            piece='flat',
                                                            has_cover=True)


class TorpedoCarConsist(CarConsist):
    """
    Specialist wagon for hauling molten pig iron.
    May or may not extend to other metal cargos (probably not).
    """

    def __init__(self, **kwargs):
        self.base_id = 'torpedo_car'
        super().__init__(**kwargs)
        self.class_refit_groups = [] # no classes, use explicit labels
        self.label_refits_allowed = ['IRON']
        self.label_refits_disallowed = []
        self.default_cargos = ['IRON']
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
        self.weight_factor = 2 # double the default weight
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['freight_core']
        self._joker = True
        # articulated so can't flip
        self.allow_flip = False
        # Graphics configuration
        # custom gestalt with dedicated template as these wagons are articulated which standard wagon templates don't support
        self.gestalt_graphics = GestaltGraphicsCustom('vehicle_torpedo_car.pynml')


class VehiclePartsBoxCarConsist(CarConsist):
    """
    Vehicle parts box car, van - same refits as box car, just a specific visual variation.
    """

    def __init__(self, **kwargs):
        self.base_id = 'vehicle_parts_box_car'
        super().__init__(**kwargs)
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label['box_freight']
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label['non_freight_special_cases']
        self.default_cargos = polar_fox.constants.default_cargos['box']
        self.buy_cost_adjustment_factor = 1.2
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = 1 # single base colour unless flipped
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(id_base='vehicle_parts_box_car',
                                                                  recolour_maps=graphics_constants.box_livery_recolour_maps)


class VehicleTransporterCarConsist(CarConsist):
    """
    Transports vehicles cargo
    """

    def __init__(self, **kwargs):
        self.base_id = 'vehicle_transporter_car'
        super().__init__(**kwargs)
        self.speed_class = 'express'
        self.class_refit_groups = [] # no classes, use explicit labels
        self.label_refits_allowed = [ 'PASS', 'VEHI', 'ENSP', 'FMSP']
        self.label_refits_disallowed = []
        self.default_cargos = ['VEHI']
        self._intro_date_days_offset = global_constants.intro_date_offsets_by_role_group['non_core_wagons']
        # !! flipping not currently allowed as don't know if asymmetric sprites support is working (might be fine?) (works for containers ok)
        self.allow_flip = True # hax test because template failing to return correct cargo sprites
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVehicleTransporter()

    @property
    # account for e.g. low floor, double deck etc
    def platform_type(self):
        # !! all default currently, extend as needed - see intermodal cars for example
        return 'default'


class Train(object):
    """
    Base class for all types of trains
    """

    def __init__(self, **kwargs):
        self.consist = kwargs.get('consist')

        # setup properties for this train
        self.numeric_id = kwargs.get('numeric_id', None)
        # vehicle_length is either derived from chassis length or similar, or needs to be set explicitly as kwarg
        self._vehicle_length = kwargs.get('vehicle_length', None)
        self._weight = kwargs.get('weight', None)
        self.capacity = kwargs.get('capacity', 0)
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        # spriterow_num allows assigning sprites for multi-part vehicles, and is not supported in all vehicle templates (by design - TMWFTLB to support)
        self.spriterow_num = kwargs.get('spriterow_num', 0) # first row = 0;
        # sometimes we want to offset the buy menu spriterow (!! this is incomplete hax, not supported by generated buy menu sprites etc)
        self.buy_menu_spriterow_num = 0 # set in the subclass as needed, (or extend to kwargs in future)
        # !! the need to copy cargo refits from the consist is legacy from the default multi-unit articulated consists in Iron Horse 1
        # !! could likely be refactored !!
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.autorefit = True
        # nml constant (STEAM is sane default)
        self.engine_class = 'ENGINE_CLASS_STEAM'
        # structure for effect spawn and sprites, default and per railtype as needed
        self.effects = {} # empty if no effects, set in subtypes as needed
        # optional, use to over-ride automatic effect positioning
        # expects a list of offset pairs [(x, y), (x, y)] etc
        # n.b max 4 effects (nml limit)
        self._effect_offsets = kwargs.get('effect_offsets', None)
        # z offset is rarely used and is handled separately, mostly just for low-height engines
        self._effect_z_offset = kwargs.get('effect_z_offset', None)
        self.default_effect_z_offset = 12 # optimised for Pony diesel and electric trains
        # optional - only set if the graphics processor generates the vehicle chassis
        self.chassis = kwargs.get('chassis', None)
        # optional - occasionally we need to suppress composited roof sprites and just draw our own
        self.suppress_roof_sprite = kwargs.get('suppress_roof_sprite', False)
        # optional - some engine units need to set explicit tail light spritesheets
        # subclasses may over-ride this, e.g. wagons have an automatic tail light based on vehicle length
        self.tail_light = kwargs.get('tail_light', 'empty')
        # 'symmetric' or 'asymmetric'?
        # defaults to symmetric, over-ride in sub-classes or per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')
        # optional - a switch name to trigger re-randomising vehicle random bits - over-ride as need in subclasses
        self.random_trigger_switch = None

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
        if self.default_cargo_capacity != 0:
            return True
        else:
            return False

    @property
    def weight(self):
        # weight can be set explicitly or by methods on subclasses
        return self._weight

    @property
    def vehicle_length(self):
        # length of this unit, either derived from from chassis length, or set explicitly via keyword
        # first guard that one and only one of these props is set
        if self._vehicle_length is not None and self.chassis is not None:
            utils.echo_message(self.consist.id + ' has units with both chassis and length properties set')
        if self._vehicle_length is None and self.chassis is None:
            utils.echo_message(self.consist.id + ' has units with neither chassis nor length properties set')

        if self.chassis is not None:
            # assume that chassis name format is 'foo_bar_ham_eggs_24px' or similar - true as of Nov 2020
            # if chassis name format changes / varies in future, just update the string slice accordingly, safe enough
            # splits on _, then takes last entry, then slices to remove 'px'
            result = int(self.chassis.split('_')[-1][0:-2])
            return int(result / 4)
        else:
            return self._vehicle_length

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
            self._symmetry_type, self.consist.id)
        return self._symmetry_type

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC', 'TRAIN_FLAG_SPRITE_STACK']
        if self.consist.allow_flip:
            special_flags.append('TRAIN_FLAG_FLIP')
        if self.autorefit:
            special_flags.append('TRAIN_FLAG_AUTOREFIT')
        if self.consist.tilt_bonus:
            special_flags.append('TRAIN_FLAG_TILT')
        if self.consist.train_flag_mu:
            special_flags.append('TRAIN_FLAG_MU')
        return ','.join(special_flags)

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        if hasattr(self, 'articulated_unit_different_class_refit_groups'):
            # in *rare* cases an articulated unit might need different refit classes to its parent consist
            class_refit_groups = self.articulated_unit_different_class_refit_groups
        else:
            # by default get the refit classes from the consist
            class_refit_groups = self.consist.class_refit_groups
        for i in class_refit_groups:
            [cargo_classes.append(
                cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes))  # use set() here to dedupe

    def get_loading_speed(self, capacity_param):
        # ottd vehicles load at different rates depending on type,
        # normalise default loading time for this set to 240 ticks, regardless of capacity
        # openttd loading rates vary by transport type, look them up in wiki to find value to use here to normalise loading time to 240 ticks
        # this is (240 / loading frequency in ticks for transport type) from wiki
        transport_type_rate = 6
        return int(self.loading_speed_multiplier * math.ceil(self.capacities[capacity_param] / transport_type_rate))

    @property
    def running_cost_base(self):
        # all engines use the same RUNNING_COST_STEAM, and Iron Horse provides the variation between steam/electric/diesel
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # wagons will use RUNNING_COST_DIESEL - set in wagon subclass
        return 'RUNNING_COST_STEAM'

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
        # optionally drop the cargos in the compile, can save substantial compile time
        if utils.get_makefile_args(sys).get('suppress_cargo_sprites', False):
            return 'vehicle_default.pynml'

        if self.consist.gestalt_graphics.nml_template:
            return self.consist.gestalt_graphics.nml_template
        # default case
        return 'vehicle_default.pynml'

    @property
    def location_of_random_bits_for_random_variant(self):
        # articulated vehicles should get random bits from first unit, so that all units randomise consistently
        # IMPORTANT: cannot rely on returning FORWARD_SELF(0), it causes register 0x100 to be read and cleared, where 0x100 is needed for graphics layers
        # https://newgrf-specs.tt-wiki.net/wiki/NML:Random_switch#cite_note-expression-1
        if len(self.consist.units) > 1 and self.numeric_id != self.consist.base_numeric_id:
            return 'FORWARD_SELF(' + str(self.numeric_id - self.consist.base_numeric_id) + ')'
        else:
            return 'SELF'

    @property
    def roof(self):
        # fetch spritesheet name to use for roof when generating graphics
        if self.consist.roof_type is not None:
            if self.consist.base_track_type == 'NG':
                ng_prefix = 'ng_'
            else:
                ng_prefix = ''
            return str(4 * self.vehicle_length) + 'px_' + ng_prefix + self.consist.roof_type
        else:
            return None

    @property
    def requires_colour_mapping_cb(self):
        # bit weird and janky, various conditions to consider eh
        if getattr(self.consist, 'use_colour_randomisation_strategies', False):
            return 'use_colour_randomisation_strategies'
        elif getattr(self.consist.gestalt_graphics, 'colour_mapping_switch', None) is not None:
            return 'colour_mapping_switch'
        else:
            return None

    @property
    def default_effect_offsets(self):
        # over-ride this in subclasses as needed (e.g. to move steam engine smoke to front by default
        # vehicles can also over-ride this on init (stored on each model_variant as _effect_offsets)
        return [(0, 0)]

    def get_nml_expression_for_effects(self, reversed_variant, railtype='default'):
        # provides part of nml switch for effects (smoke)

        # effects can be over-ridden per vehicle, or use a default from the vehicle subclass
        if self._effect_offsets is not None:
            effect_offsets = self._effect_offsets
        else:
            effect_offsets = self.default_effect_offsets

        # when vehicles (e.g. steam engines) are reversed, invert the effect x position
        if reversed_variant == 'reversed':
            effect_offsets = [(offsets[0] * -1, offsets[1]) for offsets in effect_offsets]

        # z offset is handled independently to x, y for simplicity, option to over-ride z offset default per vehicle
        if self._effect_z_offset is not None:
            z_offset = self._effect_z_offset
        else:
            z_offset = self.default_effect_z_offset

        # changing sprite by railtype is supported, changing position is *not* as of August 2019
        effect_sprite = self.effects[railtype][1]

        result = []
        for index, offset_pair in enumerate(effect_offsets):
            items = [effect_sprite, str(offset_pair[0]), str(offset_pair[1]), str(z_offset)]
            result.append('STORE_TEMP(create_effect(' + ','.join(items) + '), 0x10' + str(index) + ')')
        return ['[' + ','.join(result) + ']', str(len(result)) + ' + CB_RESULT_CREATE_EFFECT_CENTER']

    @property
    def switch_id_for_create_effect(self):
        # randomly reversed vehicles need to use a dependent random switch, this doesn't exist for non-reversible vehicles, so need to conditionally handle switch routing
        if len(self.consist.reversed_variants) > 1:
            return self.id + "_switch_create_effect_reversed_variants"
        else:
            return self.id + "_switch_create_effect_check_railtype_" + self.consist.reversed_variants[0]

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]")
        return expression_template.substitute(unit_offset=unit_offset)

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # best used with the check for same grfid, but eh
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]")
        return expression_template.substitute(unit_offset=unit_offset)

    def get_spriteset_template_name(self, reversed, flipped, y):
        template_name = '_'.join(['spriteset_template', self.symmetry_type, reversed, str(self.vehicle_length), '8', flipped])
        anim_flag = 'ANIM' if self.consist.suppress_animated_pixel_warnings else 'NOANIM'
        args = ','.join([str(y), anim_flag])
        return template_name + '(' + args + ')'

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

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " +
                                   i + " which is not defined in the cargo table")

    def render(self, templates):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        self.assert_random_reverse()
        # test interpolated gen and intro_date
        assert(self.consist.gen), '%s consist.gen is None, which is invalid.  Set gen or intro_date' % self.id
        assert(self.consist.intro_date), '%s consist.gen is None, which is invalid.  Set gen or intro_date' % self.id
        # templating
        template_name = self.vehicle_nml_template
        template = templates[template_name]
        nml_result = template(vehicle=self,
                              consist=self.consist,
                              global_constants=global_constants,
                              temp_storage_ids=global_constants.temp_storage_ids, # convenience measure
                              graphics_path=global_constants.graphics_path)
        return nml_result


class AutoCoachCombineUnitMail(Train):
    """
    Mail unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL' # !! needs changing??
        self.effects = {}
        self.consist.str_name_suffix = None
        self._symmetry_type = 'asymmetric'
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = ['mail'] # note mail only, no other express cargos
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        # account for pax capacity 'on' this unit (implemented on adjacent pax unit)
        self.capacity = (0.75 * self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class AutoCoachCombineUnitPax(Train):
    """
    Pax unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL' # !! needs changing??
        self.effects = {}
        self.consist.str_name_suffix = None
        self._symmetry_type = 'asymmetric'
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = ['pax']
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        # account for pax 'on' the adjacent mail unit (this is roughly matched to equivalent gen railcars)
        self.capacity = 2 * self.vehicle_length * base_capacity


class CabbageDVTUnit(Train):
    """
    Unit for a DVT / Cabbage (driving cab with mail capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL' # probably fine?
        self.effects = {}
        self.consist.str_name_suffix = None
        self._symmetry_type = 'asymmetric'
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class DieselEngineUnit(Train):
    """
    Unit for a diesel engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_DIESEL', 'EFFECT_SPRITE_DIESEL']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_DIESEL'
        # most diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class DieselRailcarBaseUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to set symmetry.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # the cab magic won't work unless it's asymmetric eh? :)
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')
        # note that railcar effects are left in default position, no attempt to move them to end of vehicle, or double them (tried, looks weird)


class DieselRailcarMailUnit(DieselRailcarBaseUnit):
    """
    Unit for a mail diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class DieselRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity


class ElectricEngineUnit(Train):
    """
    Unit for an electric engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        # almost all electric engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class ElectricHighSpeedPaxUnit(Train):
    """
    Unit for high-speed, high-power pax electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'
        # magic to set high speed pax car capacity subject to length
        # uses a value in between pax and lux pax; this won't work with double deck high speed in future, extend a kwarg then if needed
        # use a conditional so that some cab cars can set capacity 0
        if kwargs.get('capacity', None) is not None:
            self.capacity = kwargs['capacity']
        else:
            base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
            self.capacity = int(self.vehicle_length * base_capacity * 0.875)


class ElectroDieselEngineUnit(Train):
    """
    Unit for a bi-mode Locomotive - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_DIESEL', 'EFFECT_SPRITE_DIESEL'],
                        'ELRL': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRODIESEL'
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1 # will get same buy cost factor as electric engine of same gen (blah balancing)
        # almost all electro-diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class ElectroDieselRailcarBaseUnit(Train):
    """
    Unit for a bi-mode railcar - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_DIESEL', 'EFFECT_SPRITE_DIESEL'],
                        'ELRL': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRODIESEL'
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1.15 # will get higher buy cost factor than electric railcar of same gen (blah balancing)
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2 # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = 2 # frankly hax at this point :|
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'


class ElectroDieselRailcarMailUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a mail electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class ElectroDieselRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity


class ElectroDieselLuxuryRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel luxury railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = int(self.vehicle_length * base_capacity * 0.75)


class ElectricRailcarBaseUnit(Train):
    """
    Unit for an electric railcar.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'


class ElectricLuxuryRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a luxury pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = int(self.vehicle_length * base_capacity * 0.75)


class ElectricRailcarMailUnit(ElectricRailcarBaseUnit):
    """
    Unit for a mail electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2 # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = self.buy_menu_spriterow_num # frankly hax at this point :|


class ElectricRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2 # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = self.buy_menu_spriterow_num # frankly hax at this point :|


class MetroUnit(Train):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs['consist'].base_track_type = 'METRO'
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_ELECTRIC', 'EFFECT_SPRITE_ELECTRIC']}
        self.default_effect_z_offset = 1 # optimised for Pony diesel and electric trains
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_METRO'
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'


class SnowploughUnit(Train):
    """
    Unit for a snowplough.  Snowploughs have express cargo capacity, so they can actually be useful. :P
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_DIESEL' # !! needs changing??
        self.effects = {}
        self.consist.str_name_suffix = None
        self._symmetry_type = 'asymmetric'
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class SteamEngineUnit(Train):
    """
    Unit for a steam engine, with smoke
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.effects = {'default': ['EFFECT_SPAWN_MODEL_STEAM', 'EFFECT_SPRITE_STEAM']}
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_STEAM'
        self.default_effect_z_offset = 13 # optimised for Pony steam trains
        self._symmetry_type = 'asymmetric'  # assume all steam engines are asymmetric

    @property
    def default_effect_offsets(self):
        # force steam engine smoke to front by default, can also over-ride per unit for more precise positioning
        return [(1 + int(math.floor(-0.5 * self.vehicle_length)), 0)]


class SteamEngineTenderUnit(Train):
    """
    Unit for a steam engine tender.
    Arguably this class is pointless, as it is just passthrough.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # assume all steam engine tenders are asymmetric
        self._symmetry_type = 'asymmetric'


# alphabetised (mostly) non-TrainCar subclasses of Train above here
# then TrainCar subclasses below here, also alphabetised

class TrainCar(Train):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by Train with useful defaults.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist = kwargs['consist']
        if hasattr(self.consist, 'loading_speed_multiplier'):
            self.loading_speed_multiplier = self.consist.loading_speed_multiplier
        # most wagons are symmetric, over-ride per vehicle or subclass as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')
        # all wagons use auto tail-lights based on length
        self.tail_light = str(self.vehicle_length * 4) + 'px'

    @property
    def running_cost_base(self):
        # all wagons use the same RUNNING_COST_DIESEL, this is nerfed down to give appropriate increments for low wagon run costs
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # engines will all use RUNNING_COST_STEAM
        return 'RUNNING_COST_DIESEL'

    @property
    def weight(self):
        # set weight based on capacity  * a multiplier from consist * roster gen factor
        return int(self.consist.weight_factor * self.default_cargo_capacity * self.consist.roster.train_car_weight_factors[self.consist.gen - 1])

class AlignmentCar(TrainCar):
    """
    Alignment Car, for debugging sprite positions
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = 'asymmetric'


class CabooseCar(TrainCar):
    """
    Caboose Car. This sub-class only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def weight(self):
        # special handling of weight
        weight_factor = 3 if self.consist.base_track_type == 'NG' else 5
        return weight_factor * self.vehicle_length


class MailCar(TrainCar):
    """
    Mail wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # mail wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = 'asymmetric'
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class PaxCar(TrainCar):
    """
    Pax wagon. This subclass only exists to set capacity and symmetry_type.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = 'asymmetric'
        # magic to set pax car capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity


class HSTPaxCar(TrainCar):
    """
    Pax wagon for HST-type trains. This subclass only exists to set capacity and symmetry_type.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = 'asymmetric'
        # magic to set dedicated pax car capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = int(self.vehicle_length * base_capacity * 0.875)


class LuxuryPaxCar(TrainCar):
    """
    Luxury pax wagon. This subclass only exists to set capacity and symmetry_type.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = 'asymmetric'
        # magic to set luxury pax car capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = int(self.vehicle_length * base_capacity * 0.75)


class ExpressCar(TrainCar):
    """
    Express freight car.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        # we nerf down express car capacity to same as mail cars, to account for them being faster
        self.capacity = (self.vehicle_length * base_capacity) / polar_fox.constants.mail_multiplier


class ExpressIntermodalCar(ExpressCar):
    """
    Express container car, subclassed from express car.  This subclass only exists to symmetry_type, random trigger and colour mapping switches.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # express intermodal cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = 'asymmetric'
        self.random_trigger_switch = '_switch_graphics_containers'


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
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (self.vehicle_length * base_capacity)


class CoilBuggyCar(FreightCar):
    """
    Coil buggy car. This subclass only exists to set the capacity.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # just double whatever is set by the init, what could go wrong? :)
        self.capacity = 2 * self.capacity


class IngotCar(FreightCar):
    """
    Ingot car. This subclass only exists to set the capacity.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # just double whatever is set by the init, what could go wrong? :)
        self.capacity = 2 * self.capacity


class IntermodalCar(FreightCar):
    """
    Intermodal Car. This subclass only exists to symmetry_type, random trigger and colour mapping switches.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # intermodal cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = 'asymmetric'
        self.random_trigger_switch = '_switch_graphics_containers'


class PaxRailcarTrailerCar(TrainCar):
    """
    Railcar unpowered pax trailer. This subclass only exists to set capacity and symmetry_type.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TrainCar sets auto tail light, over-ride it
        self.tail_light = kwargs['tail_light'] # fail if not passed, required arg
        # pax wagons may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = 'asymmetric'
        # magic to set pax car capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity


class PaxLuxuryRailcarTrailerCar(TrainCar):
    """
    Luxury railcar unpowered pax trailer. This subclass only exists to set capacity and symmetry_type.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TrainCar sets auto tail light, over-ride it
        self.tail_light = kwargs['tail_light'] # fail if not passed, required arg
        # pax wagons may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = 'asymmetric'
        # magic to set pax car capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = int(self.vehicle_length * base_capacity * 0.75)


class SlagLadleCar(FreightCar):
    """
    Slag ladle car. This subclass only exists to set the capacity.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # just double whatever is set by the init, what could go wrong? :)
        self.capacity = 2 * self.capacity


class TorpedoCar(FreightCar):
    """
    Torpedo car. This subclass sets the symmetry_type to asymmetric.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # just multiply whatever is set by the init, what could go wrong? :)
        self._symmetry_type = 'asymmetric'
        # capacity bonus is solely to support using small stations in Steeltown where space between industries is constrained
        self.capacity = 1.5 * self.capacity


class VehicleTransporterCar(FreightCar):
    """
    Vehicle transporter car.  This subclass only exists to symmetry_type, random trigger and colour mapping switches.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # vehicle transporter cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = 'asymmetric'
        self.random_trigger_switch = '_switch_graphics_containers'


