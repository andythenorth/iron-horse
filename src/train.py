import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import math
import random

# python builtin templater might be used in some utility cases
from string import Template

import polar_fox
import global_constants  # expose all constants for easy passing to templates
import utils

from gestalt_graphics.gestalt_graphics import (
    GestaltGraphics,
    GestaltGraphicsVisibleCargo,
    GestaltGraphicsBoxCarOpeningDoors,
    GestaltGraphicsEngine,
    GestaltGraphicsCaboose,
    GestaltGraphicsSimpleBodyColourRemaps,
    GestaltGraphicsRandomisedWagon,
    GestaltGraphicsConsistPositionDependent,
    GestaltGraphicsIntermodalContainerTransporters,
    GestaltGraphicsAutomobilesTransporter,
    GestaltGraphicsCustom,
)
import gestalt_graphics.graphics_constants as graphics_constants

import iron_horse
import spritelayer_cargos


class Consist(object):
    """
    'Vehicles' (appearing in buy menu) are composed as articulated consists.
    Each consist comprises one or more 'units' (visible).
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        # private var, used to store a name substr for engines, composed into name with other strings as needed
        self._name = kwargs.get("name", None)
        self.base_numeric_id = kwargs.get("base_numeric_id", None)
        # roster is set when the vehicle is registered to a roster, only one roster per vehicle
        # persist roster id for lookups, not roster obj directly, because of multiprocessing problems with object references
        self.roster_id = kwargs.get("roster_id")  # just fail if there's no roster
        # create a structure to hold buyable variants - the method can be over-ridden in consist subclasses to provide specific rules for buyable variants
        # we start empty, and rely on add_unit to populate this later, which means we can rely on gestalt_graphics having been initialised
        # otherwise we're trying to initialise variants before we have gestalt_graphics, and that's a sequencing problem
        self.buyable_variants = []
        # create a structure to hold the units
        self.units = []
        # either gen xor intro_year is required, don't set both, one will be interpolated from the other
        self._intro_year = kwargs.get("intro_year", None)
        self._gen = kwargs.get("gen", None)
        # if gen is used, the calculated intro year can be adjusted with +ve or -ve offset
        self.intro_year_offset = kwargs.get("intro_year_offset", None)
        # used for synchronising / desynchronising intro dates for groups vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147
        self._intro_year_days_offset = (
            None  # defined in subclasses, no need for instances to define this
        )
        self._vehicle_life = kwargs.get("vehicle_life", None)
        #  most consists are automatically replaced by the next consist in the role tree
        # ocasionally we need to merge two branches of the role, in this case set replacement consist id
        self._replacement_consist_id = kwargs.get("replacement_consist_id", None)
        # default loading speed multiplier, over-ride in subclasses as needed
        self._loading_speed_multiplier = 1
        self.base_track_type_name = kwargs.get("base_track_type_name", "RAIL")
        # modify base_track_type_name for electric engines when writing out the actual rail type
        # without this, RAIL and ELRL have to be specially handled whenever a list of compatible consists is wanted
        self.tractive_effort_coefficient = kwargs.get(
            "tractive_effort_coefficient", 0.3
        )  # 0.3 is recommended default value
        # private var, can be used to over-rides default (per generation, per class) speed
        self._speed = kwargs.get("speed", None)
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_power_source = kwargs.get("power_by_power_source", None)
        # some engines require pantograph sprites composited, don't bother setting this unless required
        self.pantograph_type = kwargs.get("pantograph_type", None)
        self.dual_headed = kwargs.get("dual_headed", False)
        self.tilt_bonus = False  # over-ride in subclass as needed
        self.lgv_capable = False  # over-ride in subclass as needed
        self.requires_high_clearance = kwargs.get("requires_high_clearance", False)
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        self.buy_menu_hint_wagons_add_power = False
        # wagons can be candidates for the magic randomised wagons
        # this is on Consist not CarConsist as we need to check it when determining order for all consists
        self.randomised_candidate_groups = []
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        self.easter_egg_haulage_speed_bonus = kwargs.get(
            "easter_egg_haulage_speed_bonus", False
        )
        # engines will automatically detemine role string, but to force it on certain coach/wagon types use _buy_menu_role_string
        self._buy_menu_role_string = None
        # simple buy menu hint flag for driving cabs
        self.buy_menu_hint_driving_cab = False
        # simple buy menu hint flag for restaurant cars
        self.buy_menu_hint_restaurant_car = False
        # option to force a specific name suffix, if the auto-detected ones aren't appropriate
        self._str_name_suffix = None
        # random_reverse means (1) randomised reversing of sprites when vehicle is built (2) player can also flip vehicle
        # random_reverse is not supported in some templates
        self.random_reverse = kwargs.get("random_reverse", False)
        # random_reverse vehicles can always be flipped, but flip can also be set in other cases (by subclass, or directly by consist)
        self.allow_flip = kwargs.get("allow_flip", self.random_reverse)
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
        self.fixed_run_cost_points = 30  # default, over-ride in subclass as needed
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
        self.role = kwargs.get("role", None)
        # role child branch num places this vehicle on a specific child branch of the tech tree, where the role is the parent branch
        # 1..n for branches with calculated replacements, -1..-n for jokers which are not automatically replaced in the tree, 0 reserved
        self.role_child_branch_num = kwargs.get("role_child_branch_num", 0)
        # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        self.suppress_animated_pixel_warnings = kwargs.get(
            "suppress_animated_pixel_warnings", False
        )
        # extended description (and a cite from a made up person) for docs etc
        self.description = """"""  # to be set per vehicle, multi-line supported
        self._cite = ""  # optional, set per subclass as needed
        # for 'inspired by' stuff
        self.foamer_facts = """"""  # to be set per vehicle, multi-line supported
        # occasionally we want to force a specific spriterow for docs, not needed often, set in kwargs as needed, see also buy_menu_spriterow_num
        self.docs_image_spriterow = kwargs.get(
            "docs_image_spriterow", 0
        )  # 0 indexed spriterows, position in generated spritesheet
        # aids 'project management'
        self.sprites_complete = kwargs.get("sprites_complete", False)

    def resolve_buyable_variants(self):
        # this method can be over-ridden per consist subclass as needed
        # the basic form of buyable variants is driven by liveries
        for livery in self.gestalt_graphics.all_liveries:
            # we don't need to know the actual livery here, we rely on matching them up later by indexes, which is fine
            self.buyable_variants.append(BuyableVariant(self, livery=livery))

    def add_unit(self, type, repeat=1, **kwargs):
        # we have add_unit create the variants when needed, which means we avoid sequencing problems with gestalt_graphics initialisation
        if len(self.buyable_variants) == 0:
            self.resolve_buyable_variants()
        # now add the units
        unit = type(consist=self, **kwargs)
        for repeat_num in range(repeat):
            self.units.append(unit)
        # append the unit variants after adding the unit to consist.units, as we want to be able to simply increment numeric IDs based on the number of units added so far
        for buyable_variant in self.buyable_variants:
            unit.unit_variants.append(UnitVariant(unit, buyable_variant))

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
    def unique_numeric_ids(self):
        # all the numeric_ids used for all the variants of all the units
        result = []
        for unit in self.unique_units:
            for unit_variant in unit.unit_variants:
                result.append(unit_variant.numeric_id)
        return result

    @property
    def lead_unit_variants_numeric_ids(self):
        # convenience function
        result = [
            unit_variant.numeric_id for unit_variant in self.units[0].unit_variants
        ]
        return result

    @property
    def unique_spriterow_nums(self):
        # find the unique spriterow numbers, used in graphics generation
        result = []
        for unit in set([unit.spriterow_num for unit in self.units]):
            result.append(unit)
            # extend with alternative cc livery if present, spritesheet format assumes unit_1_default, unit_1_additional_liveries, unit_2_default, unit_2_additional_liveries if present
            if self.gestalt_graphics.additional_liveries is not None:
                result.append(unit + 1)
        return result

    @property
    def reversed_variants(self):
        # Handles 'unreversed' and optional 'reversed' variant, which if provided, will be chosen at random per consist
        # NOT the same as 'flipped' which is a player choice in-game, and handled separately
        # Previous model_variant approach for this was deprecated March 2018, needlessly complicated
        result = ["unreversed"]
        if self.random_reverse:
            result.append("reversed")
        return result

    @property
    def str_name_suffix(self):
        if getattr(self, "_str_name_suffix", None) is not None:
            return self._str_name_suffix
        else:
            if self.power_by_power_source is not None:
                if len(self.power_by_power_source) == 1:
                    if "NULL" in self.power_by_power_source:
                        return None
                    elif "METRO" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_METRO"
                    elif "DIESEL" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_DIESEL"
                    elif "BATTERY_HYBRID" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_BATTERY_HYBRID"
                    elif "STEAM" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_STEAM"
                    elif "AC" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_ELECTRIC_AC"
                    elif "DC" in self.power_by_power_source:
                        return "STR_NAME_SUFFIX_ELECTRIC_DC"
                if len(self.power_by_power_source) == 2:
                    if (
                        "DIESEL" in self.power_by_power_source
                        and "AC" in self.power_by_power_source
                    ):
                        return "STR_NAME_SUFFIX_ELECTRODIESEL"
                    if (
                        "AC" in self.power_by_power_source
                        and "DC" in self.power_by_power_source
                    ):
                        return "STR_NAME_SUFFIX_ELECTRIC_AC_DC"
            return None

    @property
    def name(self):
        if self.str_name_suffix is not None:
            return "string(STR_NAME_CONSIST_PARENTHESES, string({a}), string({b}), string({c}))".format(
                a="STR_NAME_" + self.id,
                b=self.str_name_suffix,
                c="STR_EMPTY",
            )
        else:
            return "string(STR_NAME_" + self.id + ")"

    def engine_varies_power_by_power_source(self, vehicle):
        if self.power_by_power_source is not None and vehicle.is_lead_unit_of_consist:
            if len(self.power_by_power_source) > 1:
                # as of Dec 2018, can't use both variable power and wagon power
                # that could be changed if https://github.com/OpenTTD/OpenTTD/pull/7000 is done
                # would require quite a bit of refactoring though eh
                assert self.wagons_add_power == False, (
                    "%s consist has both engine_varies_power_by_power_source and power_by_power_source, which conflict"
                    % self.id
                )
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
    def intro_year(self):
        # automatic intro_year, but can over-ride by passing in kwargs for consist
        if self._intro_year:
            assert self._gen == None, (
                "%s consist has both gen and intro_year set, which is incorrect"
                % self.id
            )
            assert self.intro_year_offset == None, (
                "%s consist has both intro_year and intro_year_offset set, which is incorrect"
                % self.id
            )
            return self._intro_year
        else:
            assert self._gen != None, (
                "%s consist has neither gen nor intro_year set, which is incorrect"
                % self.id
            )
            result = self.roster.intro_years[self.base_track_type_name][self.gen - 1]
            if self.intro_year_offset is not None:
                result = result + self.intro_year_offset
            return result

    @property
    def intro_date_months_offset(self):
        # days offset is used to control *synchronising* (or not) intro dates across groups of vehicles where needed
        # see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        if self.gen == 1:
            # to ensure a fully playable roster is available for gen 1, force the days offset to 0
            # for explanation see https://www.tt-forums.net/viewtopic.php?f=26&t=68616&start=460#p1224299
            return 0
        elif self._intro_year_days_offset is not None:
            # offset defined in class (probably a wagon)
            return self._intro_year_days_offset
        else:
            for role_group, roles in global_constants.role_group_mapping.items():
                if self.role in roles:
                    group_key = role_group
                    continue
            if group_key in ["express", "freight"]:
                # assume that we want child branch 1 to be grouped as 'core' in some cases
                # !! not convinced this achieves much as of July 2022 but eh
                if self.role_child_branch_num == 1:
                    group_key = group_key + "_core"
                else:
                    group_key = group_key + "_non_core"
            result = global_constants.intro_month_offsets_by_role_group[group_key]
            if self.joker:
                # force jokers away from vehicles in same role group
                # if further variation is wanted, give the joker a different intro year, automating that isn't wise
                result = min(result + 6, 11)
        return result

    @property
    def gen(self):
        # gen is usually set in the vehicle, but can be left unset if intro_year is set
        if self._gen:
            assert self._intro_year == None, (
                "%s consist has both gen and intro_year set, which is incorrect"
                % self.id
            )
            return self._gen
        else:
            assert self._intro_year != None, (
                "%s consist has neither gen nor intro_year set, which is incorrect"
                % self.id
            )
            for gen_counter, intro_year in enumerate(
                self.roster.intro_years[self.base_track_type_name]
            ):
                if self.intro_year < intro_year:
                    return gen_counter
            # if no result is found in list, it's last gen
            return len(self.roster.intro_years[self.base_track_type_name])

    @property
    def equivalent_ids_alt_var_41(self):
        # only implemented in subclasses that require it - easiest thing when writing it, change if needed
        return None

    @property
    def replacement_consist(self):
        # option exists to force a replacement consist, this is used to merge tech tree branches
        if self._replacement_consist_id is not None:
            for consist in self.roster.engine_consists:
                if consist.id == self._replacement_consist_id:
                    return consist
            # if we don't return a valid result, that's an error, probably a broken replacement id
            raise Exception(
                "replacement consist id "
                + self._replacement_consist_id
                + " not found for consist "
                + self.id
            )
        else:
            similar_consists = []
            replacement_consist = None
            for consist in self.roster.engine_consists:
                if (
                    (consist.role == self.role)
                    and (consist.role_child_branch_num == self.role_child_branch_num)
                    and (consist.base_track_type_name == self.base_track_type_name)
                ):
                    similar_consists.append(consist)
            for consist in sorted(
                similar_consists, key=lambda consist: consist.intro_year
            ):
                if consist.intro_year > self.intro_year:
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
            if (
                (consist.base_track_type_name == self.base_track_type_name)
                and (consist.gen == self.gen)
                and (consist != self)
            ):
                if (
                    (consist.role == self.role)
                    or (0 <= (consist.power - self.power) < 500)
                    or (0 <= (self.power - consist.power) < 500)
                ):
                    result.append(consist)
        return result

    @property
    def vehicle_life(self):
        if self._vehicle_life is not None:
            # allow vehicles to provide a vehicle life if they want
            return self._vehicle_life
        elif self.replacement_consist is not None:
            time_to_replacement = self.replacement_consist.intro_year - self.intro_year
            if time_to_replacement > 40:
                # round to nearest 10, then add some padding
                return time_to_replacement - (time_to_replacement % 10) + 10
            else:
                return 40
        else:
            # pick a sensible value for vehicles that don't otherwise get replaced
            return 40

    @property
    def model_life(self):
        if self.replacement_consist is None:
            return "VEHICLE_NEVER_EXPIRES"
        else:
            return self.replacement_consist.intro_year - self.intro_year

    @property
    def retire_early(self):
        # affects when vehicle is removed from buy menu (in combination with model life)
        # to understand why this is needed see https://newgrf-specs.tt-wiki.net/wiki/NML:Vehicles#Engine_life_cycle
        # retire at end of model life + 10 (fudge factor - no need to be more precise than that)
        return -10

    @property
    def track_type_name(self):
        if self.requires_electric_rails:
            result = (
                self.base_track_type_name + "_ELECTRIFIED_" + self.electrification_type
            )
        else:
            result = self.base_track_type_name
        return result

    @property
    def track_type(self):
        # are you sure you don't want base_track_type_name instead? (generally you do want base_track_type_name)
        # track_type maps base_track_type_name and modifiers to an actual railtype label
        # this is done by looking up a railtype mapping in global constants, via internal labels
        # e.g. electric engines with "RAIL" as base_track_type_name will be translated to "ELRL"
        # narrow gauge trains will be similarly have "NG" translated to an appropriate NG railytpe label
        valid_railtype_labels = (
            global_constants.railtype_labels_by_vehicle_track_type_name[
                self.track_type_name
            ]
        )
        # assume that the label we want for the vehicle is the first in the list of valid types (the rest are fallbacks if the first railtype is missing)
        result = valid_railtype_labels[0]
        # set modifiers on the label by modifying the last byte
        # modifiers are not orthogonal and the byte can only be set to a single value
        # if multiple modifiers need to be combined, that needs to be explicitly handled
        # generally that would be a sign we're doing something unwise and with combinatorial problems
        modifier = "_"
        if self.lgv_capable:
            modifier = "A"
        elif self.requires_high_clearance:
            print(self.id, " has requires_high_clearance set - needs cleared")
            modifier = "B"
        result = result[0:3] + modifier
        return result

    @property
    def vehicle_power_source_tree(self):
        # return a structure for easy rendering of the variable power switch chain
        result = []
        if self.power_by_power_source is None:
            return result
        # extend this as necessary for different power sources, there's no magic pattern, it's manually declared mappings
        # NOTE that order is explicit - and assumes that power hierarchy is AC > DC > DIESEL
        # iff that assumption is wrong, result can be lambda sorted by actual vehicle power amounts before returning, but not necessary as of July 2022
        if "AC" in self.power_by_power_source.keys():
            result.append(["AC", self.base_track_type_name + "_ELECTRIFIED_AC"])
        if "DC" in self.power_by_power_source.keys():
            result.append(["DC", self.base_track_type_name + "_ELECTRIFIED_DC"])
        if "DIESEL" in self.power_by_power_source.keys():
            result.append(["DIESEL", self.base_track_type_name])
        if "STEAM" in self.power_by_power_source.keys():
            result.append(["STEAM", self.base_track_type_name])
        # now append suffixes for switches - self and next, could be done in the template, but it's just neater to do here
        for counter, value in enumerate(result):
            value.append(counter)
            if counter == len(result) - 1:
                # no suffix for the last one
                value.append(None)
            else:
                value.append(counter + 1)
        # reverse order as switch chain is actually rendered in the templating as lowest -> highest
        result.reverse()
        return result

    @property
    def requires_electric_rails(self):
        if self.power_by_power_source is None:
            return False
        for power_source_name in self.power_by_power_source.keys():
            if power_source_name not in ["AC", "DC"]:
                # add any electric types here (not metro though)
                return False
        return True

    @property
    def electrification_type(self):
        if "AC" in self.power_by_power_source:
            # handle multi-system first
            if "DC" in self.power_by_power_source:
                return "AC_DC"
            else:
                return "AC"
        elif "DC" in self.power_by_power_source:
            return "DC"
        else:
            raise BaseException(
                "no valid electrification type found for "
                + self.id
                + " - is it an electrified vehicle?"
            )

    @property
    def power(self):
        if self.power_by_power_source == None:
            # probably a wagon eh?
            return 0
        else:
            # this is to get the default value, used when only one value can be shown
            # cascade in controlled order through the available power sources
            if "NULL" in self.power_by_power_source:
                # null is used for e.g. snowploughs etc where the power is only to enable the vehicle to lead the train
                return self.power_by_power_source["NULL"]
            if "STEAM" in self.power_by_power_source:
                return self.power_by_power_source["STEAM"]
            elif "DIESEL" in self.power_by_power_source:
                return self.power_by_power_source["DIESEL"]
            elif "BATTERY_HYBRID" in self.power_by_power_source:
                return self.power_by_power_source["BATTERY_HYBRID"]
            elif "METRO" in self.power_by_power_source:
                return self.power_by_power_source["METRO"]
            elif "AC" in self.power_by_power_source:
                # AC is the default for multi-system AC/DC locos
                return self.power_by_power_source["AC"]
            elif "DC" in self.power_by_power_source:
                return self.power_by_power_source["DC"]
            else:
                raise BaseException(
                    "no valid power source found when fetching default power for "
                    + self.id
                    + " - possibly power source check needs extending?"
                )

    def get_speed_by_class(self, speed_class):
        # automatic speed, but can over-ride by passing in kwargs for consist
        speeds_by_track_type = self.roster.speeds[self.base_track_type_name]
        return speeds_by_track_type[speed_class][self.gen - 1]

    @property
    def speed(self):
        if self._speed:
            return self._speed
        elif getattr(self, "speed_class", None):
            # speed by class, if speed_class is set explicitly (and not None)
            # !! this doesn't handle RAIL / ELRL correctly
            # could be fixed by checking a list of railtypes
            return self.get_speed_by_class(self.speed_class)
        elif self.role:
            # first check for express roles, which are determined by multiple role groups
            for role_group_mapping_key in [
                "express",
                "driving_cab",
                "express_railcar",
                "high_power_railcar",
            ]:
                group_roles = global_constants.role_group_mapping[
                    role_group_mapping_key
                ]
                if self.role in group_roles:
                    return self.get_speed_by_class("express")
            # then check other specific roles
            if self.role in ["mail_railcar", "pax_railcar"]:
                return self.get_speed_by_class("suburban")
            elif self.role in ["hst"]:
                return self.get_speed_by_class("hst")
            elif self.role in ["very_high_speed"]:
                return self.get_speed_by_class("very_high_speed")
            else:
                return self.get_speed_by_class("standard")
        else:
            # assume no speed limit
            return None

    @property
    def speed_on_lgv(self):
        if not self.lgv_capable:
            raise Exception(
                self.id, "is not lgv capable, but is attempting to set speed on lgv"
            )

        # mildly JDFI hacky
        if self.role in ["hst"]:
            return self.get_speed_by_class("hst_on_lgv")
        elif self.role in ["very_high_speed"]:
            return self.get_speed_by_class("very_high_speed_on_lgv")
        else:
            return self.get_speed_by_class(self.speed_class + "_on_lgv")

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
        return sum([getattr(unit, "weight", 0) for unit in self.units])

    @property
    def length(self):
        # total length of the consist
        return sum([unit.vehicle_length for unit in self.units])

    @property
    def loading_speed_multiplier(self):
        # over-ride in subclass as needed
        return self._loading_speed_multiplier

    @property
    def hide_in_wagons_only_mode(self):
        # wagons-only mode excludes all engines, and selected other vehicles
        # all engines have power, all true wagons don't
        if self.power > 0:
            return True
        elif self.wagons_add_power:
            return True
        else:
            return False

    @property
    def is_randomised_wagon(self):
        # this shorthand to avoid looking up the classname directly for a couple of special cases
        return (
            self.gestalt_graphics.__class__.__name__ == "GestaltGraphicsRandomisedWagon"
        )

    @property
    def is_caboose(self):
        # this shorthand to avoid looking up the classname directly for a couple of special cases
        return self.gestalt_graphics.__class__.__name__ == "GestaltGraphicsCaboose"

    @property
    def roster(self):
        return iron_horse.roster_manager.get_roster_by_id(self.roster_id)

    def get_expression_for_availability(self):
        result = []
        if self.joker:
            result.append("param_simplified_gameplay==0")
        if self.hide_in_wagons_only_mode:
            result.append("param_wagons_only_mode==0")
        # a hack to make this check work now that roster is removed, for the non-joker case, with no other condition to match
        result.append("1")
        return " && ".join(result)

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
                result = 'cargotype_available("' + cargo + '")?' + cargo + ":" + result
            return result

    def nml_expression_for_vehicle_is_electrically_powered_by_tile(self):
        result = []
        if self.power_by_power_source is not None:
            # multisystem support
            for electrification_type in ["AC", "DC"]:
                if electrification_type in self.power_by_power_source:
                    result.append(
                        "tile_powers_track_type_name_"
                        + self.base_track_type_name
                        + "_ELECTRIFIED_"
                        + electrification_type
                        + "()"
                    )
                    # note that this is JFDI and expects the base_track_type_name to NOT be LGV, refactor approach if that's a problem
                    if self.lgv_capable:
                        result.append(
                            "tile_powers_track_type_name_"
                            + "LGV_ELECTRIFIED_"
                            + electrification_type
                            + "()"
                        )
        else:
            # otherwise use the electrification type already known by the consist
            result.append(
                "tile_powers_track_type_name_"
                + self.base_track_type_name
                + "_ELECTRIFIED_"
                + self.electrification_type
                + "()"
            )
        result = " || ".join(result)
        result = "[" + result + "]"
        return result

    @property
    def buy_menu_x_loc(self):
        # automatic buy menu sprite if single-unit consist
        # extend this to check an auto_buy_menu_sprite property if manual over-rides are needed in future
        if len(self.units) > 1:
            # custom buy menu sprite for articulated vehicles
            return 360
        elif self.is_randomised_wagon or self.is_caboose:
            # possibly fragile class name check, but eh
            return 360
        else:
            # default to just using 6th angle of vehicle
            return global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[6][
                0
            ]

    @property
    def buy_menu_width(self):
        # max sensible width in buy menu is 64px
        # the +1 for buffers etc is added in the template
        calculated_buy_menu_width = (
            4 * self.length + self.gestalt_graphics.buy_menu_width_addition
        )
        if calculated_buy_menu_width < 64:
            return calculated_buy_menu_width
        else:
            return 64

    @property
    def num_sprite_layers(self):
        # always at least one layer
        result = 1
        # order of adding extra layers doesn't matter here, it's just a number,
        # the switch chain for the vehicle type will need to take care of switching to correct layers
        # gestalt may add extra sprites layer for e.g. visible cargo, vehicle masks
        if (
            getattr(
                self.gestalt_graphics, "num_extra_layers_for_spritelayer_cargos", None
            )
            != None
        ):
            result = (
                result + self.gestalt_graphics.num_extra_layers_for_spritelayer_cargos
            )
        # add a layer for a masked overlay as needed (usually applied over cargo sprites)
        if self.gestalt_graphics.add_masked_overlay:
            result = result + 1
        # add a layer for pantographs as needed, note this is not done in the gestalt as it's more convenient to treat separarely
        if self.pantograph_type is not None:
            result = result + 1
        # OpenTTD has a limited number of layers in the sprite stack, we can't exceed them
        if result > 8:
            raise Exception("Too many sprite layers ", result, " defined for ", self.id)
        return result

    def get_nml_for_spriteset_template(self, y_offset):
        template_subtype = "dual_headed" if self.dual_headed else "default"
        args = []
        args.append(self.buy_menu_x_loc)
        args.append(10 + y_offset)
        args.append(1 + self.buy_menu_width)  # add 1 to account for buffers / couplers
        args.append(-1 * int(self.buy_menu_width / 2))  # x_offset
        args.append("ANIM" if self.suppress_animated_pixel_warnings else "NOANIM")
        return (
            "spriteset_template_purchase_"
            + template_subtype
            + "("
            + ",".join([str(arg) for arg in args])
            + ")"
        )

    def get_buy_menu_format(self, vehicle):
        # keep the template logic simple, present strings for a switch/case tree
        # variable_power and wagons_add_power are mutually exclusive (asserted by engine_varies_power_by_power_source as of August 2019)
        if self.engine_varies_power_by_power_source(vehicle):
            return "variable_power"
        elif self.lgv_capable:
            # yeah, simplicity failed when lgv_capable was added, this simple tree needs rethought to allow better composition of arbitrary strings
            if self.buy_menu_hint_wagons_add_power:
                return "lgv_capable_and_wagons_add_power"
            else:
                return "lgv_capable"
        elif self.buy_menu_hint_driving_cab:
            return "driving_cab"
        elif self.buy_menu_hint_restaurant_car:
            return "restaurant_car"
        else:
            return "default"

    def get_buy_menu_string(self, vehicle):
        result = []
        # optional string if engine varies power by railtype
        if self.engine_varies_power_by_power_source(vehicle):
            if len(self.power_by_power_source) == 2:
                result.append("STR_POWER_BY_POWER_SOURCE_TWO_SOURCES")
            elif len(self.power_by_power_source) == 3:
                result.append("STR_POWER_BY_POWER_SOURCE_THREE_SOURCES")
            else:
                print("CABBAGE", self.id)
                # raise BaseException("consist " + self.id + " defines unsupported number of power sources")
        # optional string if consist is lgv-capable
        if self.lgv_capable:
            result.append("STR_SPEED_BY_RAILTYPE_LGV_CAPABLE")
        # optional string if dedicated wagons add power
        if self.buy_menu_hint_wagons_add_power:
            result.append(self.buy_menu_distributed_power_substring)

        # engines will always show a role string
        # !! this try/except is all wrong, I just want to JFDI to add buy menu strings to wagons which previously didn't support them, and can do regret later
        # !! this may not be used / or required as of April 2021 - _buy_menu_role_string is available instead
        try:
            result.append(self.buy_menu_role_string)
        except:
            pass

        # some wagons (mostly railcar trailers and pax coaches) might want to show an optional role string
        if self._buy_menu_role_string is not None:
            result.append("STR_ROLE, string(" + self._buy_menu_role_string + ")")

        # driving cab hint comes after role string
        if self.buy_menu_hint_driving_cab:
            result.append("STR_BUY_MENU_HINT_DRIVING_CAB")

        # driving cab hint comes after role string
        if self.buy_menu_hint_restaurant_car:
            result.append("STR_BUY_MENU_HINT_RESTAURANT_CAR")

        if len(result) == 1:
            return "STR_BUY_MENU_WRAPPER_ONE_SUBSTR, string(" + result[0] + ")"
        if len(result) == 2:
            return (
                "STR_BUY_MENU_WRAPPER_TWO_SUBSTR, string("
                + result[0]
                + "), string("
                + result[1]
                + ")"
            )
        if len(result) == 3:
            return (
                "STR_BUY_MENU_WRAPPER_THREE_SUBSTR, string("
                + result[0]
                + "), string("
                + result[1]
                + "), string("
                + result[2]
                + ")"
            )
        # should never be reached, extend this if we do
        raise Exception("Unsupported number of buy menu strings for ", self.id)

    @property
    def buy_menu_role_string(self):
        for role_group, roles in global_constants.role_group_mapping.items():
            if self.role in roles:
                return (
                    "STR_ROLE, string("
                    + global_constants.role_string_mapping[role_group]
                    + ")"
                )
        raise Exception("no role string found for ", self.id)

    @property
    def cite(self):
        # this assumes that NG and Metro always return the same, irrespective of consist cite
        # that makes sense for Pony roster, but might not work in other rosters, deal with that if it comes up eh?
        # don't like how much content (text) is in code here, but eh
        if self.base_track_type_name == "NG":
            cite_name = "Roberto Flange"
            cite_titles = [
                "Narrow Gauge Superintendent",
                "Works Manager (Narrow Gauge)",
                "Traction Controller, Narrow Gauge Lines",
            ]
        elif self.base_track_type_name == "METRO":
            cite_name = "JJ Transit"
            cite_titles = [
                "Superintendent (Metro Division)",
                "Chief Engineer, Mass Mobility Systems",
            ]
        else:
            if self._cite == "Arabella Unit":
                cite_name = self._cite
                cite_titles = [
                    "General Manager (Railcars)",
                    "Senior Engineer, Self-Propelled Traction",
                    "Director, Suburban and Rural Lines",
                ]
            elif self._cite == "Dr Constance Speed":
                cite_name = self._cite
                cite_titles = [
                    "Lead Engineer, High Speed Projects",
                    "Director, Future Traction Concepts",
                ]
            else:
                cite_name = "Mr Train"
                cite_titles = [
                    "Acting Superintendent of Engines",
                    "Provisional Chief Engineer",
                    "Interim Head of Works",
                    "Transitional General Manager (Traction)",
                ]
        return cite_name + ", " + random.choice(cite_titles)

    def render_articulated_switch(self, templates):
        template = templates["articulated_parts.pynml"]
        nml_result = template(
            consist=self,
            global_constants=global_constants,
        )
        return nml_result

    def freeze_cross_roster_lookups(self):
        # graphics processing can't depend on roster object reliably, as it blows up multiprocessing (can't pickle roster), for reasons I never figured out
        # this freezes any necessary roster items in place
        self.frozen_roster_items = {}
        if self.is_randomised_wagon:
            self.frozen_roster_items[
                "wagon_randomisation_candidates"
            ] = self.roster.get_wagon_randomisation_candidates(self)
        # no return

    def assert_speed(self):
        # speed is assumed to be limited to 200mph
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.speed is not None:
            if self.speed > 200:
                utils.echo_message(
                    "Consist " + self.id + " has speed > 200, which is too much"
                )

    def assert_power(self):
        # power is assumed to be limited to 10,000hp
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.speed is not None:
            if self.power > 10000:
                utils.echo_message(
                    "Consist " + self.id + " has power > 10000hp, which is too much"
                )

    def assert_weight(self):
        # weight is assumed to be limited to 500t
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.weight is not None:
            if self.weight > 500:
                utils.echo_message(
                    "Consist " + self.id + " has weight > 500t, which is too much"
                )

    def assert_description_foamer_facts(self):
        # if these are too noisy, comment them out temporarily
        if self.power > 0:
            if len(self.description) == 0:
                utils.echo_message("Consist " + self.id + " has no description")
            if len(self.foamer_facts) == 0:
                utils.echo_message("Consist " + self.id + " has no foamer_facts")
            if "." in self.foamer_facts:
                utils.echo_message(
                    "Consist " + self.id + " foamer_facts has a '.' in it."
                )

    def render(self, templates, graphics_path):
        self.assert_speed()
        self.assert_power()
        # templating
        nml_result = ""
        if len(self.units) > 1:
            nml_result = nml_result + self.render_articulated_switch(templates)
        for unit in self.unique_units:
            nml_result = nml_result + unit.render(templates, graphics_path)
        return nml_result


class EngineConsist(Consist):
    """
    Standard engines (without passenger or cargo capacity).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # arbitrary multiplier to floating run costs (factors are speed, power, weight)
        # adjust per subtype as needed
        self.floating_run_cost_multiplier = 8.5
        # fixed (baseline) run costs on this subtype, or more rarely instances can over-ride this
        self.fixed_run_cost_points = kwargs.get("fixed_run_cost_points", 180)
        # pax/mail cars will default to the alternative 2nd livery automatically using role and branch, or it can be forced here (set in engines as needed)
        # (player can always invert the choice by flipping vehicles)
        self.force_default_pax_mail_livery = kwargs.get(
            "force_default_pax_mail_livery", None
        )
        # optionally force a specific caboose family to be used
        self._caboose_family = kwargs.get("caboose_family", None)
        # Graphics configuration only as required
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        self.gestalt_graphics = GestaltGraphicsEngine(
            pantograph_type=self.pantograph_type,
            additional_liveries=self.roster.get_liveries_by_name(
                kwargs.get("additional_liveries", [])
            ),
            default_livery_extra_docs_examples=kwargs.get(
                "default_livery_extra_docs_examples", []
            ),
        )

    @property
    def caboose_family(self):
        # caboose families are used to match engines to caboose variants
        # can be forced on a per engine basis
        # otherwise use default for base track type and vehicle gen
        if self._caboose_family is not None:
            return self._caboose_family
        else:
            return "default_" + str(self.gen)

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
            power_factor = (
                self.electro_diesel_buy_cost_malus
                * self.power_by_power_source["AC"]  # !! assumption of AC !!
            ) / 750
        # multiplier for non-electric power, max value will be 10
        else:
            power_factor = self.power / 1000
        # basic cost from speed, power, subclass factor (e.g. engine with pax capacity might cost more to buy)
        buy_cost_points = (
            speed_cost_points * power_factor * self.buy_cost_adjustment_factor
        )
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
        is_NG = True if self.base_track_type_name == "NG" else False
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
            if "railcar" in self.role:
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
        floating_run_cost_points = (
            floating_run_cost_points * self.floating_run_cost_multiplier
        )
        fixed_run_cost_points = self.fixed_run_cost_points
        # add floating cost to the fixed (baseline) cost (which is arbitrary points, range 0-200-ish)
        # do an arbitrary calculation using gen to give the results I want (tried values in a spreadsheet until looked right)
        # the aim is to space costs widely across types within a generation, but only have slight increase (or flat) across generations of same type
        gen_multiplier = 8.52 - math.pow(1.22, self.gen)
        run_cost = gen_multiplier * (fixed_run_cost_points + floating_run_cost_points)
        # freight engines get a run cost bonus as they'll often be sat waiting for loads, so balance (also super realism!!)
        # doing this is preferable to doing variable run costs, which are weird and confusing (can't trust the costs showin in vehicle window)
        if self.role in [
            "heavy_freight",
            "super_heavy_freight",
        ]:  # smaller bonus for heavy_freight
            run_cost = 0.9 * run_cost
        elif self.role in [
            "branch_freight",
            "freight",
        ]:  # bigger bonus for other freight
            run_cost = 0.8 * run_cost
        # massive bonuses for NG and Gronks
        elif self.role == "gronk!":
            run_cost = 0.66 * run_cost
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
        self.role = "driving_cab_express_mixed"
        self.role_child_branch_num = -1  # driving cab cars are probably jokers?
        self.buy_menu_hint_driving_cab = True
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types[
            "autocoach_combine"
        ]
        # confer tiny power value to make this one an engine so it can lead.
        self.power_by_power_source = {
            "NULL": 10
        }  # use 10 not 1, because 1 looks weird when added to engine HP
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0
        # ....buy costs adjusted to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_buy_cost_points = 6  # to reduce it from engine factor
        # ....run costs nerfed down to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_run_cost_points = 43
        # no flip as articulated innit (even needed?)
        self.allow_flip = False
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCustom("vehicle_autocoach.pynml")

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class MailEngineConsist(EngineConsist):
    """
    Consist of engines / units that has mail (and express freight) capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
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
        self.role = "driving_cab_express_mail"
        self.role_child_branch_num = -1  # driving cab cars are probably jokers?
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = True
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        self.power_by_power_source = {"NULL": 300}
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0.1
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1  # to reduce it from engine factor
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="driving_cab_cars",
            liveries=[{},{}],
            # temp commented out until spritesheets revised
            #liveries=self.roster.default_mail_liveries,
        )


class MailEngineCargoSprinterEngineConsist(MailEngineConsist):
    """
    Consist for a cab motor unit for Cargo Sprinter express freight unit.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # non-standard cite
        self._cite = "Arabella Unit"
        # run cost algorithm doesn't account for dual-head / high power MUs reliably, so just fix it here, using assumption that there are very few cargo sprinters and this will be fine
        self.fixed_run_cost_points = 240
        self._loading_speed_multiplier = 2
        # Graphics configuration
        # !! there is no automatic masking of the cab overlays as of Dec 2020, currently manual - automation might be needed for well cars in future, deal with it then if that's the case
        # NOTE that cargo sprinter will NOT randomise containers on load as of Dec 2020 - there is a bug with rear unit running unwanted triggers and re-randomising in depots etc
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_cargo_sprinter.pynml",
            cargo_label_mapping=GestaltGraphicsIntermodalContainerTransporters().cargo_label_mapping,
            num_extra_layers_for_spritelayer_cargos=2,
        )

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["cargo_sprinter"]


