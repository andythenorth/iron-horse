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
                                               GestaltGraphicsCaboose, GestaltGraphicsCargoSpecificLivery, GestaltGraphicsOnlyAddPantographs,
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
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get('roster_id') # just fail if there's no roster
        # either gen xor intro_date is required, don't set both, one will be interpolated from the other
        self._intro_date = kwargs.get('intro_date', None)
        self._gen = kwargs.get('gen', None)
        # if gen is used, the calculated intro date can be adjusted with +ve or -ve offset
        self.intro_date_offset = kwargs.get('intro_date_offset', None)
        self.vehicle_life = kwargs.get('vehicle_life', 40)
        self.power = kwargs.get('power', 0)
        self.base_track_type = kwargs.get('base_track_type', 'RAIL')
        # modify base_track_type for electric engines when writing out the actual rail type
        # without this, RAIL and ELRL have to be specially handled whenever a list of compatible consists is wanted
        # this *does* need a specific flag, can't rely on unit visual effect or unit engine type props - they are used for other things
        self.requires_electric_rails = False # set by unit subclasses as needed, not a kwarg
        self.tractive_effort_coefficient = kwargs.get(
            'tractive_effort_coefficient', 0.3)  # 0.3 is recommended default value
        # private var, can be used to over-rides default (per generation, per class) speed
        self._speed = kwargs.get('speed', None)
        # default cargo age period, over-ride in subclass as needed
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_railtype = kwargs.get('power_by_railtype', None)
        self.visual_effect_override_by_railtype = kwargs.get(
            'visual_effect_override_by_railtype', None)
        # some engines require pantograph sprites composited, don't bother setting this unless required
        self.pantograph_type = kwargs.get('pantograph_type', None)
        self.dual_headed = 1 if kwargs.get('dual_headed', False) else 0
        self.tilt_bonus = False  # over-ride in subclass as needed
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        self.easter_egg_haulage_speed_bonus = kwargs.get('easter_egg_haulage_speed_bonus', False)
        # random_reverse means (1) randomised reversing of sprites when vehicle is built (2) player can also flip vehicle
        # random_reverse is not supported in some templates
        self.random_reverse = kwargs.get('random_reverse', False)
        self.allow_flip = self.random_reverse # random_reverse vehicles can always be flipped, but flip can also be set in other cases (by subclass)
        # just a simple buy cost tweak, only use when needed
        self.electro_diesel_buy_cost_malus = None
        # arbitrary multiplier to the calculated buy cost, e.g. 1.1, 0.9 etc
        # set to 1 by default, over-ride in subclasses as needed
        self.buy_cost_adjustment_factor = 1
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
        # option to swap company colours (uses remap sprites in-game, rather than pixa)
        self.random_company_colour_swap = False  # over-ride in subclasses as needed
        # role is e.g. Heavy Freight, Express etc, and is used to automatically set model life as well as in docs
        self.role = kwargs.get('role', None)
        # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get(
            'suppress_animated_pixel_warnings', False)
        # by design, occasional 'joker' engines are included that don't fit the roster pattern, this is to add variety
        self.joker = kwargs.get('joker', False)
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
        return set([unit.spriterow_num for unit in self.units])

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
        return "string(STR_NAME_CONSIST_PARENTHESES, string(STR_NAME_" + self.id + "), string(" + self.str_name_suffix + "))"

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
            if unit.always_use_same_spriterow:
                unit_rows.append('always_use_same_spriterow')
            else:
                # assumes gestalt_graphics is used to handle any other rows, no other cases at time of writing, could be changed eh?
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
    def livery_2_engine_ids(self):
        # for vehicles with consist-specific liveries
        # will switch vehicle to livery 2 for specific roles of lead engine
        result = []
        for consist in self.roster.engine_consists:
            # second livery choice is deliberate, means 'as seen in buy menu' livery is built for common case of express_1, heavy_express_1
            if consist.role in ['branch_express', 'express_2', 'heavy_express_2', 'pax_railcar_2', 'mail_railcar_2']:
                result.append(consist.id)
        return result

    @property
    def haulage_bonus_engine_id_tree(self):
        express_engine_ids = []
        for consist in self.roster.engine_consists:
            if consist.role in self.express_roles:
                express_engine_ids.append(consist.id)
        return [(count, id) for count, id in enumerate(express_engine_ids)]

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
    def model_life(self):
        similar_consists = []
        for consist in self.roster.engine_consists:
            if consist.role == self.role and consist.base_track_type == self.base_track_type:
                similar_consists.append(consist)
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

    @property
    def express_roles(self):
        # for cases where we need to know all the roles that reduce to 'express'
        # aside: total abuse of @property, I have no justification other than it fits the pattern in context :P
        return ['branch_express', 'express_1', 'express_2', 'heavy_express_1', 'heavy_express_2']

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
            if self.role in self.express_roles:
                return self.get_speed_by_class('express')
            elif self.role in ['pax_high_speed']:
                return self.get_speed_by_class('very_high_speed')
            else:
                return self.get_speed_by_class('standard')
        else:
            # assume no speed limit
            return None

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

    def render_articulated_switch(self):
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

    def render(self):
        self.assert_speed()
        self.assert_power()
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
        kwargs['roster_id'] = kwargs.get('roster').id
        super().__init__(**kwargs)
        # arbitrary multiplier to floating run costs (factors are speed, power, weight)
        # adjust per subtype as needed
        self.floating_run_cost_multiplier = 8.5
        # fixed (baseline) run costs on this subtype
        self.fixed_run_cost_points = 180
        # Graphics configuration only as required
        # just check if pantograph generation is needed for this engine
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        if self.pantograph_type is not None:
            self.gestalt_graphics = GestaltGraphicsOnlyAddPantographs()

    @property
    def buy_cost(self):
        # max speed = 200mph by design - see assert_speed()
        # multiplier for speed, max value will be 25
        speed_cost_points = self.speed / 8
        # max power 10000hp by design - see assert_power()
        # malus for electric engines, ~33% higher equipment costs
        # !! this is an abuse of requires_electric_rails, but it's _probably_ fine :P
        if self.requires_electric_rails:
            power_factor = self.power / 750
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
        # start from an arbitrary baseline of 100 points, add points for gen, cost points, seems to work
        # cap to int for nml
        return int(10 + self.gen + buy_cost_points)

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
        # multiplier for power, max value will be 16
        power_factor = self.power / (250 if is_NG else 625)
        # max weight = 500t by design - see assert_weight() - (NG assumes 200t max)
        # multiplier for weight, max value will be 8
        weight_factor = self.weight / (32 if is_NG else 62.5)

        # !! this is an abuse of requires_electric_rails, but it's _probably_ fine :P
        if self.requires_electric_rails:
            if 'railcar' in self.role:
                # massive bonus to el railcars
                power_factor = 0.4 * power_factor
            else:
                # much smaller bonus to electric engines
                # they already tend to be lighter per unit power (so cheaper to run) than similar power types
                power_factor = 0.8 * power_factor
        elif self.electro_diesel_buy_cost_malus is not None:
            if 'railcar' in self.role:
                # bonus to ED railcars (ED engines are fine without this)
                power_factor = 0.6 * power_factor

        # basic cost from speed, power, weight
        floating_run_cost_points = speed_cost_factor * power_factor * weight_factor
        # then multiply by a factor specific to the subtype, so that we can control how much floating costs matter for this subtype
        # be aware that engines cost base is nerfed down, otherwise, wagon costs aren't fine grained enough
        # this means that floating_run_cost_multiplier might need to be > 3 to reset the base cost nerf
        floating_run_cost_points = floating_run_cost_points * self.floating_run_cost_multiplier
        fixed_run_cost_points = self.fixed_run_cost_points
        # massive bonus for NG
        # !! these NG multipliers are just magic numbers that work for Pony NG roster, they probably fail in other rosters
        if is_NG:
            floating_run_cost_points = 0.4 * floating_run_cost_points
            fixed_run_cost_points = 0.6 * fixed_run_cost_points
        # add floating cost to the fixed (baseline) cost (which is arbitrary points, range 0-200-ish)
        # multiply by gen and an arbitrary factor to give the results I want
        # the aim is to space costs widely across types within a generation, but mostly flatten them across generations of same type
        gen_multiplier = 13 - self.gen
        run_cost = gen_multiplier * (fixed_run_cost_points + floating_run_cost_points)
        # freight engines get a substantial run cost bonus as they'll often be sat waiting for loads, so balance (also super realism!!)
        # doing this is preferable to doing variable run costs, which are weird and confusing (can't trust the costs showin in vehicle window)
        if 'freight' in self.role:
            run_cost = 0.8 * run_cost
        # cap to int for nml
        return int(run_cost)


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
        # also reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 96


