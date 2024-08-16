import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import copy
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
        # rosters can optionally reuse wagon modules from other rosters, if so, store the roster_id of the origin module (otherwise roster_id is same)
        self.roster_id_providing_module = kwargs.get(
            "roster_id_providing_module", self.roster_id
        )
        # create a structure to hold buyable variants - the method can be over-ridden in consist subclasses to provide specific rules for buyable variants
        # we start empty, and rely on add_unit to populate this later, which means we can rely on gestalt_graphics having been initialised
        # otherwise we're trying to initialise variants before we have gestalt_graphics, and that's a sequencing problem
        self.buyable_variants = []
        # variant group id options are set in subclasses; supported methods are cascading:
        # set explicitly to a named group matching a consist id
        # set explicitly to a base id, for e.g. wagon groups defined on the roster, which will then compose a group name using e.g. consist track type, gen etc
        # or implicitly inferred later from rules for e.g. livery variants
        self._buyable_variant_group_id = kwargs.get("buyable_variant_group_id", None)
        self.use_named_buyable_variant_group = None
        # create a structure to hold the units
        self.units = []
        # we clone some consists to make alternate length variants, we need to track that
        self.clones = []
        # store the consist this was cloned from, may also be used to determine if this is a clone or not
        self.cloned_from_consist = None
        # either gen xor intro_year is required, don't set both, one will be interpolated from the other
        self._intro_year = kwargs.get("intro_year", None)
        self._gen = kwargs.get("gen", None)
        # override this in subclasses if needed, there's no case currently for setting it via keyword
        self._model_life = None
        # if gen is used, the calculated intro year can be adjusted with +ve or -ve offset
        self.intro_year_offset = kwargs.get("intro_year_offset", None)
        # used for synchronising / desynchronising intro dates for groups vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147
        self._intro_year_days_offset = (
            None  # defined in subclasses, no need for instances to define this
        )
        # vehicle life uses a default value, but can be extended automatically via a bool keyword, or it can be set manually
        self.extended_vehicle_life = kwargs.get("extended_vehicle_life", False)
        self._vehicle_life = kwargs.get("vehicle_life", None)
        #  most consists are automatically replaced by the next consist in the role tree
        # ocasionally we need to merge two branches of the role, in this case set replacement consist id
        self._replacement_consist_id = kwargs.get("replacement_consist_id", None)
        # default loading speed multiplier, override in subclasses as needed
        self._loading_speed_multiplier = 1
        self.base_track_type_name = kwargs.get("base_track_type_name", "RAIL")
        # modify base_track_type_name for electric engines when writing out the actual rail type
        # without this, RAIL and ELRL have to be specially handled whenever a list of compatible consists is wanted
        self.tractive_effort_coefficient = kwargs.get(
            "tractive_effort_coefficient", 0.3
        )  # 0.3 is recommended default value
        # private var, can be used to overrides default (per generation, per class) speed
        self._speed = kwargs.get("speed", None)
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.power_by_power_source = kwargs.get("power_by_power_source", None)
        # some engines require pantograph sprites composited, don't bother setting this unless required
        self.pantograph_type = kwargs.get("pantograph_type", None)
        # some consists don't show pans in the buy menu (usually unpowered)
        self.suppress_pantograph_if_no_engine_attached = False
        # some engines have an optional decor layer, which is a manual spriterow num (as decor might not be widely used?)
        self.decor_spriterow_num = kwargs.get("decor_spriterow_num", None)
        # stupid extra-detail, control which variants show decor in purchase menu
        self.show_decor_in_purchase_for_variants = kwargs.get(
            "show_decor_in_purchase_for_variants", []
        )
        self.dual_headed = kwargs.get("dual_headed", False)
        self.tilt_bonus = kwargs.get("tilt_bonus", False)
        self.lgv_capable = kwargs.get("lgv_capable", False)
        self.requires_high_clearance = kwargs.get("requires_high_clearance", False)
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        self.buy_menu_additional_text_hint_wagons_add_power = False
        # wagons can be candidates for the magic randomised wagons
        # this is on Consist not CarConsist as we need to check it when determining order for all consists
        self.randomised_candidate_groups = []
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        self.easter_egg_haulage_speed_bonus = kwargs.get(
            "easter_egg_haulage_speed_bonus", False
        )
        # engines will automatically detemine role string, but to force it on certain coach/wagon types use _buy_menu_additional_text_role_string
        self._buy_menu_additional_text_role_string = None
        # simple buy menu hint flag for driving cabs
        self.buy_menu_additional_text_hint_driving_cab = False
        # simple buy menu hint flag for restaurant cars
        self.buy_menu_additional_text_hint_restaurant_car = False
        # option to force a specific name suffix, if the auto-detected ones aren't appropriate
        self._str_name_suffix = None
        # random_reverse means (1) randomised flip of vehicle when built (2) player can also flip vehicle manually
        # random_reverse is not supported in some templates
        self.random_reverse = kwargs.get("random_reverse", False)
        # just a simple buy cost tweak, only use when needed
        self.electro_diesel_buy_cost_malus = None
        # arbitrary multiplier to the calculated buy cost, e.g. 1.1, 0.9 etc
        # set to 1 by default, override in subclasses as needed
        self.buy_cost_adjustment_factor = 1
        # fixed (baseline) buy costs on this subtype, 10 points
        # leave this alone except for edge cases (e.g. driving van trailers which are implemented as engines, but need wagon costs)
        self.fixed_buy_cost_points = 10
        # arbitrary multiplier to the calculated run cost, e.g. 1.1, 0.9 etc
        # set to 1 by default, override in subclasses as needed
        self.floating_run_cost_multiplier = 1
        # fixed (baseline) run costs on this subtype, 100 points
        self.fixed_run_cost_points = 30  # default, override in subclass as needed
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
        # 0 indexed spriterows, position in generated spritesheet, used by brake vans to get a docs image for 4th gen, not 1st
        self.docs_image_spriterow = kwargs.get("docs_image_spriterow", None)
        # aids 'project management'
        self.sprites_complete = kwargs.get("sprites_complete", False)
        self.sprites_additional_liveries_potential = kwargs.get(
            "sprites_additional_liveries_potential", False
        )

    def clone(self, **kwargs):
        # consists have support for optional clones, which are used to provide variants of different lengths
        # e.g. diesels with 1 or 2 units, and similar
        # a consist can have more than one clone variant
        # parameters
        # - base_numeric_id: (int) used for the cloned consist
        # - clone_units: [repeat=n1, repeat=n2] etc for each unit defined in the original consist
        # so to extend a 1 unit consist to a 2 unit variant: clone_units=[2]
        # to shorten a 2 unit consist to a 1 unit variant: clone_units=[1, 0]

        # we clone the consist by copying the current consist, this is the simplest way to not get caught out by any properties in subclasses
        cloned_consist = copy.deepcopy(self)
        cloned_consist.cloned_from_consist = self
        cloned_consist.id = self.id + "_clone_" + str(len(self.clones))
        cloned_consist.base_numeric_id = kwargs["base_numeric_id"]
        cloned_consist._buyable_variant_group_id = self.id
        # purchase menu variant decor isn't supported if the consist is articulated, so just forcibly clear this property
        cloned_consist.show_decor_in_purchase_for_variants = []
        # we have to recreate the units from scratch using the original classes and kwargs stored when they were inited
        # this is faff, but is the simplest available method due to the way the structure for units + buyable_variants is constructed and unit_variant IDs assigned
        cloned_consist.units = []
        for counter, unit in enumerate(self.units):
            unit_kwargs = unit.kwargs_for_optional_consist_cloning_later.copy()
            del unit_kwargs[
                "consist"
            ]  # drop this, it's re-added to kwargs later by add_unit, which will cause an error to be thrown
            cloned_consist.add_unit(
                type(unit), repeat=kwargs["clone_units"][counter], **unit_kwargs
            )
        cloned_consist.set_clone_power_from_clone_source()
        self.clones.append(cloned_consist)
        # no return needed

    @property
    def clone_stats_adjustment_factor(self):
        # clones need to adjust some stats, e.g. power, running_cost etc
        return len(self.units) / len(self.cloned_from_consist.units)

    def set_clone_power_from_clone_source(self):
        # recalculate power for a clone, adjusting by num units or other factor
        for (
            power_type,
            power_value,
        ) in self.cloned_from_consist.power_by_power_source.items():
            self.power_by_power_source[power_type] = int(
                power_value * self.clone_stats_adjustment_factor
            )
        # no return needed

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
            # !! this is suspect, it's not counting the actual number of liveries
            if len(self.gestalt_graphics.all_liveries) > 1:
                result.append(unit + 1)
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

    def get_name_parts(self, context, unit_variant):
        default_name = "STR_NAME_" + self.id.upper()
        if context == "purchase_level_1":
            result = [default_name]
        elif context == "default_name":
            result = [default_name]
        else:
            if self.str_name_suffix is not None:
                result = [
                    "STR_NAME_" + self.id.upper(),
                    "STR_PARENTHESES",
                    self.str_name_suffix,
                ]
            else:
                result = [default_name]
        return result

    def get_name_as_text_stack(self, context, unit_variant):
        stack_items = self.get_name_parts(context=context, unit_variant=unit_variant)

        # we need to know how many strings we have to handle, so that we can provide a container string with correct number of {STRING} entries
        # this is non-trivial as we might have non-string items for the stack (e.g. number or procedure results), used by a preceding substring
        string_counter = 0
        for stack_item in stack_items:
            if stack_item[0:4] == "STR_":
                string_counter += 1
        if string_counter > 1:
            stack_items.insert(0, "STR_NAME_CONTAINER_" + str(string_counter))

        result = []
        for stack_item in stack_items:
            if stack_item[0:4] == "STR_":
                # possibly fragile wrapping of string() around strings, to avoid having to always specify them that way
                result.append("string(" + stack_item + ")")
            else:
                # otherwise pass through as is
                result.append(stack_item)
        return result
        # return utils.convert_flat_list_to_pairs_of_tuples(result)

    def get_name_as_property(self, unit_variant):
        # text filter in buy menu needs name as prop as of June 2023
        # this is very rudimentary and doesn't include all the parts of the name
        name_parts = self.get_name_parts(
            context="default_name", unit_variant=unit_variant
        )
        result = "string(" + name_parts[0] + ")"
        return result

    def engine_varies_power_by_power_source(self, vehicle):
        # note that we use self.cab_id to eliminate trailer cars from this (which use power_by_power_source to manage pantographs), this is JFDI and may need refactored in future
        if (
            (self.power_by_power_source is not None)
            and (vehicle.is_lead_unit_of_consist)
            and (getattr(self, "cab_consist", None) is None)
        ):
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
        # vehicle classes should override this to provide class-appropriate cost calculation
        return 0

    @property
    def running_cost(self):
        # stub only
        # vehicle classes should override this to provide class-appropriate running cost calculation
        return 0

    @property
    def intro_year(self):
        # automatic intro_year, but can override by passing in kwargs for consist
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
                and (consist.cloned_from_consist is None)
                and (getattr(consist, "cab_id", None) is None)
            ):
                if (
                    (consist.role == self.role)
                    or (0 <= (consist.power - self.power) < 500)
                    or (0 <= (self.power - consist.power) < 500)
                ):
                    result.append(consist)
        return result

    @property
    def cab_consist(self):
        # fetch the consist for the cab engine
        for engine_consist in self.roster.engine_consists:
            if engine_consist.id == self.cab_id:
                return engine_consist

    @property
    def dedicated_trailer_consists(self):
        # fetch dedicated trailer consists for this cab engine (if any)
        result = []
        for consists in [
            self.roster.engine_consists_excluding_clones,
            self.roster.wagon_consists,
        ]:
            for consist in consists:
                if getattr(consist, "cab_id", None) == self.id:
                    result.append(consist)
        return result

    @property
    def vehicle_life(self):
        if self._vehicle_life is not None:
            # allow vehicles to provide a vehicle life if they want
            return self._vehicle_life
        if self.extended_vehicle_life:
            lifespan = 60
        else:
            lifespan = 40
        if self.replacement_consist is not None:
            time_to_replacement = self.replacement_consist.intro_year - self.intro_year
            if time_to_replacement > lifespan:
                # round to nearest 10, then add some padding
                return time_to_replacement - (time_to_replacement % 10) + 10
            else:
                return lifespan
        else:
            # pick a sensible value for vehicles that don't otherwise get replaced
            return lifespan

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
        if "METRO" in self.power_by_power_source.keys():
            result.append(["METRO", self.base_track_type_name])
        if "BATTERY_HYBRID" in self.power_by_power_source.keys():
            result.append(["BATTERY_HYBRID", self.base_track_type_name])
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
        # automatic speed, but can override by passing in kwargs for consist
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
            # !! this would be better determined by setting self.speed_class appropriately in the consist subclasses
            if self.role in ["mail_railcar", "pax_railcar", "pax_railbus"]:
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
        for role_group_mapping_key in [
            "express",
            "driving_cab",
            "express_railcar",
            "high_power_railcar",
        ]:
            group_roles = global_constants.role_group_mapping[role_group_mapping_key]
            if self.role in group_roles:
                return self.get_speed_by_class("express_on_lgv")

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
        # override in subclass as needed
        return self._loading_speed_multiplier

    @property
    def is_general_purpose_true_wagon(self):
        # all engines have power
        # all true wagons don't
        # wagons that add power aren't true wagons
        # some subclasses handle this directly (e.g. pax trailers for specific railcars)
        if self.power > 0:
            return False
        elif self.wagons_add_power:
            return False
        else:
            return True

    @property
    def is_randomised_wagon_type(self):
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
    def requires_custom_buy_menu_sprite(self):
        # boolean check for whether we'll need a custom buy menu sprite, or if we can default to just using 6th angle of vehicle
        if len(self.units) > 1:
            # custom buy menu sprite for articulated vehicles
            return True
        elif self.is_randomised_wagon_type or self.is_caboose:
            return True
        elif self.dual_headed:
            return True
        else:
            return False

    @property
    def buy_menu_x_loc(self):
        if self.requires_custom_buy_menu_sprite:
            # always x = 360 for custom buy menu sprites (y is calculated elsewhere for variant livery etc)
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
    def engine_sprite_layers_with_layer_names(self):
        result = []
        counter = 0
        # always append the base engine layer
        result.append((counter, "base"))
        # add a layer for decor as needed, note this is not done in the gestalt as it's more convenient to treat separarely
        if self.decor_spriterow_num is not None:
            # guard against the decor spriterow not being updated when liveries are added
            if self.decor_spriterow_num <= len(self.gestalt_graphics.liveries) - 1:
                raise BaseException(
                    self.id
                    + " has decor_spriterow_num "
                    + str(self.decor_spriterow_num)
                    + " and also "
                    + str(len(self.gestalt_graphics.liveries) - 1)
                    + " additional liveries defined. This will cause vehicle sprites to be incorrectly shown as decor."
                )
            # if guard passes...
            counter = counter + 1
            result.append((counter, "decor"))
        # add a layer for pantographs as needed, note this is not done in the gestalt as it's more convenient to treat separarely
        if self.pantograph_type is not None:
            counter = counter + 1
            result.append((counter, "pantographs"))
        return result

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
        # add a layer for decor as needed, note this is not done in the gestalt as it's more convenient to treat separarely
        if self.decor_spriterow_num is not None:
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

    def get_wagon_recolour_strategy_num(self, livery, context=None):
        # > 103 = strategy num will be randomised to one of the other strategy nums
        # 101 = use colour set complementary to player company colour
        # 100 = use colour set from player company colour
        # 0..99 = use colour set number directly (look up by name)
        if context == "purchase":
            colour_set = livery["purchase"]
        else:
            colour_set = livery["colour_set"]
        # this is lolz, so many ifs just to get a string -> number mapping
        if "random_from_consist_liveries_12" in colour_set:
            return 114
        if "random_from_consist_liveries_11" in colour_set:
            return 113
        elif "random_from_consist_liveries_10" in colour_set:
            return 112
        elif "random_from_consist_liveries_9" in colour_set:
            return 111
        elif "random_from_consist_liveries_8" in colour_set:
            return 110
        elif "random_from_consist_liveries_7" in colour_set:
            return 109
        elif "random_from_consist_liveries_6" in colour_set:
            return 108
        elif "random_from_consist_liveries_5" in colour_set:
            return 107
        elif "random_from_consist_liveries_4" in colour_set:
            return 106
        elif "random_from_consist_liveries_3" in colour_set:
            return 105
        elif "random_from_consist_liveries_2" in colour_set:
            return 104
        elif "random_from_consist_liveries_1" in colour_set:
            return 103
        # 102 left empty for legacy reasons as of May 2023, should be refactored really
        elif "complement_company_colour" in colour_set:
            return 101
        elif "company_colour" in colour_set:
            return 100
        else:
            return list(global_constants.colour_sets.keys()).index(colour_set)

    def get_candidate_liveries_for_randomised_strategy(self, livery):
        # this will only work with wagon liveries as of April 2023, and is intended to get remaps only
        result = []
        for candidate_livery in self.gestalt_graphics.all_liveries:
            if (
                candidate_livery["colour_set"]
                in global_constants.wagon_livery_mixes[livery["colour_set"]]
            ):
                candidate_livery_strategy_num = self.get_wagon_recolour_strategy_num(
                    candidate_livery
                )
                result.append(candidate_livery_strategy_num)
        # length of result *must* be 8, as we have up to 8 liveries per buyable wagon variant, and we must provide values for 8 registers
        # this just crudely extends the list, repeating values as needed
        extension = result[0 : 8 - len(result)]
        if len(extension) == 0:
            raise BaseException(
                self.id
                + " get_candidate_liveries_for_randomised_strategy: extension list too short "
                + str(extension)
                + "; \n this is probably because we're slicing 8, and have more than 8 colours defined; which will fail;"
                + "; \n there are now more random bits available for OpenTTD 14 so this might be solvable"
            )
        # !! it's possible this doesn't close
        while len(result) < 8:
            result.extend(extension)
        # yes, I'm sure we could avoid over-extending and then slicing the list, but eh, life is short
        if (len(result)) > 8:
            result = result[0:8]
        return result

    def get_buy_menu_additional_text(self, vehicle, unit_variant=None):
        result = []
        # optional string if engine varies power by railtype
        if self.engine_varies_power_by_power_source(vehicle):
            if len(self.power_by_power_source) == 2:
                result.append("STR_POWER_BY_POWER_SOURCE_TWO_SOURCES")
            elif len(self.power_by_power_source) == 3:
                result.append("STR_POWER_BY_POWER_SOURCE_THREE_SOURCES")
            else:
                raise BaseException(
                    "consist "
                    + self.id
                    + " defines unsupported number of power sources"
                )
        # optional string if consist is lgv-capable
        if self.lgv_capable:
            result.append("STR_SPEED_BY_RAILTYPE_LGV_CAPABLE")
        # optional string if dedicated wagons add power
        if self.buy_menu_additional_text_hint_wagons_add_power:
            result.append(self.buy_menu_additional_text_distributed_power_substring)

        # engines will always show a role string
        # !! this try/except is all wrong, I just want to JFDI to add buy menu strings to wagons which previously didn't support them, and can do regret later
        # !! this may not be used / or required as of April 2021 - _buy_menu_additional_text_role_string is available instead
        try:
            result.append(self.buy_menu_additional_text_role_string)
        except:
            pass

        # driving cab hint comes after role string
        if self.buy_menu_additional_text_hint_driving_cab:
            result.append("STR_BUY_MENU_ADDITIONAL_TEXT_HINT_DRIVING_CAB")

        # driving cab hint comes after role string
        if self.buy_menu_additional_text_hint_restaurant_car:
            # this roster and generation specific check is definition of BAD FEATURE, but eh, regrets later?
            if self.roster_id == "pony" and self.gen == 5:
                result.append(
                    "STR_BUY_MENU_ADDITIONAL_TEXT_HINT_RESTAURANT_CAR_EXTENDED"
                )
            else:
                result.append("STR_BUY_MENU_ADDITIONAL_TEXT_HINT_RESTAURANT_CAR")

        # livery variants comes after role string
        if unit_variant is not None:
            # as of May 2023 get_buy_menu_additional_text is never called with a variant in scope unless the variant requires this string
            # so no conditional checks needed - this may change
            result.append("STR_BUY_MENU_ADDITIONAL_TEXT_HINT_LIVERY_VARIANTS")

        if len(result) == 1:
            return (
                "STR_BUY_MENU_ADDITIONAL_TEXT_WRAPPER_ONE_SUBSTR, string("
                + result[0]
                + ")"
            )
        if len(result) == 2:
            return (
                "STR_BUY_MENU_ADDITIONAL_TEXT_WRAPPER_TWO_SUBSTR, string("
                + result[0]
                + "), string("
                + result[1]
                + ")"
            )
        if len(result) == 3:
            return (
                "STR_BUY_MENU_ADDITIONAL_TEXT_WRAPPER_THREE_SUBSTR, string("
                + result[0]
                + "), string("
                + result[1]
                + "), string("
                + result[2]
                + ")"
            )
        # should never be reached, extend this if we do
        raise Exception(
            "Unsupported number of buy menu strings for "
            + self.id
            + ": "
            + str(len(result))
        )

    @property
    def buy_menu_additional_text_role_string(self):
        if self._buy_menu_additional_text_role_string is not None:
            return (
                "STR_ROLE, string(" + self._buy_menu_additional_text_role_string + ")"
            )
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

    def freeze_cross_roster_lookups(self):
        # graphics processing can't depend on roster object reliably, as it blows up multiprocessing (can't pickle roster), for reasons I never figured out
        # this freezes any necessary roster items in place
        self.frozen_roster_items = {}
        if self.is_randomised_wagon_type:
            wagon_randomisation_candidates = []
            for buyable_variant in self.buyable_variants:
                wagon_randomisation_candidates.append(
                    self.roster.get_wagon_randomisation_candidates(buyable_variant)
                )
            self.frozen_roster_items["wagon_randomisation_candidates"] = (
                wagon_randomisation_candidates
            )
        # no return

    def assert_buyable_variant_groups(self):
        # can't use buyable variant groups until they've been inited, which depends on consists being inited prior, so guard for that case
        if self.roster.buyable_variant_groups is None:
            raise BaseException(
                "buyable_variant_groups undefined for roster "
                + self.roster.id
                + " - probably buyable_variant.buyable_variant called before variant groups inited"
            )

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
        # fixed (baseline) run costs on this subtype, or more rarely instances can override this
        self.fixed_run_cost_points = kwargs.get("fixed_run_cost_points", 180)
        # optionally force a specific caboose family to be used
        self._caboose_family = kwargs.get("caboose_family", None)
        # how to handle grouping this consist type
        self.group_as_wagon = False
        # Graphics configuration only as required
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        # insert a default livery
        self.gestalt_graphics = GestaltGraphicsEngine(
            pantograph_type=self.pantograph_type,
            liveries=self.roster.get_liveries_by_name(
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
        # first check if we're simply a clone, because then we just take the costs from the clone source vehicle, and adjust them to account for differing number of units
        if self.cloned_from_consist is not None:
            return int(
                self.cloned_from_consist.buy_cost * self.clone_stats_adjustment_factor
            )

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

        # first check if we're simply a clone, because then we just take the costs from the clone source vehicle, and adjust them to account for differing number of units
        if self.cloned_from_consist is not None:
            return int(
                self.cloned_from_consist.running_cost
                * self.clone_stats_adjustment_factor
            )

        # note some string to handle NG trains, which tend to have a smaller range of speed, cost, power
        is_NG = True if self.base_track_type_name == "NG" else False
        # max speed = 200mph by design - see assert_speed() - (NG assumes 100mph max)
        # multiplier for speed, max value will be 12.5
        speed_cost_factor = self.speed / (8 if is_NG else 16)
        # max power 10000hp by design - see assert_power() - (NG assumes 4000hp max)
        # multiplier for power, max value will be ~18
        power_factor = self.power / (250 if is_NG else 555)
        # max weight = 500t by design - see assert_weight() - (NG assumes 200t max)
        # multiplie
[353100 characters not shown]