class MailEngineMetroConsist(MailEngineConsist):
    """
    Consist for a mail metro train.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buy costs increased above baseline, account for 2 units + underground nonsense
        self.buy_cost_adjustment_factor = 2
        # metro should only be effective over short distances
        # ....run cost multiplier is adjusted up from pax base for underground nonsense, also account for 2 units
        self.floating_run_cost_multiplier = 18
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # Graphics configuration
        # 1 livery as can't be flipped
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="metro",
            liveries=[{}],
        )

    @property
    def loading_speed_multiplier(self):
        # OP bonus to mail metro loading speed
        return 4


class MailEngineRailcarConsist(MailEngineConsist):
    """
    Consist for a mail railcar.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # non-standard cite
        if self.base_track_type_name == "NG":
            # give NG a bonus to align run cost with NG railbus
            self.fixed_run_cost_points = 52

        self._cite = "Arabella Unit"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # by design, mail railcars don't change livery in a pax consist, but do have 2 liveries, matching mail cars for this generation
        # position variants
        # * unit with driving cabs both ends
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no driving cabs (OPTIONAL - only provided for 4-unit sets)
        # Rules are 2 unit sets of 3 unit sets (4 could also be supported, but isn't at time of writing)
        if kwargs.get("use_3_unit_sets", False):
            consist_ruleset = "railcars_3_unit_sets"
            spriterow_group_mappings = {
                "default": 0,
                "first": 1,
                "last": 2,
                "special": 3,
            }
        else:
            consist_ruleset = "railcars_2_unit_sets"
            spriterow_group_mappings = {
                "default": 0,
                "first": 1,
                "last": 2,
                "special": 0,
            }
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset=consist_ruleset,
            liveries=self.roster.default_mail_liveries,
            # temp commented out until spritesheets revised
            #liveries=self.roster.default_mail_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # this is intended for pax railcars, but mail railcars share templating in some cases, so stub in this result to prevent unwanted behaviour
        # mail railcars generally do not combine with anything other than their own ID, this is just a compatibility stub
        result = []
        result.extend(self.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result


class PassengerEngineConsist(EngineConsist):
    """
    Consist of engines / units that has passenger capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = ["PASS"]
        # increased buy costs for having seats and stuff eh?
        self.buy_cost_adjustment_factor = 1.8
        # ...but reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 84
        # specific structure for capacity multiplier and loading speed, over-ride in subclasses as needed
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["default"]

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class PassengerEngineCabControlCarConsist(PassengerEngineConsist):
    """
    Consist for a passenger cab control car / driving trailer.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "driving_cab_express_pax"
        self.role_child_branch_num = -1  # driving cab cars are probably jokers?
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = True
        # special purpose attr for use with alt var 41 and pax_car_ids
        self.treat_as_pax_car_for_var_41 = True
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        self.power_by_power_source = {"NULL": 300}
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0.1
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1  # to reduce it from engine factor
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="driving_cab_cars",
            liveries=self.roster.default_pax_liveries,
        )