class PassengerEngineMetroConsist(PassengerEngineConsist):
    """
    Consist for a pax metro train.  Just a sparse subclass to force the gestalt_graphics
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 1, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="metro")


class PassengerEngineRailcarConsist(PassengerEngineConsist):
    """
    Consist for a pax railcar.  Just a sparse subclass to force the gestalt_graphics and allow_flip
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # this will knock standard age period down, so this train is less profitable over ~128 tiles than a similar luxuryy train
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_STANDARD_PAX_MALUS

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
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="pax_railcars",
                                                                     pantograph_type=self.pantograph_type)


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
        self.tilt_bonus = True
        # moderate cargo age bonus
        self.cargo_age_period = 1.33 * global_constants.CARGO_AGE_PERIOD
        # note that buy costs are actually adjusted down from pax base, to account for distributed traction etc
        self.buy_cost_adjustment_factor = 0.95
        # run costs are set to make high speed train costs all high, with floating costs having smaller effect relative to normal trains
        # note that run cost multiplier is actually adjusted down from pax base, to account for distributed traction etc
        self.floating_run_cost_multiplier = 6
        # ...but very high fixed (baseline) run costs on this subtype
        self.fixed_run_cost_points = 200
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
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

class PassengerVeryHighSpeedMiddleEngineConsist(PassengerEngineConsist):
    """
    Consist for an intermediate motor unit for very high speed train (TGV etc).
    When added to the correct cab engine, this vehicle will cause cab power to increase.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cab_id = self.id.split('_middle')[0] + '_cab'
        self.wagons_add_power = True
        self.tilt_bonus = True
        # moderate cargo age bonus
        self.cargo_age_period = 1.33 * global_constants.CARGO_AGE_PERIOD
        # train_flag_mu solely used for ottd livery (company colour) selection
        # eh as of Feb 2019, OpenTTD won't actually use this for middle cars, as not engines
        # this means the buy menu won't match, but wagons will match anyway when attached to cab
        # prop left in place in case that ever gets changed :P
        self.train_flag_mu = True
        # Graphics configuration
        self.roof_type = 'pax_mail_smooth'
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * default unit
        # * unit with pantograph - leading end
        # * unit with pantograph -  rear end
        # * restaurant unit
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 1, 'last': 2, 'special': 3}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="pax_cars",
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


class MailEngineConsist(EngineConsist):
    """
    Consist of engines / units that has mail (and express freight) capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ['TOUR']
        self.default_cargos = global_constants.default_cargos['mail']
        # increased costs for having extra doors and stuff eh?
        self.buy_cost_adjustment_factor = 1.4
        # reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 96