class PassengerHSTCabEngineConsist(PassengerEngineConsist):
    """
    Consist for a dual-headed HST (high speed train).
    May or may not have capacity (set per vehicle).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # always dual-head
        self.dual_headed = True
        self.lgv_capable = kwargs.get("lgv_capable", False)
        self.buy_cost_adjustment_factor = 1.2
        # higher speed should only be effective over longer distances
        # ....run cost multiplier is adjusted up from pax base for high speed
        self.floating_run_cost_multiplier = 10
        # non-standard cite
        self._cite = "Dr Constance Speed"


class PassengerEngineExpressRailcarConsist(PassengerEngineConsist):
    """
    Consist for an express pax railcar (single unit, combinable).
    Intended for express-speed, high-power long-distance EMUs, use railbus or railcars for short / slow / commuter routes.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 0.85
        # to avoid these railcars being super-bargain cheap, add a cost malus compared to standard railcars (still less than standard engines)
        self.fixed_run_cost_points = 155
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_4_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to express pax railcars and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of express_railcar_passenger_trailer_car trailers
        result = []
        # this will catch self also
        for consist in self.roster.engine_consists:
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["express_pax_railcar"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        for consist in self.roster.wagon_consists[
            "express_railcar_passenger_trailer_car"
        ]:
            if (consist.gen == self.gen) and (
                consist.base_track_type_name == self.base_track_type_name
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result


class PassengerEngineMetroConsist(PassengerEngineConsist):
    """
    Consist for a pax metro train.  Just a sparse subclass to force the gestalt_graphics
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buy costs increased above baseline, account for 2 units + underground nonsense
        self.buy_cost_adjustment_factor = 2
        # metro should only be effective over short distances
        # ....run cost multiplier is adjusted up from pax base for underground nonsense, also account for 2 units
        self.floating_run_cost_multiplier = 18
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # Graphics configuration
        # 1 livery as can't be flipped
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="metro",
            liveries=[{}],
        )

    @property
    def loading_speed_multiplier(self):
        # super super OP bonus to pax metro loading speed
        return 8


class PassengerEngineRailbusConsist(PassengerEngineConsist):
    """
    Consist for a lightweight railbus (single unit, combinable).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_flip = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # big cost bonus for railbus
        self.fixed_run_cost_points = 48
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # 2 liveries, don't need to match anything else, railbus isn't intended to combine well with other vehicle types
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # ruleset will combine these to make multiple-units 1, 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_2_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to railbus and will be fragile if railbus or trailers are changed/extended
        result = []
        # this will catch self also
        for consist in self.roster.engine_consists:
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["pax_railbus"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        for consist in self.roster.wagon_consists["railbus_passenger_trailer_car"]:
            if (consist.gen == self.gen) and (
                consist.base_track_type_name == self.base_track_type_name
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result


class PassengerEngineRailcarConsist(PassengerEngineConsist):
    """
    Consist for a high-capacity pax railcar (single unit, combinable).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["high_capacity"]
        # non-standard cite
        self._cite = "Arabella Unit"
        self.allow_flip = True
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_3_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

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
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["pax_railcar"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        for consist in self.roster.wagon_consists["railcar_passenger_trailer_car"]:
            if (consist.gen == self.gen) and (
                consist.base_track_type_name == self.base_track_type_name
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result


class SnowploughEngineConsist(EngineConsist):
    """
    Consist for a snowplough.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "snoughplough!"  # blame Pikka eh?
        self.role_child_branch_num = -1
        self.buy_menu_hint_driving_cab = True
        self.allow_flip = True
        # nerf power and TE down to minimal values, these confer a tiny performance boost to the train, 'operational efficiency' :P
        self.power_by_power_source = {"NULL": 100}
        self.tractive_effort_coefficient = 0.1
        # give it mail / express capacity so it has some purpose :P
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1  # to reduce it from engine factor
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCustom("vehicle_snowplough.pynml")


class TGVCabEngineConsist(EngineConsist):
    """
    Consist for a TGV (very high speed) engine cab (leading motor unit)
    This has power by default and would usually be set as a dual-headed engine.
    Adding specific middle engines (with correct ID) will increase power for this engine.
    This does not have pax capacity, by design, to allow for TGV La Poste mail trains.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_menu_hint_wagons_add_power = True
        self.tilt_bonus = True
        self.lgv_capable = True
        # note that buy costs are actually adjusted down from pax base, to account for distributed traction etc
        self.buy_cost_adjustment_factor = 0.95
        # ....run cost multiplier is adjusted up from pax base because regrettable realism
        # but allow that every vehicle will have powered run costs, so not too high eh?
        self.floating_run_cost_multiplier = 16
        # train_flag_mu solely used for ottd livery (company colour) selection
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        # non-standard cite
        self._cite = "Dr Constance Speed"

    @property
    def buy_menu_distributed_power_substring(self):
        return "STR_WAGONS_ADD_POWER_CAB"

    @property
    def buy_menu_distributed_power_name_substring(self):
        return "STR_NAME_" + self.id

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.power


class TGVMiddleEngineConsistMixin(EngineConsist):
    """
    Mixin for an intermediate motor unit for very high speed train (TGV etc).
    When added to the correct cab engine, this vehicle will cause cab power to increase.
    Add as additional class for e.g. pax or mail engine consist.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cab_id = self.id.split("_middle")[0] + "_cab"
        self.wagons_add_power = True
        self.buy_menu_hint_wagons_add_power = True
        self.tilt_bonus = True
        self.lgv_capable = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        # eh as of Feb 2019, OpenTTD won't actually use this for middle cars, as not engines
        # this means the buy menu won't match, but wagons will match anyway when attached to cab
        # prop left in place in case that ever gets changed :P
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # 1 livery as can't be flipped
        # position variants
        # * default unit
        # * unit with pantograph - leading end
        # * unit with pantograph -  rear end
        # * buffet unit
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=[{}, {}],
            pantograph_type=self.pantograph_type,
        )

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
        # take 49% of cab engine running cost as running cost
        # this is to prevent horrible scaling up of costs with each unit added, but could assume the cab has more cost due to driver, equipment etc
        return int(0.49 * self.cab_consist.running_cost)

    @property
    def buy_menu_distributed_power_substring(self):
        return "STR_WAGONS_ADD_POWER_MIDDLE"

    @property
    def buy_menu_distributed_power_name_substring(self):
        return "STR_NAME_" + self.cab_id

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.cab_consist.power


class TGVMiddleMailEngineConsist(TGVMiddleEngineConsistMixin, MailEngineConsist):
    """
    Mail intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TGVMiddlePassengerEngineConsist(
    TGVMiddleEngineConsistMixin, PassengerEngineConsist
):
    """
    Pax intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CarConsist(Consist):
    """
    Intermediate class for car (wagon) consists to subclass from, provides sparse properties, most are declared in subclasses.
    """

    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        id = self.get_wagon_id(self.base_id, **kwargs)
        kwargs["id"] = id
        super().__init__(**kwargs)
        self.roster.register_wagon_consist(self)

        self._joker = False  # over-ride this in sub-class as needed
        self.speed_class = (
            "standard"  # over-ride this in sub-class for, e.g. express freight consists
        )
        self.subtype = kwargs["subtype"]
        # Weight factor: over-ride in sub-class as needed
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type_name == "NG" else 1
        # used to synchronise / desynchronise groups of vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        # default all to car consists to 'universal' offset, over-ride in subclasses as needed
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["universal"]
        )
        # assume all wagons randomly swap CC, revert to False in wagon subclasses as needed
        self.use_colour_randomisation_strategies = True
        # set to 2 in subclass if 2cc should be randomised - can't randomise both, too fiddly
        self.cc_num_to_randomise = 1
        # over-ride in subclasses to select specific randomisation strategy for vehicle type
        self.auto_colour_randomisation_strategy_num = 0  # 0 is default
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
        buy_cost_points = (
            speed_cost_points * length_cost_factor * self.buy_cost_adjustment_factor
        )
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
        if self.base_track_type_name == "NG":
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
            if wagon.base_track_type_name == self.base_track_type_name:
                tree_permissive.append(wagon.gen)
                if wagon.subtype == self.subtype:
                    tree_strict.append(wagon.gen)

        tree_permissive = sorted(set(tree_permissive))
        tree_strict = sorted(set(tree_strict))

        if tree_permissive.index(self.gen) == len(tree_permissive) - 1:
            # this is the last generation of this type, on this track type, so keep it around
            # note that there may also be other subtypes in this generation, but they'll all be the last of the type
            return "VEHICLE_NEVER_EXPIRES"

        if tree_strict.index(self.gen) != len(tree_strict) - 1:
            # this is not the last of this subtype, so span strictly over to the next of this subtype
            next_gen = tree_strict[tree_strict.index(self.gen) + 1]
        else:
            # this is the last of this subtype, but there are other later generations of other subtypes
            next_gen = tree_permissive[tree_permissive.index(self.gen) + 1]
        next_gen_intro_year = self.roster.intro_years[self.base_track_type_name][
            next_gen - 1
        ]
        return next_gen_intro_year - self.intro_year

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos

        # special case NG - extend this for other track_types as needed
        # 'narmal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get("base_track_type_name", None) == "NG":
            id_base = id_base + "_ng"
        result = "_".join(
            (
                id_base,
                kwargs["roster_id"],
                "gen",
                str(kwargs["gen"]) + str(kwargs["subtype"]),
            )
        )
        return result

    def get_wagon_title_class_str(self):
        return "STR_NAME_SUFFIX_" + self.base_id.upper()

    def get_wagon_title_subtype_str(self):
        if self.subtype == "A":
            subtype_str = "STR_NAME_SUFFIX_SMALL"
        elif self.subtype == "B":
            subtype_str = "STR_NAME_SUFFIX_MEDIUM"
        elif self.subtype == "C":
            subtype_str = "STR_NAME_SUFFIX_LARGE"
        elif self.subtype == "D":
            subtype_str = "STR_NAME_SUFFIX_TWIN"
        return subtype_str

    @property
    def name(self):
        if self.is_randomised_wagon or self.is_caboose:
            optional_randomised_suffix = "STR_NAME_SUFFIX_RANDOMISED_WAGON"
        else:
            optional_randomised_suffix = "STR_EMPTY"
        if self.subtype == "U":
            # subtype U is a hack to indicate there is only one subtype for this wagon, so no size suffix needed
            return "string(STR_NAME_CONSIST_PLAIN, string({a}), string({b}))".format(
                a=self.get_wagon_title_class_str(), b=optional_randomised_suffix
            )
        else:
            return "string(STR_NAME_CONSIST_PARENTHESES, string({a}), string({b}), string({c}))".format(
                a=self.get_wagon_title_class_str(),
                b=self.get_wagon_title_subtype_str(),
                c=optional_randomised_suffix,
            )

    @property
    def joker(self):
        # jokers are bonus vehicles (mostly) engines which don't fit strict tech tree progression
        # for cars, jokers are mid-length 'B' vehicles and/or rules from the sub-class
        if self.subtype == "B" or self._joker == True:
            return True
        else:
            return False


class AlignmentCarConsist(CarConsist):
    """
    For checking sprite alignment
    """

    def __init__(self, **kwargs):
        self.base_id = "alignment_car"
        super().__init__(**kwargs)
        self.speed_class = None  # no speed limit
        # refit nothing
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.buy_cost_adjustment_factor = 0  # free
        # no random CC, no flip
        self.use_colour_randomisation_strategies = False
        self.allow_flip = False


class AutomobileCarConsistBase(CarConsist):
    """
    Transports automobiles (cars, trucks, tractors etc).
    'Automobile' is used as name to avoid confusion with 'Vehicles' or 'Car'.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = []  # no classes, use explicit labels
        # self.label_refits_allowed = ["PASS", "VEHI", "ENSP", "FMSP"]
        self.label_refits_allowed = ["PASS", "VEHI"]
        self.label_refits_disallowed = []
        self.default_cargos = ["VEHI"]
        # special flag to turn on cargo subtypes specific to vehicles, can be made more generic if subtypes need to be extensible in future
        # self.use_cargo_subytpes_VEHI = True
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # automobile cars can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random automobile cargos, which would also cause new random wagon colour
        # player can still flip to the second livery
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        if self.subtype == "D":
            consist_ruleset = "articulated_permanent_twin_sets"
        else:
            consist_ruleset = self._consist_ruleset
        self.gestalt_graphics = GestaltGraphicsAutomobilesTransporter(
            self.spritelayer_cargo_layers,
            consist_ruleset=consist_ruleset,
        )


class AutomobileCarConsist(AutomobileCarConsistBase):
    """
    Automobile transporter with single flat deck at conventional height.
    """

    def __init__(self, **kwargs):
        self.base_id = "automobile_car"
        super().__init__(**kwargs)

    @property
    def _consist_ruleset(self):
        return "1_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["default"]


class AutomobileDoubleDeckCarConsist(AutomobileCarConsistBase):
    """
    Automobile transporter with double deck, cars only.
    """

    def __init__(self, **kwargs):
        self.base_id = "double_deck_automobile_car"
        super().__init__(**kwargs)
        # blah blah, more restrictive refits for double deck, cars only
        self.label_refits_allowed = ["PASS", "VEHI"]
        self.use_cargo_subytpes_VEHI = False
        # double deck cars need an extra masked overlay, which is handled via gestalt_graphics
        self.gestalt_graphics.add_masked_overlay = True

    @property
    def _consist_ruleset(self):
        if self.subtype == "B":
            return "2_unit_sets"
        else:
            return "4_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["double_deck_lower", "double_deck_upper"]


class AutomobileLowFloorCarConsist(AutomobileCarConsistBase):
    """
    Automobile transporter with single deck at lowered height.
    """

    def __init__(self, **kwargs):
        self.base_id = "low_floor_automobile_car"
        super().__init__(**kwargs)

    @property
    def _consist_ruleset(self):
        return "4_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class BolsterCarConsist(CarConsist):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    def __init__(self, **kwargs):
        self.base_id = "bolster_car"
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_flatbed_freight"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["long_products"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_metal_coil_car",
            "randomised_flat_car",
        ]
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="flat")


class BoxCarConsistBase(CarConsist):
    """
    Base for box car, van - piece goods cargos, express, other selected cargos.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["packaged_freight"]
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "box_freight"
        ]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["box"]
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True


class BoxCarConsist(BoxCarConsistBase):
    """
    Standard box car / van
    """

    def __init__(self, **kwargs):
        self.base_id = "box_car"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "randomised_box_car",
            "randomised_piece_goods_car",
        ]
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.box_livery_recolour_maps,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="box_car",
            weathered_variants=weathered_variants,
        )


class BoxCarCurtainSideConsist(BoxCarConsistBase):
    """
    Curtain side box car - same refits as box car.
    *Not* tarpaulin car which is curtain roof flat.
    """

    def __init__(self, **kwargs):
        self.base_id = "curtain_side_box_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_curtain_side"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_box_car",
            "randomised_piece_goods_car",
        ]
        self._joker = True
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.curtain_side_livery_recolour_maps,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="curtain_side_box_car",
            weathered_variants=weathered_variants,
        )


class BoxCarGoodsConsist(BoxCarConsistBase):
    """
    Alternative livery for standard box car / van
    """

    def __init__(self, **kwargs):
        self.base_id = "goods_box_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_goods"]
        # don't include in random box car group, at least for pony, looks bad - other rosters may differ?
        self.randomised_candidate_groups = ["randomised_piece_goods_car"]
        # Graphics configuration
        self.roof_type = "freight_brown"
        weathered_variants = {
            "unweathered": graphics_constants.goods_box_car_body_recolour_maps,
            "weathered": graphics_constants.goods_box_car_body_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="goods_box_car",
            weathered_variants=weathered_variants,
        )


class BoxCarMerchandiseConsist(BoxCarConsistBase):
    """
    Alternative livery for standard box car / van
    """

    def __init__(self, **kwargs):
        self.base_id = "merchandise_box_car"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "randomised_box_car",
            "randomised_piece_goods_car",
        ]
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": (
                ("DFLT", graphics_constants.merchandise_car_body_recolour_map),
            ),
            "weathered": (
                (
                    "DFLT",
                    graphics_constants.merchandise_car_body_recolour_map_weathered,
                ),
            ),
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="box_car",
            weathered_variants=weathered_variants,
        )