class MailEngineMetroConsist(MailEngineConsist):
    """
    Consist for a mail metro train.  Just a sparse subclass to force the gestalt_graphics
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # 1 livery as can't be flipped, 1 spriterow may be left blank for compatibility with Gestalt (TBC)
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 1, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="metro")


class MailEngineRailcarConsist(MailEngineConsist):
    """
    Consist for a mail railcar.  Just a sparse subclass to force the gestalt_graphics and allow_flip
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
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
        # ruleset will combine these to make multiple-units 1 or 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {'mail': {'default': 0, 'first': 1, 'last': 2, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset="mail_railcars",
                                                                     pantograph_type=self.pantograph_type)


class CarConsist(Consist):
    """
    Intermediate class for car (wagon) consists to subclass from, provides sparse properties, most are declared in subclasses.
    """

    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs['id'] = id
        kwargs['roster_id'] = kwargs['roster'] # conflation of 'roster' and 'roster_id' here, could be refactored, but eh
        super().__init__(**kwargs)
        self.roster.register_wagon_consist(self)

        self.speed_class = 'standard'  # over-ride this in sub-class for, e.g. express freight consists
        self.subtype = kwargs['subtype']
        # Weight factor: over-ride in sub-class as needed
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type == 'NG' else 1
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        # assume all wagons randomly swap CC, revert to False in wagon subclasses as needed
        self.random_company_colour_swap = True

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
        length_cost_factor = self.length / 8
        # start from an arbitrary baseline and add speed cost
        run_cost_points = 100 + speed_cost_points
        # multiply by length (after baseline, so the 8/8 cost is always twice 4/8 etc
        run_cost_points = run_cost_points * length_cost_factor
        # multiply up by arbitrary amount, to where I want wagon run costs to be
        # (base cost is set deliberately low to allow small increments for fine-grained control)
        run_cost_points = 3 * run_cost_points * self.floating_run_cost_multiplier
        # narrow gauge gets a bonus
        if self.base_track_type == 'NG':
            run_cost_points = 0.5 * run_cost_points
        # cap to int for nml
        return int(run_cost_points)

    @property
    def model_life(self):
        # automatically span wagon model life across gap to next generation
        # FYI next generation might be +n, not +1
        # don't check wagon subtype, only wagon subclass and track type (otherwise, e.g. A never expire even if replaced permanently by B)
        roster_gens_for_class = sorted(set(
            [wagon.gen for wagon in self.roster.wagon_consists[self.base_id] if wagon.base_track_type == self.base_track_type]))
        this_index = roster_gens_for_class.index(self.gen)
        if this_index == len(roster_gens_for_class) - 1:
            return 'VEHICLE_NEVER_EXPIRES'
        else:
            next_gen = roster_gens_for_class[roster_gens_for_class.index(self.gen) + 1]
            next_gen_intro_date = self.roster.intro_dates[self.base_track_type][next_gen-1]
            return next_gen_intro_date - self.intro_date

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get('base_track_type', None) == 'NG':
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
        if self.subtype == 'U':
            # subtype U is a hack to indicate there is only one subtype for this wagon, so no suffix needed
            return "string(STR_NAME_CONSIST_PLAIN, string(" + self.get_wagon_title_class_str() + "))"
        else:
            return "string(STR_NAME_CONSIST_PARENTHESES, string(" + self.get_wagon_title_class_str() + "), string(" + self.get_wagon_title_subtype_str() + "))"


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
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        self.buy_cost_adjustment_factor = 0 # free
        # no random CC, no flip
        self.random_company_colour_swap = False
        self.allow_flip = False


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
        self.buy_cost_adjustment_factor = 1.2
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base='box_car',
            recolour_maps=graphics_constants.box_livery_recolour_maps)


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
        self.buy_cost_adjustment_factor = 0.75 # chop down caboose costs, they're just eye candy eh
        # liveries swap CC on user-flip, so no swapping CC randomly
        self.random_company_colour_swap = False
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(num_generations=len(self.roster.intro_dates[self.base_track_type]),
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
        self.buy_cost_adjustment_factor = 1.2
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        # Graphics configuration
        # covered hopper cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # the player can simply choose the alternative livery on flip
        # there is no randomisation of livery, but CC is randomised
        spriterow_group_mappings = {'pax': {'default': 0, 'first': 0, 'last': 0, 'special': 0}}
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset=None)


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
        self.loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True, has_alt_livery=True)


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
        self.class_refit_groups = ['liquids']
        self.label_refits_allowed = ['FOOD']
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_edible_liquids']
        self.default_cargos = global_constants.default_cargos['edibles_tank']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCargoSpecificLivery(
            recolour_maps=polar_fox.constants.tanker_livery_recolour_maps)


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
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['express']
        # adjust weight factor because express car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self.floating_run_cost_multiplier = 1.2
        self.allow_flip = True
        # Graphics configuration
        if self.gen in [1]:
            self.roof_type = 'pax_mail_clerestory'
        elif self.gen in [2, 3]:
            self.roof_type = 'pax_mail_ridged'
        else:
            self.roof_type = 'pax_mail_smooth'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base='express_car',
            recolour_maps=graphics_constants.box_livery_recolour_maps)


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
        self.class_refit_groups = []
        self.label_refits_allowed = ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['fruit_veg']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.2
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base='box_car',
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
        self.buy_cost_adjustment_factor = 1.2
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True, has_alt_livery=True)


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
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsCargoSpecificLivery(
            recolour_maps=graphics_constants.livestock_livery_recolour_maps)


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
        self.label_refits_disallowed = global_constants.disallowed_refits_by_label[
            'non_freight_special_cases']
        self.default_cargos = global_constants.default_cargos['mail']
        # adjust weight factor because mail car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self.floating_run_cost_multiplier = 1.2
        self.allow_flip = True
        self.random_company_colour_swap = False
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
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
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
        # allow flipping, used to flip company colour
        self.allow_flip = True
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
        self.speed_class = 'express'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['pax']
        self.random_company_colour_swap = False
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
    """

    def __init__(self, **kwargs):
        self.base_id = 'passenger_car'
        super().__init__(**kwargs)
        # this will knock standard age period down, so this train is less profitable over ~128 tiles than a similar luxuryy train
        self.cargo_age_period = global_constants.CARGO_AGE_PERIOD_STANDARD_PAX_MALUS
        self.buy_cost_adjustment_factor = 1.3
        self.floating_run_cost_multiplier = 1.5
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
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset='pax_cars')


class PassengerLuxuryCarConsist(PassengerCarConsistBase):
    """
    Improved decay rate and lower capacity per unit length compared to standard pax car.
    Possibly random sprites for restaurant car, observation car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = 'luxury_passenger_car'
        super().__init__(**kwargs)
        # this won't make much difference except over *very* long routes, but set it anyway
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.6
        self.floating_run_cost_multiplier = 2.25
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
        self.gestalt_graphics = GestaltGraphicsConsistSpecificLivery(spriterow_group_mappings, consist_ruleset='pax_cars')


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
        self.default_cargos = global_constants.default_cargos['reefer']
        self.cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.66
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = 'freight'
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base='box_car',
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
        self.buy_cost_adjustment_factor = 1.2
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
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece='stake')