class BoxCarRandomisedConsist(BoxCarConsistBase):
    """
    Random choice of box car sprite, from available box cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_box_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=2)


class BoxCarSlidingWallConsist(BoxCarConsistBase):
    """
    Sliding wall van - (cargowagon, habfiss, thrall, pullman all-door car etc) - same refits as box car.
    """

    def __init__(self, **kwargs):
        self.base_id = "sliding_wall_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_sliding_wall"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.sliding_wall_livery_recolour_maps,
            "weathered": graphics_constants.sliding_wall_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="sliding_wall_car",
            weathered_variants=weathered_variants,
        )


class BoxCarVehiclePartsConsist(BoxCarConsistBase):
    """
    Vehicle parts box car, van - same refits as box car, just a specific visual variation.
    """

    def __init__(self, **kwargs):
        self.base_id = "vehicle_parts_box_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_vehicle_parts"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self._joker = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.box_livery_recolour_maps,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="vehicle_parts_box_car",
            weathered_variants=weathered_variants,
        )


class CabooseCarConsist(CarConsist):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """

    def __init__(self, **kwargs):
        self.base_id = "caboose_car"
        super().__init__(**kwargs)
        self.speed_class = None  # no speed limit
        # refit nothing, don't mess with this, it breaks auto-replace
        self.class_refit_groups = []
        # label refits are just to get caboose to use freight car livery group
        # try to catch enough common cargos otherwise the vehicle will be hidden; don't use MAIL as that forces pax colour group
        self.label_refits_allowed = ["ENSP", "GOOD", "COAL", "WOOD", "OIL_"]
        self.label_refits_disallowed = []
        self.buy_cost_adjustment_factor = (
            0.75  # chop down caboose costs, they're just eye candy eh
        )
        self.use_colour_randomisation_strategies = True
        self.allow_flip = True
        self.random_reverse = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(
            recolour_map=graphics_constants.caboose_car_body_recolour_map,
            spriterow_labels=kwargs.get("spriterow_labels"),
            caboose_families=kwargs.get("caboose_families"),
            buy_menu_sprite_pairs=kwargs.get("buy_menu_sprite_pairs"),
        )

    @property
    def buy_menu_variants_by_date(self):
        # map buy menu variants and date ranges to show them for
        result = []
        for counter, date_range in enumerate(
            self.roster.intro_year_ranges(self.base_track_type_name)
        ):
            result.append((counter, date_range))
        return result


class CarbonBlackHopperCarConsist(CarConsist):
    """
    Dedicated covered hopper car for carbon black.  No other cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "carbon_black_hopper_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ["CBLK"]
        self.label_refits_disallowed = []
        self.default_cargos = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.carbon_black_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.carbon_black_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoilBuggyCarConsist(CarConsist):
    """
    Dedicated (steel mill) buggy car for coils. Not a standard railcar. No other refits.
    """

    # note does NOT subclass CoilCarConsistBase - different type of consist
    def __init__(self, **kwargs):
        self.base_id = "coil_buggy_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # none needed
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "metal_coil"
        ]
        self.label_refits_disallowed = []  # none needed
        self.default_cargos = polar_fox.constants.default_cargos["coil"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2  # double the default weight
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self._joker = True
        # CC is swapped randomly (player can't choose), player can't flip as vehicle is articulated
        self.allow_flip = False
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            cargo_row_map={},  # leave blank, all default to same
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", "flipped", 10],
                ["loading_0", "flipped", 40],
                ["loaded_0", "flipped", 40],
                ["empty_unweathered", "unflipped", 10],
                ["loading_0", "unflipped", 40],
                ["loaded_0", "unflipped", 40],
            ],
        )


class CoilCarConsistBase(CarConsist):
    """
    Coil car - for finished metals (steel, copper etc).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "metal_coil"
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = ["randomised_metal_coil_car"]
        # allow flipping, used to flip company colour
        self.allow_flip = True


class CoilCarCoveredConsist(CoilCarConsistBase):
    """
    Covered coil car.  No visible cargo.
    """

    def __init__(self, **kwargs):
        self.base_id = "coil_car_covered"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil_covered"]
        self.cc_num_to_randomise = 2
        self._joker = True
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC2}
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            piece="coil",
            has_cover=True,
        )


class CoilCarUncoveredConsist(CoilCarConsistBase):
    """
    Uncovered coil car.  Visible cargo.
    """

    def __init__(self, **kwargs):
        self.base_id = "coil_car_uncovered"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil"]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="coil")


class ColdMetalCarRandomisedConsist(CoilCarConsistBase):
    """
    Random choice of cold metal car sprite, from available coil cars, bolster cars etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_metal_coil_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=2)


class CoveredHopperCarConsistBase(CarConsist):
    """
    Bulk cargos needing covered protection.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "covered_hoppers"
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self.randomised_candidate_groups = ["randomised_covered_hopper_car"]
        # allow flipping, used to flip company colour
        self.allow_flip = True


class CoveredHopperCarConsist(CoveredHopperCarConsistBase):
    """
    Default covered hopper.
    """

    def __init__(self, **kwargs):
        self.base_id = "covered_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.pellet_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.pellet_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoveredHopperCarChemicalConsist(CoveredHopperCarConsistBase):
    """
    Covered hopper for chemical industry cargos, same refits as standard covered hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "chemical_covered_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_chemical"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.chemical_covered_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.chemical_covered_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoveredHopperCarDryPowderConsist(CoveredHopperCarConsistBase):
    """
    Covered hopper for dry powder cargos, same refits as standard covered hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "dry_powder_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_mineral"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_hopper_car_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoveredHopperCarMineralConsist(CoveredHopperCarConsistBase):
    """
    Covered hopper for mineral industry cargos, same refits as standard covered hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_covered_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_mineral"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.mineral_covered_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.mineral_covered_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoveredHopperCarRandomisedConsist(CoveredHopperCarConsistBase):
    """
    Random choice of covered hopper car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_covered_hopper_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=1)


class CoveredHopperCarRollerRoofConsist(CoveredHopperCarConsistBase):
    """
    Covered hopper with a rollover roof, same refits as standard covered hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "roller_roof_hopper_car"
        super().__init__(**kwargs)
        self._joker = True
        self.default_cargos = polar_fox.constants.default_cargos["covered_roller_roof"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.pellet_hopper_car_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class CoveredHopperCarSwingRoofConsist(CoveredHopperCarConsistBase):
    """
    Covered hopper with a swing roof hatch, same refits as standard covered hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "swing_roof_hopper_car"
        super().__init__(**kwargs)
        self._joker = True
        self.default_cargos = polar_fox.constants.default_cargos["covered_chemical"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_hopper_car_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class DumpCarConsistBase(CarConsist):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos, same set as hopper cars.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["dump_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_dump_bulk"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["dump"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class DumpCarConsist(DumpCarConsistBase):
    """
    Standard Dump Car.
    """

    def __init__(self, **kwargs):
        self.base_id = "dump_car"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "randomised_dump_car",
            "randomised_bulk_car",
        ]


class DumpCarAggregateConsist(DumpCarConsistBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_aggregates"]
        self.randomised_candidate_groups = [
            "randomised_dump_car",
            "randomised_bulk_car",
        ]
        self._joker = True


class DumpCarHighSideConsist(DumpCarConsistBase):
    """
    High Side Dump Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "dump_car_high_side"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_high_sides"]
        self.randomised_candidate_groups = [
            "randomised_dump_car",
            "randomised_bulk_car",
        ]
        self._joker = True


class DumpCarOreConsist(DumpCarConsistBase):
    """
    Ore Dump Car.
    Same as standard dump car, but different appearance and default cargos.
    The classname breaks convention (would usually be OreCar), this is to keep all dump car subclasses togther).
    """

    def __init__(self, **kwargs):
        self.base_id = "ore_dump_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_ore"]
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            2  # no randomisation, but reverse on flip
        )


class DumpCarRandomisedConsist(DumpCarConsistBase):
    """
    Random choice of dump car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_dump_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=2)


class DumpCarScrapMetalConsist(DumpCarConsistBase):
    """
    Scrap Metal Car
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "scrap_metal_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_scrap"]


# not in alphabetical order as it depends on subclassing DumpCarConsistBase
class BulkCarRandomisedConsist(DumpCarConsistBase):
    """
    Random choice of bulk car sprite, from available dump / hopper cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_bulk_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=1)


class EdiblesTankCarConsist(CarConsist):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = "edibles_tank_car"
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "edible_liquids"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["edibles_tank"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["food_wagons"]
        )
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        # only one livery, but recolour gestalt used to automate adding chassis
        weathered_variants = {
            "unweathered": graphics_constants.edibles_tank_car_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class ExpressCarConsist(CarConsist):
    """
    Express cars - express freight, valuables, mails.
    """

    def __init__(self, **kwargs):
        self.base_id = "express_car"
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["express"]
        # adjust weight factor because express car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        # keep matched to MailCarConsist
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_core"]
        )
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        self.use_wagon_base_colour_parameter = False
        # Graphics configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        weathered_variants = {
            "unweathered": graphics_constants.box_livery_recolour_maps,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="express_car",
            weathered_variants=weathered_variants,
        )


class ExpressIntermodalCarConsist(CarConsist):
    """
    Express intermodal container cars - express freight, valuables, mails.
    """

    def __init__(self, **kwargs):
        self.base_id = "express_intermodal_car"
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["express"]
        self._loading_speed_multiplier = 2
        # adjust weight factor because express intermodal car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        # keep matched to MailCarConsist
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_core"]
        )
        self._joker = True
        # intermodal containers can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        # player can still flip to the second livery
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        # !! note to future, if e.g. NA Horse needs longer express intermodal sets, set the consist_ruleset conditionally by checking roster
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            consist_ruleset="2_unit_sets"
        )

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        # !! express intermodal all default currently, extend as needed
        return ["default"]


class FarmProductsBoxCarConsist(CarConsist):
    """
    Farm type cargos - box cars / vans.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_products_box_car"
        super().__init__(**kwargs)
        # note this is not derived from BoxCarBase, it's a standalone type
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "farm_products"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["farm_products_box"]
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.farm_products_box_car_livery_recolour_maps,
            "weathered": graphics_constants.farm_products_box_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="farm_products_box_car",
            weathered_variants=weathered_variants,
        )


class FarmProductsHopperCarConsist(CarConsist):
    """
    Farm type cargos - covered hoppers.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_products_hopper_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "farm_products"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["farm_products_hopper"]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.farm_products_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.farm_products_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class FlatCarConsistBase(CarConsist):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_flatbed_freight"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["flat"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True


class FlatCarBulkheadConsist(FlatCarConsistBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    def __init__(self, **kwargs):
        self.base_id = "bulkhead_flat_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["bulkhead"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_piece_goods_car",
            "randomised_metal_coil_car",
            "randomised_flat_car",
        ]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="flat")


class FlatCarConsist(FlatCarConsistBase):
    """
    Flatbed - no stakes, visible cargo.
    """

    def __init__(self, **kwargs):
        self.base_id = "flat_car"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "randomised_flat_car",
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="flat")


class FlatCarPlateConsist(FlatCarConsistBase):
    """
    Low-side wagon - variant on flat wagon, refits same
    """

    def __init__(self, **kwargs):
        self.base_id = "plate_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["plate"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_metal_coil_car",
            "randomised_piece_goods_car",
            "randomised_flat_car",
        ]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="flat")


class FlatCarRandomisedConsist(FlatCarConsistBase):
    """
    Random choice of flat car sprite, from available coil cars, bolster cars etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_flat_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=2)


class FlatCarSlidingRoofConsist(FlatCarConsistBase):
    """
    Sliding roof van - sfins2 holdall and similar - same refits as flat, not van (experimental)
    """

    def __init__(self, **kwargs):
        self.base_id = "sliding_roof_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["flat_sliding_roof"]
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_piece_goods_car",
            "randomised_flat_car",
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.sliding_roof_car_body_recolour_map,
            "weathered": graphics_constants.sliding_roof_car_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            piece="flat",
            has_cover=True,
        )


class FlatCarTarpaulinConsist(FlatCarConsistBase):
    """
    Tarpaulin car - a graphical alternative to flat car, with identical refits
    """

    def __init__(self, **kwargs):
        self.base_id = "tarpaulin_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["flat_tarpaulin_roof"]
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = [
            "randomised_metal_coil_car",
            "randomised_piece_goods_car",
            "randomised_flat_car",
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.tarpaulin_car_body_recolour_map
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            piece="flat",
            has_cover=True,
        )


class GasTankCarConsistBase(CarConsist):
    """
    Specialist tank cars for gases, e.g. Oxygen, Chlorine, Ammonia, Propylene etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "cryo_gases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["cryo_gases"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.33
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        weathered_variants = {
            "unweathered": polar_fox.constants.cryo_tanker_livery_recolour_maps,
            "weathered": polar_fox.constants.cryo_tanker_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class GasTankCarPressureConsist(GasTankCarConsistBase):
    """
    Pressure tank cars for gases under pressure at low temperatue, e.g. Chlorine etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = "pressure_tank_car"
        super().__init__(**kwargs)


class GasTankCarCryoConsist(GasTankCarConsistBase):
    """
    Specialist insulated and pressurised tank cars for gases under pressure at low temperatue, e.g. Oxygen etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = "cryo_tank_car"
        super().__init__(**kwargs)


class HopperCarConsistBase(CarConsist):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["dump_freight"]
        self.label_refits_allowed = []  # none needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_dump_bulk"
        ]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self.randomised_candidate_groups = [
            "randomised_hopper_car",
            "randomised_bulk_car",
        ]
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True)


class HopperCarConsist(HopperCarConsistBase):
    """
    Standard hopper car. Defaults to coal.
    """

    def __init__(self, **kwargs):
        self.base_id = "hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]


class HopperCarMineralConsist(HopperCarConsistBase):
    """
    Hopper for mineral industry cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_hopper_car"
        super().__init__(**kwargs)
        print("mineral hoppers need default refits set")
        self.default_cargos = polar_fox.constants.default_cargos["hopper_rock"]
        self._joker = True


class HopperCarMGRConsist(HopperCarConsistBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    def __init__(self, **kwargs):
        self.base_id = "mgr_hopper_car"
        super().__init__(**kwargs)
        # don't include MGR hoppers in randomised lists, they don't look good
        self.randomised_candidate_groups = []
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]


class HopperCarRandomisedConsist(HopperCarConsistBase):
    """
    Random choice of hopper car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_hopper_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=1)


class HopperCarOreConsist(HopperCarConsistBase):
    """
    Hopper for ore cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "ore_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_ore"]


class HopperCarRockConsist(HopperCarConsistBase):
    """
    Hopper for rock cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "rock_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_rock"]
        self._joker = True


class HopperCarSkipConsist(HopperCarConsistBase):
    """
    Dedicated (narrow gauge) skip variant of hoppers
    Defaults to rock/stone-type cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "skip_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_rock"]
        # not eligible for randomisation, breaks due to articulation
        self.randomised_candidate_groups = []
        self._joker = True


class IngotCarConsist(CarConsist):
    """
    Dedicated car for steel / iron ingots. A steel mill ingot buggy, not a standard railcar. No other refits.
    """

    def __init__(self, **kwargs):
        self.base_id = "ingot_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # none needed
        self.label_refits_allowed = ["IRON", "CSTI", "STCB", "STST", "STAL"]
        self.label_refits_disallowed = []  # none needed
        self.default_cargos = ["IRON"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2  # double the default weight
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self._joker = True
        # CC is swapped randomly (player can't choose), player can't flip as vehicle is articulated
        self.allow_flip = False
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            cargo_row_map={},  # leave blank, all default to same
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", "flipped", 10],
                ["loading_0", "flipped", 40],
                ["loaded_0", "flipped", 70],
                ["empty_unweathered", "unflipped", 10],
                ["loading_0", "unflipped", 40],
                ["loaded_0", "unflipped", 70],
            ],
        )


class IntermodalCarConsistBase(CarConsist):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["all_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["box_intermodal"]
        self._loading_speed_multiplier = 2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # intermodal containers can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        # player can still flip to the second livery
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # Graphics configuration
        # various rulesets are supported, per consist, (or could be extended to checks per roster)
        if kwargs.get("consist_ruleset", None) is not None:
            consist_ruleset = kwargs.get("consist_ruleset")
        else:
            consist_ruleset = "4_unit_sets"
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            consist_ruleset=consist_ruleset
        )


class IntermodalCarConsist(IntermodalCarConsistBase):
    """
    Default intermodal car - simple flat platform at default height.
    """

    def __init__(self, **kwargs):
        self.base_id = "intermodal_car"
        super().__init__(**kwargs)

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        # the 'default' for NG is the same as for low_floor so just re-use that for now
        if self.base_track_type_name == "NG":
            return ["low_floor"]
        else:
            return ["default"]


class IntermodalLowFloorCarConsist(IntermodalCarConsistBase):
    """
    Low floor intermodal car - simple flat platform at height -1
    """

    def __init__(self, **kwargs):
        self.base_id = "low_floor_intermodal_car"
        super().__init__(**kwargs)

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class KaolinHopperCarConsist(CarConsist):
    """
    Dedicated to kaolin (china clay).
    """

    def __init__(self, **kwargs):
        self.base_id = "kaolin_hopper_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ["KAOL"]
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self._joker = True
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.kaolin_hopper_car_livery_recolour_maps,
            "weathered": graphics_constants.kaolin_hopper_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class LivestockCarConsist(CarConsist):
    """
    Specialist transporter for livestock.
    """

    def __init__(self, **kwargs):
        self.base_id = "livestock_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ["LVST"]
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = ["LVST"]
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.1
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        self.cc_num_to_randomise = 2
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.livestock_livery_recolour_maps,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="livestock_car",
            weathered_variants=weathered_variants,
        )


class LogCarConsist(CarConsist):
    """
    Specialist transporter for logs
    """

    def __init__(self, **kwargs):
        self.base_id = "log_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        # limited refits by design eh
        self.label_refits_allowed = ["WOOD"]
        self.label_refits_disallowed = []
        self.default_cargos = ["WOOD"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        self.cc_num_to_randomise = 2
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="tree_length_logs")


class MailCarConsistBase(CarConsist):
    """
    Common base class for passenger cars.
    """

    # very specific flag used by graphics chain to detect other pax cars (could have used prop 25 userbits, but eh, screw that :)
    report_as_pax_car_to_neighbouring_vehicle_in_rulesets = True

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # specific structure for capacity multiplier and loading speed, over-ride in subclasses as needed
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["default"]
        # keep matched to ExpressCarConsist
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_core"]
        )
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # roof configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class MailCarConsist(MailCarConsistBase):
    """
    Mail cars - also handle express freight, valuables.
    """

    def __init__(self, **kwargs):
        self.base_id = "mail_car"
        super().__init__(**kwargs)
        self.speed_class = "express"
        # adjust weight factor because mail car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_core"]
        )
        # mail cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # * solid block can be used, but looks like freight cars, so duotone liveries are preferred (see caboose cars for inspiration)
        # position based variants
        # longer mail cars get an additional sprite option in the consist ruleset; shorter mail cars don't as it's TMWFTLB
        # * windows or similar variation for first, last vehicles (maybe also every nth vehicle?)
        brake_car_sprites = 1 if self.subtype in ["B", "C"] else 0
        bonus_sprites = 2 if self.subtype in ["C"] else 0
        spriterow_group_mappings = {
            "default": 0,
            "first": brake_car_sprites,
            "last": brake_car_sprites,
            "special": bonus_sprites,
        }

        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="mail_cars",
            liveries=self.roster.default_mail_liveries,
        )


class MailHSTCarConsist(MailCarConsistBase):
    """
    Trailer dedicated for Mail on HST-type trains (no wagon attach, but matching stats and livery).
    """

    def __init__(self, **kwargs):
        self.base_id = "hst_mail_car"
        super().__init__(**kwargs)
        self.speed_class = "hst"
        # used to get insert the name of the parent into vehicle name
        self.cab_id = kwargs[
            "cab_id"
        ]  # cab_id must be passed, do not mask errors with .get()
        self.lgv_capable = kwargs.get("lgv_capable", False)
        self.buy_cost_adjustment_factor = 1.66
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["hst"]
        )
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_HST"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (buffet) coach
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="mail_cars",
            liveries=[{}],
        )

    @property
    def name(self):
        # special name handling to use the cab name
        # !! this doesn't work in the docs,
        # !! really for this kind of stuff, there needs to be a python tree/list of strings, then render to nml, html etc later
        # !! buy menu text kinda does that, but would need to convert all names to do this
        return (
            "string(STR_NAME_CONSIST_COMPOUND, string(STR_NAME_"
            + self.cab_id
            + "), string(STR_NAME_SUFFIX_HST_MAIL_CAR))"
        )


class OpenCarConsistBase(CarConsist):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["all_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self.randomised_candidate_groups = [
            "randomised_open_car",
            "randomised_piece_goods_car",
        ]
        # allow flipping, used to flip company colour
        self.allow_flip = True


class OpenCarConsist(OpenCarConsistBase):
    """
    Standard open car
    """

    def __init__(self, **kwargs):
        self.base_id = "open_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(bulk=True, piece="open")


class OpenCarHoodConsist(OpenCarConsistBase):
    """
    Open car with a hood when fully loaded
    """

    def __init__(self, **kwargs):
        self.base_id = "hood_open_car"
        super().__init__(**kwargs)
        self.default_cargos = ["KAOL"]
        self.default_cargos.extend(polar_fox.constants.default_cargos["open"])
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.hood_open_car_body_recolour_map,
            "weathered": graphics_constants.hood_open_car_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            piece="open",
            weathered_variants=weathered_variants,
            has_cover=True,
        )


class OpenCarMerchandiseConsist(OpenCarConsistBase):
    """
    Open car with alternative livery
    """

    def __init__(self, **kwargs):
        self.base_id = "merchandise_open_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.merchandise_car_body_recolour_map,
            "weathered": graphics_constants.merchandise_car_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, piece="open", weathered_variants=weathered_variants
        )


class OpenCarRandomisedConsist(OpenCarConsistBase):
    """
    Random choice of open car sprite, from available open cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_open_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=1)