class WellCarConsist(CarConsist):
    """
    Low-floor wagon, with support for asymmetric sprites
    """

    def __init__(self, **kwargs):
        self.base_id = 'well_car'
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = ['ENSP', 'FMSP', 'VEHI']
        self.label_refits_disallowed = []
        self.default_cargos = global_constants.default_cargos['supplies']
        # !! flipping not currently allowed as don't know if asymmetric sprites support is working (might be fine?)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(heavy_items=True)


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
        self.buy_cost_adjustment_factor = 1.2
        # allow flipping, used to flip company colour
        self.allow_flip = True
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
        self.buy_cost_adjustment_factor = 1.2


class Train(object):
    """Base class for all types of trains"""

    def __init__(self, **kwargs):
        self.consist = kwargs.get('consist')

        # setup properties for this train
        self.numeric_id = kwargs.get('numeric_id', None)
        self.vehicle_length = kwargs.get('vehicle_length', None)
        self._weight = kwargs.get('weight', None)
        self.capacity = kwargs.get('capacity', 0)
        self.loading_speed_multiplier = kwargs.get(
            'loading_speed_multiplier', 1)
        # spriterow_num allows assigning sprites for multi-part vehicles, and is not supported in all vehicle templates (by design - TMWFTLB to support)
        self.spriterow_num = kwargs.get('spriterow_num', 0) # first row = 0;
        # sometimes we want to offset the buy menu spriterow (!! this is incomplete hax, not supported by generated buy menu sprites etc)
        self.buy_menu_spriterow_num = 0 # set in the subclass as needed, (or extend to kwargs in future)
        # !! the need to copy cargo refits from the consist is probably historical (mixed cargo articulated trains), and could likely be refactored !!
        self.class_refit_groups = self.consist.class_refit_groups
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.autorefit = True
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
        if not self.always_use_same_spriterow:
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

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " +
                                   i + " which is not defined in the cargo table")

    def render(self):
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


class DieselRailcarBaseUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to set symmetry.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # the cab magic won't work unless it's asymmetric eh? :)
        self._symmetry_type = kwargs.get('symmetry_type', 'asymmetric')


class DieselRailcarMailUnit(DieselRailcarBaseUnit):
    """
    Unit for a mail diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (kwargs['vehicle_length'] * base_capacity) / polar_fox.constants.mail_multiplier


class DieselRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = kwargs['vehicle_length'] * base_capacity


class ElectricEngineUnit(Train):
    """
    Unit for an electric engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
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
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'
        self.consist.visual_effect_override_by_railtype = {
            'ELRL': 'VISUAL_EFFECT_ELECTRIC'}
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
        self.capacity = (kwargs['vehicle_length'] * base_capacity) / polar_fox.constants.mail_multiplier


class ElectroDieselRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = kwargs['vehicle_length'] * base_capacity


class ElectricRailcarBaseUnit(Train):
    """
    Unit for an electric railcar.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_ELECTRIC'
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2 # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = 2 # frankly hax at this point :|
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = 'asymmetric'


class ElectricRailcarMailUnit(ElectricRailcarBaseUnit):
    """
    Unit for a mail electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = (kwargs['vehicle_length'] * base_capacity) / polar_fox.constants.mail_multiplier


class ElectricRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        self.capacity = kwargs['vehicle_length'] * base_capacity


class ElectricHighSpeedPaxUnit(Train):
    """
    Unit for high-speed, high-power pax electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist.requires_electric_rails = True
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'
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
            self.capacity = int(kwargs['vehicle_length'] * base_capacity * 0.875)


class MetroUnit(Train):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs['consist'].base_track_type = 'METRO'
        self.loading_speed_multiplier = 2
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'
        self.consist.str_name_suffix = 'STR_NAME_SUFFIX_METRO'
        # the cab magic won't work unless it's asymmetrical eh? :P
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
        # most wagons are symmetric, over-ride per vehicle or subclass as needed
        self._symmetry_type = kwargs.get('symmetry_type', 'symmetric')

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
        self.capacity = (kwargs['vehicle_length'] * base_capacity) / polar_fox.constants.mail_multiplier


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
        self.capacity = kwargs['vehicle_length'] * base_capacity


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
        self.capacity = int(kwargs['vehicle_length'] * base_capacity * 0.625)


class ExpressCar(TrainCar):
    """
    Express freight wagon.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[self.consist.base_track_type][self.consist.gen - 1]
        # we nerf down express car capacity to same as mail cars, to account for them being faster
        self.capacity = (kwargs['vehicle_length'] * base_capacity) / polar_fox.constants.mail_multiplier


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
        self.capacity = (kwargs['vehicle_length'] * base_capacity)


class WellCar(FreightCar):
    """
    Well Car. This subclass only exists to set symmetry_type to asymmetric.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # well cars may be asymmetric, there is magic in the graphics processing to make cargo sprites work with this
        self._symmetry_type = 'asymmetric'