class PassengerCarConsistBase(CarConsist):
    """
    Common base class for passenger cars.
    """

    # very specific flag used by graphics chain to detect other pax cars (could have used prop 25 userbits, but eh, screw that :)
    report_as_pax_car_to_neighbouring_vehicle_in_rulesets = True

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["pax"]
        # specific structure for capacity multiplier and loading speed, over-ride in subclasses as needed
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["default"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_core"]
        )
        self.use_colour_randomisation_strategies = False
        self.allow_flip = True
        # roof configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class PassengerCarConsist(PassengerCarConsistBase):
    """
    Standard passenger car.
    Default decay rate, capacities within reasonable distance of original base set pax coaches.
    Position-dependent sprites for brake car etc.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    def __init__(self, **kwargs):
        self.base_id = "passenger_car"
        super().__init__(**kwargs)
        # buy costs and run costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.4
        self.floating_run_cost_multiplier = 3.33
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        if self.base_track_type_name == "NG":
            self._buy_menu_role_string = "STR_ROLE_GENERAL_PURPOSE"
        else:
            self._buy_menu_role_string = "STR_ROLE_GENERAL_PURPOSE_EXPRESS"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special coaches from PassengerLuxuryCarConsist Feb 2021, as Restaurant cars were added
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=self.roster.default_pax_liveries,
        )


class PassengerExpressRailcarTrailerCarConsist(PassengerCarConsistBase):
    """
    Unpowered passenger trailer car for express railcars.
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "express_railcar_passenger_trailer_car"
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["express_non_core"]
        )
        self._joker = True
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_GENERAL_PURPOSE_EXPRESS"
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type_name == "NG" else 1.5
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # 2 liveries, should match local and express liveries of pax cars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_4_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to pax railcar trailers and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of pax_railcar and pax railcar trailers
        result = []
        result.extend(self.lead_unit_variants_numeric_ids)
        for consist in self.roster.engine_consists:
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["express_pax_railcar"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result

    @property
    def hide_in_wagons_only_mode(self):
        return True


class PassengerHSTCarConsist(PassengerCarConsistBase):
    """
    Trailer dedicated for HST-type trains (no wagon attach, but matching stats and livery).
    Moderately improved decay rate compared to standard pax car.
    Position-dependent sprites for buffet car, brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "hst_passenger_car"
        super().__init__(**kwargs)
        self.speed_class = "hst"
        # used to get insert the name of the parent into vehicle name
        self.cab_id = kwargs[
            "cab_id"
        ]  # cab_id must be passed, do not mask errors with .get()
        self.lgv_capable = kwargs.get("lgv_capable", False)
        self.buy_cost_adjustment_factor = 1.66
        # run cost multiplier matches standard pax coach costs; higher speed is accounted for automatically already
        self.floating_run_cost_multiplier = 3.33
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["hst"]
        )
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type_name == "NG" else 1.6
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_HST"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (buffet) coach
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=[{}],
        )

    @property
    def name(self):
        # special name handling to use the cab name
        # !! this doesn't work in the docs,
        # !! really for this kind of stuff, there needs to be a python tree/list of strings, then render to nml, html etc later
        # !! buy menu text kinda does that, but would need to convert all names to do this
        return (
            "string(STR_NAME_CONSIST_COMPOUND, string(STR_NAME_"
            + self.cab_id
            + "), string(STR_NAME_SUFFIX_HST_PASSENGER_CAR))"
        )


class PassengerRailbusTrailerCarConsist(PassengerCarConsistBase):
    """
    Unpowered passenger trailer car for railbus (not railcar).
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "railbus_passenger_trailer_car"
        super().__init__(**kwargs)
        # PassengerCarConsistBase sets 'express' speed, but railbus trailers should over-ride this
        self.speed_class = "standard"
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["suburban"]
        )
        self._joker = True
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_GENERAL_PURPOSE"
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # 2 liveries, don't need to match anything else, railbus isn't intended to combine well with other vehicle types
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # ruleset will combine these to make multiple-units 1, 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_2_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to railbus and will be fragile if railbus or trailers are changed/extended
        result = []
        # this will catch self also
        for consist in self.roster.engine_consists:
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["pax_railbus"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        for consist in self.roster.wagon_consists["railbus_passenger_trailer_car"]:
            if (consist.gen == self.gen) and (
                consist.base_track_type_name == self.base_track_type_name
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result


class PassengerRailcarTrailerCarConsist(PassengerCarConsistBase):
    """
    Unpowered high-capacity passenger trailer car for railcars (not railbus).
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "railcar_passenger_trailer_car"
        super().__init__(**kwargs)
        # PassengerCarConsistBase sets 'express' speed, but railcar trailers should over-ride this
        self.speed_class = "suburban"
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["high_capacity"]
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["suburban"]
        )
        self._joker = True
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_SUBURBAN"
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        # for railcar trailers, the capacity is doubled, so halve the weight factor, this could have been automated with some constants etc but eh, TMWFTLB
        self.weight_factor = 0.33 if self.base_track_type_name == "NG" else 1
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # 2 liveries, should match liveries of railcars for this generation
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_3_unit_sets",
            liveries=self.roster.default_pax_liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def equivalent_ids_alt_var_41(self):
        # where var 14 checks consecutive chain of a single ID, I provided an alternative checking a list of IDs
        # may or may not handle articulated vehicles correctly (probably not, no actual use cases for that)
        # this redefinition specific to pax railcar trailers and will be fragile if railcars or trailers are changed/extended
        # also relies on same ruleset being used for all of pax_railcar and pax railcar trailers
        result = []
        result.extend(self.lead_unit_variants_numeric_ids)
        for consist in self.roster.engine_consists:
            if (
                (consist.gen == self.gen)
                and (consist.base_track_type_name == self.base_track_type_name)
                and (consist.role in ["pax_railcar"])
            ):
                result.extend(consist.lead_unit_variants_numeric_ids)
        # the list requires 16 entries as the nml check has 16 switches, fill out to empty list entries with '-1', which won't match any IDs
        for i in range(len(result), 16):
            result.append(-1)
        return result

    @property
    def hide_in_wagons_only_mode(self):
        return True


class PassengerRestaurantCarConsist(PassengerCarConsistBase):
    """
    Special pax coach that modifies run costs and decay rates for other pax coaches in the consist.
    """

    def __init__(self, **kwargs):
        self.base_id = "restaurant_car"
        super().__init__(**kwargs)
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["restaurant"]
        self.buy_cost_adjustment_factor = 2.5
        # double the luxury pax car amount; balance between the bonus amount (which scales with num. pax coaches) and the run cost of running this booster
        self.floating_run_cost_multiplier = 12
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        self._joker = True
        self._buy_menu_role_string = "STR_ROLE_GENERAL_PURPOSE_EXPRESS"
        self.buy_menu_hint_restaurant_car = True
        # Graphics configuration
        # position based variants are not used for restaurant cars, but they use the pax ruleset and sprite compositor for convenience
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 0, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=self.roster.default_pax_liveries,
        )


class PassengerSuburbanCarConsist(PassengerCarConsistBase):
    """
    Suburban pax car.
    Aggressive decay rate due to high capacity. Improved loading speed, lots of door space.
    Position-dependent sprites for brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "suburban_passenger_car"
        super().__init__(**kwargs)
        # PassengerCarConsistBase sets 'express' speed, but suburban coaches should over-ride this
        # note that setting the speed lower doesn't actually balance profitability vs. standard pax coaches, but it gives a possibly comforting delusion about roles of each type
        self.speed_class = "suburban"
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["high_capacity"]
        # buy costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.4
        # give it a run cost nerf due to the very high capacity
        self.floating_run_cost_multiplier = 4.75
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        # for suburban cars, the capacity is doubled, so halve the weight factor, this could have been automated with some constants etc but eh, TMWFTLB
        self.weight_factor = 0.33 if self.base_track_type_name == "NG" else 1
        self._joker = True
        # directly set role buy menu string here, don't set a role as that confuses the tech tree etc
        self._buy_menu_role_string = "STR_ROLE_SUBURBAN"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special coaches from PassengerCarConsistBase Dec 2018, overkill
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=self.roster.default_pax_liveries,
        )


class PeatCarConsist(CarConsist):
    """
    Specialist transporter (narrow gauge bin) for peat
    """

    def __init__(self, **kwargs):
        self.base_id = "peat_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        # limited refits by design eh
        self.label_refits_allowed = ["PEAT"]
        self.label_refits_disallowed = []
        self.default_cargos = ["PEAT"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        self.cc_num_to_randomise = 2
        # Graphics configuration
        # self.gestalt_graphics = GestaltGraphicsVisibleCargo(piece="tree_length_logs")
        utils.echo_message("Peat car using potash hopper body colour remaps")
        weathered_variants = {
            "unweathered": polar_fox.constants.potash_hopper_car_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class PieceGoodsCarRandomisedConsist(CarConsist):
    """
    Randomised general freight wagon - with refits matching flat / plate / tarpaulin cars - this might be a bad idea
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_piece_goods_car"
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_flatbed_freight"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["flat_tarpaulin_roof"]
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        self.randomised_candidate_groups = []
        self._joker = True
        # Graphics configuration
        self.allow_flip = True
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=3)


class ReeferCarConsist(CarConsist):
    """
    Refrigerated cargos.
    No actual cargo aging change - doesn't really work - so trade higher speed against lower capacity instead.
    """

    def __init__(self, **kwargs):
        self.base_id = "reefer_car"
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["refrigerated_freight"]
        self.label_refits_allowed = []  # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["reefer"]
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["food_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True
        # type-specific wagon colour randomisation
        self.auto_colour_randomisation_strategy_num = (
            1  # single base colour unless flipped
        )
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.refrigerated_livery_recolour_maps,
            "weathered": graphics_constants.refrigerated_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            id_base="reefer_car",
            weathered_variants=weathered_variants,
        )


class SiloCarConsistBase(CarConsist):
    """
    Powder bulk cargos needing protection and special equipment for unloading.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = [
            "SUGR",
            "FMSP",
            "RFPR",
            "BDMT",
            "QLME",
            "SASH",
            "CMNT",
            "CBLK",
            "SAND",
            "SOAP",
        ]  # move to Polar Fox (maybe??)
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["non_core_wagons"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True


class SiloCarConsist(SiloCarConsistBase):
    """
    Standard silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = "silo_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.silo_livery_recolour_maps
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class SiloCarChemicalConsist(SiloCarConsistBase):
    """
    Chemical-coloured silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = "chemical_silo_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.chemical_silo_car_livery_recolour_maps,
            "weathered": graphics_constants.chemical_silo_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class SiloCarCementConsist(SiloCarConsistBase):
    """
    Cement-coloured silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = "cement_silo_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_cement"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.cement_silo_livery_recolour_maps,
            "weathered": graphics_constants.cement_silo_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class SlagLadleCarConsist(CarConsist):
    """
    Dedicated car for iron / steel slag.  No other refits.
    """

    def __init__(self, **kwargs):
        self.base_id = "slag_ladle_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # none needed
        self.label_refits_allowed = ["SLAG"]
        self.label_refits_disallowed = []  # none needed
        self.default_cargos = ["SLAG"]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self.weight_factor = 2  # double the default weight
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self._joker = True
        # CC is swapped randomly (player can't choose), but also swap base livery on flip (player can choose
        self.allow_flip = True
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            cargo_row_map={"SLAG": [0]},
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", "flipped", 10],
                ["loading_0", "flipped", 40],
                ["loaded_0", "flipped", 70],
                ["empty_unweathered", "unflipped", 10],
                ["loading_0", "unflipped", 40],
                ["loaded_0", "unflipped", 70],
            ],
        )


class TankCarConsistBase(CarConsist):
    """
    All non-edible liquid cargos
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they may also change livery at stations if refitted between certain cargo types <shrug>
        super().__init__(**kwargs)
        self.class_refit_groups = ["liquids"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_generic_liquids"
        ]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        # allow flipping, used to flip company colour
        self.allow_flip = True


class TankCarConsist(TankCarConsistBase):
    """
    Standard tank car
    """

    def __init__(self, **kwargs):
        self.base_id = "tank_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["tank"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": polar_fox.constants.tanker_livery_recolour_maps,
            "weathered": polar_fox.constants.tanker_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class TankCarAcidConsist(TankCarConsistBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "acid_tank_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["product_tank"]
        self.randomised_candidate_groups = ["randomised_chemicals_tank_car"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.acid_tank_car_livery_recolour_maps,
            "weathered": graphics_constants.acid_tank_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class TankCarProductConsist(TankCarConsistBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "product_tank_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["product_tank"]
        self.randomised_candidate_groups = ["randomised_chemicals_tank_car"]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.product_tank_car_livery_recolour_maps,
            "weathered": graphics_constants.product_tank_car_livery_recolour_maps_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants
        )


class TankCarChemicalsRandomisedConsist(TankCarConsistBase):
    """
    Random choice of tank car sprite, from available acid / chemicals tank cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "randomised_chemicals_tank_car"
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(dice_colour=3)


class TorpedoCarConsist(CarConsist):
    """
    Specialist wagon for hauling molten pig iron.
    May or may not extend to other metal cargos (probably not).
    """

    def __init__(self, **kwargs):
        self.base_id = "torpedo_car"
        super().__init__(**kwargs)
        self.class_refit_groups = []  # no classes, use explicit labels
        self.label_refits_allowed = ["IRON"]
        self.label_refits_disallowed = []
        self.default_cargos = ["IRON"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
        self.weight_factor = 2  # double the default weight
        self._intro_year_days_offset = (
            global_constants.intro_month_offsets_by_role_group["freight_core"]
        )
        self._joker = True
        # articulated so can't flip
        self.allow_flip = False
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt with dedicated template as these wagons are articulated which standard wagon templates don't support
        self.gestalt_graphics = GestaltGraphicsCustom("vehicle_torpedo_car.pynml")


class BuyableVariant(object):
    """
    Simple class to hold buyable variants of the consist.
    """

    def __init__(self, consist, livery):
        self.consist = consist
        self._livery_num = livery.get("livery_num", None)

    @property
    def buyable_variant_num(self):
        # convenience method
        return self.consist.buyable_variants.index(self)

    @property
    def is_default_buyable_variant(self):
        # convenience method
        if self.buyable_variant_num == 0:
            return True
        else:
            return False


class UnitVariant(object):
    """
    Simple class for unit variants.
    These are used to create variants of units.
    """

    def __init__(self, unit, buyable_variant, **kwargs):
        self.unit = unit
        self.buyable_variant = buyable_variant

        # numeric ids are just assigned sequentially when adding variants
        if len(self.unit.consist.unique_numeric_ids) == 0:
            self.numeric_id = self.unit.consist.base_numeric_id
        else:
            self.numeric_id = max(self.unit.consist.unique_numeric_ids) + 1

    @property
    def id(self):
        if (
            self.unit.is_lead_unit_of_consist
            and self.buyable_variant.is_default_buyable_variant
        ):
            # we make certain assumptions about the id of the first unit of the default variant which need special handling
            return self.unit.id
        else:
            return (
                self.unit.id
                + "_variant_"
                + str(self.buyable_variant.buyable_variant_num)
            )

    @property
    def livery_num(self):
        if self.buyable_variant._livery_num != None:
            return self.buyable_variant._livery_num
        else:
            return self.buyable_variant.buyable_variant_num

    @property
    def buyable_variant_group_id(self):
        if self.buyable_variant.is_default_buyable_variant:
            return None
        else:
            return self.unit.consist.base_numeric_id


class Train(object):
    """
    Base class for all types of trains
    """

    def __init__(self, **kwargs):
        self.consist = kwargs.get("consist")
        # create an id, which is used for shared switch chains, and as base id for unit variants to construct an id
        if len(self.consist.unique_units) == 0:
            # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
            self.id = self.consist.id
        else:
            self.id = self.consist.id + "_unit_" + str(len(self.consist.unique_units))
        # create structure to hold the buyable variants, done last as may depend on other attrs of self
        self.unit_variants = []
        # vehicle_length is either derived from chassis length or similar, or needs to be set explicitly as kwarg
        self._vehicle_length = kwargs.get("vehicle_length", None)
        self._weight = kwargs.get("weight", None)
        self.capacity = kwargs.get("capacity", 0)
        # spriterow_num allows assigning sprites for multi-part vehicles, and is not supported in all vehicle templates (by design - TMWFTLB to support)
        self.spriterow_num = kwargs.get("spriterow_num", 0)  # first row = 0;
        # sometimes we want to offset the buy menu spriterow (!! this is incomplete hax, not supported by generated buy menu sprites etc)
        self.buy_menu_spriterow_num = (
            0  # set in the subclass as needed, (or extend to kwargs in future)
        )
        # !! the need to copy cargo refits from the consist is legacy from the default multi-unit articulated consists in Iron Horse 1
        # !! could likely be refactored !!
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.autorefit = True
        # nml constant (STEAM is sane default)
        self.engine_class = "ENGINE_CLASS_STEAM"
        # structure for effect spawn and sprites, default and per railtype as needed
        self.effects = {}  # empty if no effects, set in subtypes as needed
        # optional, use to over-ride automatic effect positioning
        # expects a list of offset pairs [(x, y), (x, y)] etc
        # n.b max 4 effects (nml limit)
        self._effect_offsets = kwargs.get("effect_offsets", None)
        # z offset is rarely used and is handled separately, mostly just for low-height engines
        self._effect_z_offset = kwargs.get("effect_z_offset", None)
        self.default_effect_z_offset = (
            12  # optimised for Pony diesel and electric trains
        )
        # optional - only set if the graphics processor generates the vehicle chassis
        self.chassis = kwargs.get("chassis", None)
        # optional - occasionally we need to suppress composited roof sprites and just draw our own
        self.suppress_roof_sprite = kwargs.get("suppress_roof_sprite", False)
        # optional - some engine units need to set explicit tail light spritesheets
        # subclasses may over-ride this, e.g. wagons have an automatic tail light based on vehicle length
        self.tail_light = kwargs.get("tail_light", "empty")
        # 'symmetric' or 'asymmetric'?
        # defaults to symmetric, over-ride in sub-classes or per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "symmetric")
        # optional - a switch name to trigger re-randomising vehicle random bits - over-ride as need in subclasses
        self.random_trigger_switch = None

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [
            int(math.ceil(capacity * multiplier))
            for multiplier in global_constants.capacity_multipliers
        ]

    @property
    def capacities(self):
        return self.get_capacity_variations(self.capacity)

    @property
    def default_cargo_capacity(self):
        return self.capacities[2]

    @property
    def has_cargo_capacity(self):
        if self.default_cargo_capacity != 0:
            return True
        else:
            return False

    def get_pax_car_capacity(self):
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        result = int(
            self.vehicle_length
            * base_capacity
            * self.consist.pax_car_capacity_type["multiplier"]
        )
        return result

    @property
    def weight(self):
        # weight can be set explicitly or by methods on subclasses
        return self._weight

    @property
    def vehicle_length(self):
        # length of this unit, either derived from from chassis length, or set explicitly via keyword
        # first guard that one and only one of these props is set
        if self._vehicle_length is not None and self.chassis is not None:
            utils.echo_message(
                self.consist.id
                + " has units with both chassis and length properties set"
            )
        if self._vehicle_length is None and self.chassis is None:
            utils.echo_message(
                self.consist.id
                + " has units with neither chassis nor length properties set"
            )

        if self.chassis is not None:
            # assume that chassis name format is 'foo_bar_ham_eggs_24px' or similar - true as of Nov 2020
            # if chassis name format changes / varies in future, just update the string slice accordingly, safe enough
            # splits on _, then takes last entry, then slices to remove 'px'
            result = int(self.chassis.split("_")[-1][0:-2])
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
        if self.consist.units.index(self) == 0:
            return True
        else:
            return False

    @property
    def symmetry_type(self):
        assert self._symmetry_type in [
            "symmetric",
            "asymmetric",
        ], "symmetry_type '%s' is invalid in %s" % (
            self._symmetry_type,
            self.consist.id,
        )
        return self._symmetry_type

    @property
    def misc_flags(self):
        # note that there are both misc_flags and extra_flags, for grf_spec reasons
        misc_flags = ["TRAIN_FLAG_2CC", "TRAIN_FLAG_SPRITE_STACK"]
        if self.consist.allow_flip:
            misc_flags.append("TRAIN_FLAG_FLIP")
        if self.autorefit:
            misc_flags.append("TRAIN_FLAG_AUTOREFIT")
        if self.consist.tilt_bonus:
            misc_flags.append("TRAIN_FLAG_TILT")
        if self.consist.train_flag_mu:
            misc_flags.append("TRAIN_FLAG_MU")
        return ",".join(misc_flags)

    def get_extra_flags(self, unit_variant):
        extra_flags = []
        if unit_variant.buyable_variant_group_id is not None:
            extra_flags.append("VEHICLE_FLAG_DISABLE_NEW_VEHICLE_MESSAGE")
            extra_flags.append("VEHICLE_FLAG_SYNCHRONISE_VARIANT_EXCLUSIVE_PREVIEW")
            extra_flags.append("VEHICLE_FLAG_SYNCHRONISE_VARIANT_RELIABILITY")
        return ",".join(extra_flags)

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        if hasattr(self, "articulated_unit_different_class_refit_groups"):
            # in *rare* cases an articulated unit might need different refit classes to its parent consist
            class_refit_groups = self.articulated_unit_different_class_refit_groups
        else:
            # by default get the refit classes from the consist
            class_refit_groups = self.consist.class_refit_groups
        for i in class_refit_groups:
            [
                cargo_classes.append(cargo_class)
                for cargo_class in global_constants.base_refits_by_class[i]
            ]
        return ",".join(set(cargo_classes))  # use set() here to dedupe

    @property
    def loading_speed(self):
        # ottd vehicles load at different rates depending on type, train default is 5
        # Iron Horse uses 5 as default, with some vehicle types adjusting that up or down
        return int(5 * self.consist.loading_speed_multiplier)

    @property
    def running_cost_base(self):
        # all engines use the same RUNNING_COST_STEAM, and Iron Horse provides the variation between steam/electric/diesel
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # wagons will use RUNNING_COST_DIESEL - set in wagon subclass
        return "RUNNING_COST_STEAM"

    def get_offsets(self, flipped=False):
        # offsets can also be over-ridden on a per-model basis by providing this property in the model class
        base_offsets = global_constants.default_spritesheet_offsets[
            str(self.vehicle_length)
        ]
        if flipped:
            flipped_offsets = list(base_offsets[4:8])
            flipped_offsets.extend(base_offsets[0:4])
            return flipped_offsets
        else:
            return base_offsets

    @property
    def vehicle_nml_template(self):
        # optionally drop the cargos in the compile, can save substantial compile time
        if utils.get_command_line_args().suppress_cargo_sprites:
            return "vehicle_default.pynml"

        if self.consist.gestalt_graphics.nml_template:
            return self.consist.gestalt_graphics.nml_template
        # default case
        return "vehicle_default.pynml"

    @property
    def roof(self):
        # fetch spritesheet name to use for roof when generating graphics
        if self.consist.roof_type is not None:
            if self.consist.base_track_type_name == "NG":
                ng_prefix = "ng_"
            else:
                ng_prefix = ""
            return (
                str(4 * self.vehicle_length)
                + "px_"
                + ng_prefix
                + self.consist.roof_type
            )
        else:
            return None

    @property
    def requires_colour_mapping_cb(self):
        # bit weird and janky, various conditions to consider eh
        if getattr(self.consist, "use_colour_randomisation_strategies", False):
            return "use_colour_randomisation_strategies"
        elif (
            getattr(self.consist.gestalt_graphics, "colour_mapping_switch", None)
            is not None
        ):
            if self.consist.gestalt_graphics.colour_mapping_with_purchase:
                return "colour_mapping_switch_with_purchase"
            else:
                return "colour_mapping_switch_without_purchase"
        else:
            return None

    @property
    def effects_vary_by_power_source(self):
        # simple check if more than one type of effect is defined
        return len(self.effects) > 1

    @property
    def default_effect_offsets(self):
        # over-ride this in subclasses as needed (e.g. to move steam engine smoke to front by default
        # vehicles can also over-ride this on init (stored on each model_variant as _effect_offsets)
        return [(0, 0)]

    def get_nml_expression_for_effects(self, reversed_variant, railtype="default"):
        # provides part of nml switch for effects (smoke)

        # effects can be over-ridden per vehicle, or use a default from the vehicle subclass
        if self._effect_offsets is not None:
            effect_offsets = self._effect_offsets
        else:
            effect_offsets = self.default_effect_offsets

        # when vehicles (e.g. steam engines) are reversed, invert the effect x position
        if reversed_variant == "reversed":
            effect_offsets = [
                (offsets[0] * -1, offsets[1]) for offsets in effect_offsets
            ]

        # z offset is handled independently to x, y for simplicity, option to over-ride z offset default per vehicle
        if self._effect_z_offset is not None:
            z_offset = self._effect_z_offset
        else:
            z_offset = self.default_effect_z_offset

        # changing sprite by railtype is supported, changing position is *not* as of August 2019
        effect_sprite = self.effects[railtype][1]

        result = []
        for index, offset_pair in enumerate(effect_offsets):
            items = [
                effect_sprite,
                str(offset_pair[0]),
                str(offset_pair[1]),
                str(z_offset),
            ]
            result.append(
                "STORE_TEMP(create_effect("
                + ",".join(items)
                + "), 0x10"
                + str(index)
                + ")"
            )
        return [
            "[" + ",".join(result) + "]",
            str(len(result)) + " + CB_RESULT_CREATE_EFFECT_CENTER",
        ]

    @property
    def switch_id_for_create_effect(self):
        # randomly reversed vehicles need to use a dependent random switch, this doesn't exist for non-reversible vehicles, so need to conditionally handle switch routing
        if len(self.consist.reversed_variants) > 1:
            return self.id + "_switch_create_effect_reversed_variants"
        else:
            return (
                self.id
                + "_switch_create_effect_check_railtype_"
                + self.consist.reversed_variants[0]
            )

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]"
        )
        return expression_template.substitute(unit_offset=unit_offset)

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # best used with the check for same grfid, but eh
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]"
        )
        return expression_template.substitute(unit_offset=unit_offset)

    def get_spriteset_template_name(self, reversed, flipped, y):
        template_name = "_".join(
            [
                "spriteset_template",
                self.symmetry_type,
                reversed,
                str(self.vehicle_length),
                "8",
                flipped,
            ]
        )
        anim_flag = (
            "ANIM" if self.consist.suppress_animated_pixel_warnings else "NOANIM"
        )
        args = ",".join([str(y), anim_flag])
        return template_name + "(" + args + ")"

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ",".join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ",".join(self.label_refits_disallowed)

    def get_cargo_suffix(self):
        return "string(" + self.cargo_units_refit_menu + ")"

    def assert_random_reverse(self):
        # some templates don't support the random_reverse (by design, they're symmetrical sprites, and reversing bloats the template)
        if self.consist.random_reverse:
            if hasattr(self.consist, "gestalt_graphics"):
                for nml_template in [
                    "vehicle_with_visible_cargo.pynml",
                    "vehicle_box_car_with_opening_doors.pynml",
                    "vehicle_with_cargo_specific_liveries.pynml",
                    "vehicle_consist_position_dependent.pynml",
                ]:
                    assert self.consist.gestalt_graphics.nml_template != nml_template, (
                        "%s has 'random_reverse set True, which isn't supported by nml_template %s"
                        % (self.consist.id, nml_template)
                    )

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message(
                    "Warning: vehicle "
                    + self.id
                    + " references cargo label "
                    + i
                    + " which is not defined in the cargo table"
                )

    def render(self, templates, graphics_path):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        self.assert_random_reverse()
        # test interpolated gen and intro_year
        assert self.consist.gen, (
            "%s consist.gen is None, which is invalid.  Set gen or intro_year" % self.id
        )
        assert self.consist.intro_year, (
            "%s consist.gen is None, which is invalid.  Set gen or intro_year" % self.id
        )
        # templating
        template_name = self.vehicle_nml_template
        template = templates[template_name]
        nml_result = template(
            vehicle=self,
            consist=self.consist,
            global_constants=global_constants,
            temp_storage_ids=global_constants.temp_storage_ids,  # convenience measure
            graphics_path=graphics_path,
            spritelayer_cargos=spritelayer_cargos,
        )
        return nml_result


class AutoCoachCombineUnitMail(Train):
    """
    Mail unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self.effects = {}
        self._symmetry_type = "asymmetric"
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = [
            "mail"
        ]  # note mail only, no other express cargos
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        # also account for some pax capacity 'on' this unit (implemented on adjacent pax unit)
        self.capacity = (
            0.75 * self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class AutoCoachCombineUnitPax(Train):
    """
    Pax unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # !! needs changing??
        self.effects = {}
        self._symmetry_type = "asymmetric"
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = ["pax"]
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class CabbageDVTUnit(Train):
    """
    Unit for a DVT / Cabbage (driving cab with mail capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self.effects = {}
        self._symmetry_type = "asymmetric"
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class CabControlPaxCarUnit(Train):
    """
    Unit for a cab control car (driving cab with pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self.effects = {}
        self._symmetry_type = "asymmetric"
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class BatteryHybridEngineUnit(Train):
    """
    Unit for a battery hybrid engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self.effects = {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_STEAM"]}
        # most battery hybrid engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")


class DieselEngineUnit(Train):
    """
    Unit for a diesel engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]
        }
        # most diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")


class DieselRailcarBaseUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to set symmetry.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # the cab magic won't work unless it's asymmetric eh? :)
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")
        # note that railcar effects are left in default position, no attempt to move them to end of vehicle, or double them (tried, looks weird)


class DieselRailcarMailUnit(DieselRailcarBaseUnit):
    """
    Unit for a mail diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class DieselRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class ElectricEngineUnit(Train):
    """
    Unit for an electric engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }
        # almost all electric engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")


class ElectricHighSpeedUnitBase(Train):
    """
    Unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }
        self._symmetry_type = "asymmetric"


class ElectricHighSpeedMailUnit(ElectricHighSpeedUnitBase):
    """
    Mail unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class ElectricHighSpeedPaxUnit(ElectricHighSpeedUnitBase):
    """
    Passenger unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set high speed pax car capacity subject to length
        # this won't work with double deck high speed in future, extend a class for that then if needed
        self.capacity = self.get_pax_car_capacity()


class ElectroDieselEngineUnit(Train):
    """
    Unit for a bi-mode Locomotive - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1  # will get same buy cost factor as electric engine of same gen (blah balancing)
        # almost all electro-diesel engines are asymmetric, over-ride per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")


class ElectroDieselRailcarBaseUnit(Train):
    """
    Unit for a bi-mode railcar - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1.15  # will get higher buy cost factor than electric railcar of same gen (blah balancing)
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2  # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = 2  # frankly hax at this point :|
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"


class ElectroDieselRailcarMailUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a mail electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class ElectroDieselExpressRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel express railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class ElectricRailcarBaseUnit(Train):
    """
    Unit for an electric railcar.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"


class ElectricExpressRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a express pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class ElectricRailcarMailUnit(ElectricRailcarBaseUnit):
    """
    Unit for a mail electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2  # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = (
            self.buy_menu_spriterow_num
        )  # frankly hax at this point :|


class ElectricRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a pax electric railcar.  Just a sparse subclass to set capacity and force the second livery to be used via dubious means.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()
        # offset to second livery, to differentiate from diesel equivalent which will use first
        self.buy_menu_spriterow_num = 2  # note that it's 2 because opening doors are in row 1, livery 2 starts at 2, zero-indexed
        self.consist.docs_image_spriterow = (
            self.buy_menu_spriterow_num
        )  # frankly hax at this point :|


class MetroUnit(Train):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs["consist"].base_track_type_name = "METRO"
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.effects = {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }
        self.default_effect_z_offset = (
            1  # optimised for Pony diesel and electric trains
        )
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"


class SnowploughUnit(Train):
    """
    Unit for a snowplough.  Snowploughs have express cargo capacity, so they can actually be useful. :P
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # !! needs changing??
        self.effects = {}
        self._symmetry_type = "asymmetric"
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class SteamEngineUnit(Train):
    """
    Unit for a steam engine, with smoke
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self.effects = {"default": ["EFFECT_SPAWN_MODEL_STEAM", "EFFECT_SPRITE_STEAM"]}
        self.default_effect_z_offset = 13  # optimised for Pony steam trains
        self._symmetry_type = "asymmetric"  # assume all steam engines are asymmetric

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
        self._symmetry_type = "asymmetric"


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
        self.consist = kwargs["consist"]
        # most wagons are symmetric, over-ride per vehicle or subclass as needed
        self._symmetry_type = kwargs.get("symmetry_type", "symmetric")
        # all wagons use auto tail-lights based on length
        self.tail_light = str(self.vehicle_length * 4) + "px"

    @property
    def running_cost_base(self):
        # all wagons use the same RUNNING_COST_DIESEL, this is nerfed down to give appropriate increments for low wagon run costs
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # engines will all use RUNNING_COST_STEAM
        return "RUNNING_COST_DIESEL"

    @property
    def weight(self):
        # set weight based on capacity  * a multiplier from consist * roster gen factor
        return int(
            self.consist.weight_factor
            * self.default_cargo_capacity
            * self.consist.roster.train_car_weight_factors[self.consist.gen - 1]
        )


class AlignmentCar(TrainCar):
    """
    Alignment Car, for debugging sprite positions
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


class CabooseCar(TrainCar):
    """
    Caboose Car. This sub-class only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # caboose cars may be asymmetric, they are also user-flippable as of August 2022 (flip also toggles CC)
        self._symmetry_type = "asymmetric"

    @property
    def weight(self):
        # special handling of weight
        weight_factor = 3 if self.consist.base_track_type_name == "NG" else 5
        return weight_factor * self.vehicle_length


class PaxCar(TrainCar):
    """
    Pax wagon. This subclass only exists to set capacity and symmetry_type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"
        # magic to set capacity subject to length and vehicle capacity type
        self.capacity = self.get_pax_car_capacity()


class PaxRailcarTrailerCar(PaxCar):
    """
    Railcar (or railbus) unpowered pax trailer. This subclass only exists to set tail light
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TrainCar sets auto tail light, over-ride it
        self.tail_light = kwargs["tail_light"]  # fail if not passed, required arg


class PaxRestaurantCar(PaxCar):
    """
    Restaurant (special) pax wagon. This subclass only exists to set special weight handling
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def weight(self):
        # special handling of weight - let's just use 37 + gen for Pony, split that later for other rosters if needed
        return 37 + self.consist.gen


class ExpressCar(TrainCar):
    """
    Express freight car.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = (
            self.vehicle_length * base_capacity
        ) / polar_fox.constants.mail_multiplier


class ExpressIntermodalCar(ExpressCar):
    """
    Express container car, subclassed from express car.  This subclass only exists to symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # express intermodal cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class ExpressMailCar(ExpressCar):
    """
    Mail wagon, subclassed from express car.  Only exists to set symmetry_type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # mail wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = "asymmetric"


class AutomobileCarAsymmetric(ExpressCar):
    """
    Automobile (cars, trucks, tractors) transporter car, subclassed from express car.
    This subclass exists to symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # some vehicle transporter cars are asymmetric
        self._symmetry_type = "asymmetric"
        utils.echo_message(
            "AutomobileCarAsymmetric random_trigger_switch is using _switch_graphics_spritelayer_cargos "
            + self.consist.id
        )
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class AutomobileCarSymmetric(ExpressCar):
    """
    Automobile (cars, trucks, tractors) transporter car, subclassed from express car.
    This subclass exists to symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # some vehicle transporter cars are symmetric
        self._symmetry_type = "symmetric"
        utils.echo_message(
            "AutomobileCarAsymmetric random_trigger_switch is using _switch_graphics_spritelayer_cargos "
            + self.consist.id
        )
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class FreightCar(TrainCar):
    """
    Freight wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs.get("capacity", None) is not None:
            print(
                self.consist.id,
                " has a capacity set in init - possibly incorrect",
                kwargs.get("capacity", None),
            )
        # magic to set freight car capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        self.capacity = self.vehicle_length * base_capacity


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
        self._symmetry_type = "asymmetric"
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class OreDumpCar(FreightCar):
    """
    Ore dump car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


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
        self._symmetry_type = "asymmetric"
        # capacity bonus is solely to support using small stations in Steeltown where space between industries is constrained
        self.capacity = 1.5 * self.capacity
