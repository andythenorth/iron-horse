import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import math
import random

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
    GestaltGraphicsFormationDependent,
    GestaltGraphicsIntermodalContainerTransporters,
    GestaltGraphicsAutomobilesTransporter,
    GestaltGraphicsCustom,
)
import gestalt_graphics.graphics_constants as graphics_constants

import iron_horse


class ModelTypeBase(object):
    """
    'Model Variants' (appearing in buy menu) are composed as articulated vehicles.
    Each vehicle comprises one or more 'units' (visible).
    """

    def __init__(self, **kwargs):
        # mandatory, fail if missing
        self.model_variant_factory = kwargs["model_variant_factory"]
        # SHIM FOR REFACTORING - should just be catalogue_entry when done
        self.cabbage_catalogue_entry = kwargs.get("catalogue_entry", None)
        # mandatory, fail if missing
        # SHIM FOR REFACTORING, SHOULD JUST USE catalogue_entry
        if self.cabbage_catalogue_entry is not None:
            self.mv_id = self.cabbage_catalogue_entry.model_variant_id
        self.id = kwargs["id"]
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        self.name = self.model_def.name
        self.base_numeric_id = self.model_def.base_numeric_id
        # create a structure to hold buyable variants - the method can be over-ridden in consist subclasses to provide specific rules for buyable variants
        # we start empty, and rely on add_unit to populate this later, which means we can rely on gestalt_graphics having been initialised
        # otherwise we're trying to initialise variants before we have gestalt_graphics, and that's a sequencing problem
        self.buyable_variants = []
        # variant group id options are set in subclasses; supported methods are cascading:
        # set explicitly to a named group matching a consist id
        # set explicitly to a base id, for e.g. wagon groups defined on the roster, which will then compose a group name using e.g. consist track type, gen etc
        # or implicitly inferred later from rules for e.g. livery variants
        self._buyable_variant_group_id = self.model_def.buyable_variant_group_id
        self.use_named_buyable_variant_group = None
        # create a structure to hold the units
        self.units = []
        # either gen xor intro_year is required, don't set both, one will be interpolated from the other
        # CABBAGE model_def?
        self._intro_year = kwargs.get("intro_year", None)
        # override this in subclasses if needed, there's no case currently for setting it via keyword
        self._model_life = None
        # used for synchronising / desynchronising intro dates for groups vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147
        self._intro_year_days_offset = (
            None  # defined in subclasses, no need for instances to define this
        )
        # CABBAGE model_def?
        self._vehicle_life = kwargs.get("vehicle_life", None)
        # default loading speed multiplier, override in subclasses as needed
        self._loading_speed_multiplier = 1
        # some engines require pantograph sprites composited, don't bother setting this unless required
        # some vehicle models don't show pans in the buy menu (usually unpowered)
        self.suppress_pantograph_if_no_engine_attached = False
        # some engines have an optional decor layer, which is a manual spriterow num (as decor might not be widely used?)
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        self.buy_menu_additional_text_hint_wagons_add_power = False
        # structure to hold badges, add badges in subclass as needed
        self._badges = []
        # wagons can be candidates for the magic randomised wagons
        # this is on ModelTypeBase not CarModelTypeBase as we need to check it when determining order for all vehicle models
        self.randomised_candidate_groups = []
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        # option to force a specific name suffix, if the auto-detected ones aren't appropriate
        self._str_name_suffix = None
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
        # one default cargo for the whole consist, no mixed cargo shenanigans, it fails with auto-replace
        self.default_cargos = []
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        # create a structure for cargo /livery graphics options
        self.gestalt_graphics = GestaltGraphics()
        # option to provide automatic roof for all units in the consist, leave as None for no generation
        self.roof_type = None
        # optionally suppress nmlc warnings about animated pixels for vehicle models where they're intentional
        # CABBAGE model_def?
        self.suppress_animated_pixel_warnings = kwargs.get(
            "suppress_animated_pixel_warnings", False
        )
        # cite from a made up person) for docs etc
        # optional, set per subclass as needed
        self._cite = ""
        # used for docs management
        self.is_wagon_for_docs = False
        # aids 'project management' - doesn't need @property passthrough, always set in model_def
        self.sprites_complete = self.model_def.sprites_complete

    @property
    def model_type_id(self):
        return self.model_variant_factory.model_type_id

    @property
    def model_def(self):
        # just a pass through for convenience
        return self.model_variant_factory.model_def

    @property
    def roster_id(self):
        # just a pass through for convenience
        return self.model_variant_factory.roster_id

    @property
    def roster_id_providing_module(self):
        # just a pass through for convenience
        return self.model_variant_factory.roster_id_providing_module

    @property
    def is_clone(self):
        # convenience boolean to avoid checking implementation details of cloning in callers
        return self.model_def.cloned_from_model_def is not None

    def resolve_buyable_variants(self):
        # this method can be over-ridden per consist subclass as needed
        # the basic form of buyable variants is driven by liveries
        for livery in self.gestalt_graphics.all_liveries:
            # we don't need to know the actual livery here, we rely on matching them up later by indexes, which is fine
            self.buyable_variants.append(BuyableVariant(self, livery=livery))

    def add_unit(self, unit_cls, unit_def):
        # we have add_unit create the variants when needed, which means we avoid sequencing problems with gestalt_graphics initialisation
        if len(self.buyable_variants) == 0:
            self.resolve_buyable_variants()
        # now add the units
        unit = unit_cls(consist=self, unit_def=unit_def)
        for repeat_num in range(unit_def.repeat):
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
    def base_track_type_name(self):
        if self.model_def.base_track_type_name is not None:
            return self.model_def.base_track_type_name
        else:
            return "RAIL"

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
            return None

    def get_name_parts(self, context):
        default_name = "STR_NAME_" + self.id.upper()
        if context == "purchase_level_1":
            result = [default_name]
        else:
            result = [default_name]
        return result

    def get_name_as_strings(self, context):
        raw_strings = self.get_name_parts(context=context)

        if raw_strings == None:
            return 0

        # we need to know how many strings we have to handle, so that we can provide a container string with correct number of {STRING} entries
        # this is non-trivial as we might have non-string items for the stack (e.g. number or procedure results), used by a preceding substring
        string_counter = 0
        for raw_string in raw_strings:
            if raw_string[0:4] == "STR_":
                string_counter += 1
        if string_counter > 1:
            raw_strings.insert(0, "STR_NAME_CONTAINER_" + str(string_counter))

        formatted_strings = []
        for raw_string in raw_strings:
            if raw_string[0:4] == "STR_":
                # possibly fragile wrapping of string() around strings, to avoid having to always specify them that way
                formatted_strings.append("string(" + raw_string + ")")
            else:
                # otherwise pass through as is
                formatted_strings.append(raw_string)

        # special case for when substrings need converting to parameters on first string
        if len(formatted_strings) > 1:
            # assumes 2 items
            if formatted_strings[0] != "string(STR_NAME_CONTAINER_2)":
                raise Exception(
                    "formatted_strings first result should be 'string(STR_NAME_CONTAINER_2)'"
                )

            base_string = formatted_strings[0][:-1]
            parameters = formatted_strings[1:]
            result = f"{base_string}, {', '.join(parameters)})"
        else:
            result = formatted_strings[0]  # we just want the first string from the list
        return result

    def get_name_as_property(self):
        # text filter in buy menu needs name as prop as of June 2023
        # this is very rudimentary and doesn't include all the parts of the name
        name_parts = self.get_name_parts(context="default_name")
        result = "string(" + name_parts[0] + ")"
        return result

    @property
    def subrole_child_branch_num(self):
        # subrole child branch num places this vehicle on a specific child branch of the tech tree, where the subrole and role are the parent branches
        # 0 = null, no branch (for wagons etc)
        #  1..n for branches
        # -1..-n for jokers
        if self.model_def.subrole_child_branch_num is not None:
            return self.model_def.subrole_child_branch_num
        else:
            return 0

    @property
    def subrole(self):
        if self.model_def.subrole is not None:
            return self.model_def.subrole
        else:
            return None

    @property
    def role(self):
        # returns first matched, assumption is vehicle models only have one valid subrole
        for role, subroles in global_constants.role_subrole_mapping.items():
            if self.subrole in subroles:
                return role
        # role is optional
        return None

    @property
    def role_badge(self):
        if self.role is not None:
            return "role/" + self.role
        return None

    @property
    def vehicle_family_badge(self):
        # stub only, over-ride in subclasses as appropriate
        return None

    @property
    def cabbage_subtype_badge(self):
        # stub only, over-ride in subclasses as appropriate
        return None

    @property
    def cabbage_power_source_badges(self):
        # note returns multiple badges, as engines support multiple power sources
        result = []
        if self.power_by_power_source is not None:
            for power_source in self.power_by_power_source.keys():
                # null is used for e.g. snowploughs etc where the power is only to enable the vehicle to lead the train
                if power_source in ["NULL"]:
                    continue
                result.append("power_source/" + power_source.lower())
            # special cases
            if (
                "DIESEL" in self.power_by_power_source.keys()
                and "AC" in self.power_by_power_source.keys()
            ):
                result.append("power_source_cabbage/electro_diesel")
            if (
                "AC" in self.power_by_power_source.keys()
                and "DC" in self.power_by_power_source.keys()
            ):
                result.append("power_source_cabbage/dual_voltage")
        return result

    @property
    def cabbage_colour_mix_badges(self):
        # note returns multiple badges, as vehicles support multiple colours
        result = []
        return result

    def get_cabbage_variant_handling_badges(self, unit_variant):
        result = []
        if len(unit_variant.buyable_variant.buyable_variant_group.buyable_variants) > 1:
            result.append("ih_variants_cabbage/cabbage_level_0_has_children")
        if unit_variant.buyable_variant.buyable_variant_group.parent_group is not None:
            result.append("ih_variants_cabbage/cabbage_level_1_has_children")
        return result

    def get_badges(self, unit_variant):
        # badges can be set on a vehicle for diverse reasons, including
        # - badges explicitly added to _badges attr
        # - badges arising implicitly from consist type or properties
        result = list(set(self._badges))
        # power source badges - note that this returns a list, not a single badge
        result.extend(self.cabbage_power_source_badges)
        # colour mix badges - note that this returns a list, not a single badge
        result.extend(self.cabbage_colour_mix_badges)
        # special variant handling badges
        result.extend(self.get_cabbage_variant_handling_badges(unit_variant))
        if self.role_badge is not None:
            result.append(self.role_badge)
        # badge for handling vehicle_family
        if self.vehicle_family_badge is not None:
            result.append(self.vehicle_family_badge)
        # badge for handling wagon lengths
        if self.cabbage_subtype_badge is not None:
            result.append(self.cabbage_subtype_badge)
        # badges for special behaviours
        if self.tilt_bonus:
            result.append("special_flags/tilt")
        return result

    def get_badges_for_nml(self, unit_variant):
        return (
            "["
            + ",".join(f'"{badge}"' for badge in self.get_badges(unit_variant))
            + "]"
        )

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
    def fixed_run_cost_points(self):
        # default, override in subclass as needed
        self.fixed_run_cost_points = 30

    @property
    def gen(self):
        # just a passthrough for convenience
        return self.model_def.gen

    @property
    def random_reverse(self):
        # just a passthrough for convenience
        # random_reverse means (1) randomised flip of vehicle when built (2) player can also flip vehicle manually
        # random_reverse is not supported in some templates
        return self.model_def.random_reverse

    @property
    def decor_spriterow_num(self):
        # just a passthrough for convenience
        # stupid extra-detail, control which variants show decor in purchase menu
        return self.model_def.decor_spriterow_num

    @property
    def show_decor_in_purchase_for_variants(self):
        if self.model_def.show_decor_in_purchase_for_variants is not None:
            return self.model_def.show_decor_in_purchase_for_variants
        else:
            return []

    @property
    def docs_image_spriterow(self):
        # just a passthrough for convenience
        # 0 indexed spriterows, position in generated spritesheet, used by caboose to get a docs image for 4th gen, not 1st
        return self.model_def.docs_image_spriterow

    @property
    def tilt_bonus(self):
        # just a passthrough for convenience
        return self.model_def.tilt_bonus

    @property
    def lgv_capable(self):
        # just a passthrough for convenience
        return self.model_def.lgv_capable

    @property
    def requires_high_clearance(self):
        # just a passthrough for convenience
        return self.model_def.requires_high_clearance

    @property
    def dual_headed(self):
        # just a passthrough for convenience
        return self.model_def.dual_headed

    @property
    def easter_egg_haulage_speed_bonus(self):
        # just a passthrough for convenience
        return self.model_def.easter_egg_haulage_speed_bonus

    @property
    def pantograph_type(self):
        # just a passthrough
        # default will be None if not set
        return self.model_def.pantograph_type

    @property
    def extended_vehicle_life(self):
        # vehicle life uses a default value, but can be extended automatically via a bool keyword, or it can be set manually
        if self.model_def.extended_vehicle_life is not None:
            return self.model_def.extended_vehicle_life
        else:
            return False

    @property
    def power_by_power_source(self):
        # just a passthrough for convenience
        return self.model_def.power_by_power_source

    @property
    def tractive_effort_coefficient(self):
        if self.model_def.tractive_effort_coefficient is not None:
            return self.model_def.tractive_effort_coefficient
        else:
            return 0.3

    @property
    def intro_year(self):
        # automatic intro_year, but can override by passing in kwargs for consist
        assert self.gen != None, (
            "%s consist has no gen value set, which is incorrect" % self.id
        )
        result = self.roster.intro_years[self.base_track_type_name][self.gen - 1]
        if self.intro_year_offset is not None:
            result = result + self.intro_year_offset
        return result

    @property
    def intro_year_offset(self):
        # if gen is used, the calculated intro year can be adjusted with +ve or -ve offset
        return self.model_def.intro_year_offset

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
            role_key = self.role
            if role_key in ["express", "freight"]:
                # assume that we want child branch 1 to be grouped as 'core' in some cases
                # !! not convinced this achieves much as of July 2022 but eh
                if self.subrole_child_branch_num == 1:
                    role_key = self.role + "_core"
                else:
                    role_key = self.role + "_non_core"
            result = global_constants.intro_month_offsets_by_role[role_key]
            if self.joker:
                # force jokers away from vehicles in same subrole
                # if further variation is wanted, give the joker a different intro year, automating that isn't wise
                result = min(result + 6, 11)
        return result

    @property
    def replacement_consist(self):
        # option exists to force a replacement consist, this is used to merge tech tree branches
        #  most vehicle models are automatically replaced by the next vehicle model in the subrole tree
        # ocasionally we need to merge two branches of the subrole, in this case set replacement consist id on the model_def
        if self.model_def.replacement_model_model_type_id is not None:
            for consist in self.roster.engine_consists:
                if consist.id == self.model_def.replacement_model_model_type_id:
                    return consist
            # if we don't return a valid result, that's an error, probably a broken replacement id
            raise Exception(
                "replacement consist id "
                + self.model_def.replacement_model_model_type_id
                + " not found for consist "
                + self.id
            )
        else:
            similar_consists = []
            replacement_consist = None
            for consist in self.roster.engine_consists:
                if (
                    (consist.subrole == self.subrole)
                    and (
                        consist.subrole_child_branch_num
                        == self.subrole_child_branch_num
                    )
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
        # note that this depends on replacement_consist property in other model defs, and may not work in all cases
        # a consist can replace more than one other consist
        result = []
        for consist in self.roster.engine_consists:
            if consist.replacement_consist is not None:
                if consist.replacement_consist.id == self.id:
                    result.append(consist)
        return result

    @property
    def similar_consists(self):
        # quite a crude guess at similar engines by subrole
        result = []
        for consist in self.roster.engine_consists:
            if (
                (consist.base_track_type_name == self.base_track_type_name)
                and (consist.gen == self.gen)
                and (consist != self)
                and (consist.model_def.cloned_from_model_def is None)
                and (getattr(consist, "cab_id", None) is None)
            ):
                if (
                    (consist.subrole == self.subrole)
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
        # fetch dedicated trailer vehicles for this cab engine (if any)
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
        for power_source, optional_props in global_constants.power_sources.items():
            if power_source in self.power_by_power_source.keys():
                result.append(
                    [
                        power_source,
                        self.base_track_type_name + optional_props.get("suffix", ""),
                    ]
                )
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
            # !! this should probably be somehow delegated back to global_constants.power_sources
            # !! but TMWFTLB as of Jan 2025
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
        if self.model_def.speed is not None:
            return self.model_def.speed
        elif getattr(self, "speed_class", None):
            # speed by class, if speed_class is set explicitly (and not None)
            # !! this doesn't handle RAIL / ELRL correctly
            # could be fixed by checking a list of railtypes
            return self.get_speed_by_class(self.speed_class)
        elif self.subrole:
            # first check for express roles, which are determined by multiple subroles
            for role in [
                "express",
                "driving_cab",
                "express_railcar",
                "high_power_railcar",
            ]:
                subroles = global_constants.role_subrole_mapping[role]
                if self.subrole in subroles:
                    return self.get_speed_by_class("express")
            # then check other specific roles
            # !! this would be better determined by setting self.speed_class appropriately in the consist subclasses
            if self.subrole in ["mail_railcar", "pax_railcar", "pax_railbus"]:
                return self.get_speed_by_class("suburban")
            elif self.subrole in ["hst"]:
                return self.get_speed_by_class("hst")
            elif self.subrole in ["very_high_speed"]:
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
        for role in [
            "express",
            "driving_cab",
            "express_railcar",
            "high_power_railcar",
        ]:
            subroles = global_constants.role_subrole_mapping[role]
            if self.subrole in subroles:
                return self.get_speed_by_class("express_on_lgv")

        if self.subrole in ["hst"]:
            return self.get_speed_by_class("hst_on_lgv")
        elif self.subrole in ["very_high_speed"]:
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
    def input_spritesheet_name_stem(self):
        # optional support for delegating to a spritesheet belonging to a different vehicle type (e.g. when recolouring same base pixels for different wagon types)
        if self.gestalt_graphics.input_spritesheet_delegate_id is not None:
            # we never get a delegate of this type from anywhere other than current consist, that's the rules
            input_spritesheet_name_stem = (
                self.gestalt_graphics.input_spritesheet_delegate_id
            )
        else:
            # handle cloned cases by referring to the original consist factory for the path
            if self.is_clone:
                # this will get a default consist from the source factory, mapping this consist to the source spritesheet
                input_spritesheet_name_stem = (
                    self.model_def.cloned_from_model_def.model_type_id
                )
            else:
                input_spritesheet_name_stem = self.id

        # the consist id might have the consist's roster_id baked into it, if so replace it with the roster_id of the module providing the graphics file
        # this will have a null effect (which is fine) if the roster_id consist is the same as the module providing the graphics gile
        input_spritesheet_name_stem = input_spritesheet_name_stem.replace(
            self.roster_id, self.roster_id_providing_module
        )
        return input_spritesheet_name_stem

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
        # !!! this is lolz, so many ifs just to get a string -> number mapping
        # !!! it's infrequently changed, but should just be some lookup table of some kind
        if "random_from_consist_liveries_grey_pewter" in colour_set:
            return 117
        elif "random_from_consist_liveries_red_ruby" in colour_set:
            return 116
        elif "random_from_consist_liveries_teal_nightshade" in colour_set:
            return 115
        elif "random_from_consist_liveries_teal_pewter" in colour_set:
            return 114
        elif "random_from_consist_liveries_sulphur_straw" in colour_set:
            return 113
        elif "random_from_consist_liveries_gremlin_green_silver" in colour_set:
            return 112
        elif "random_from_consist_liveries_ochre_sand" in colour_set:
            return 111
        elif "random_from_consist_liveries_oil_black_nightshade" in colour_set:
            return 110
        elif "random_from_consist_liveries_ruby_bauxite" in colour_set:
            return 109
        elif "random_from_consist_liveries_sulphur_ochre" in colour_set:
            return 108
        elif "random_from_consist_liveries_silver_pewter" in colour_set:
            return 107
        elif "random_from_consist_liveries_teal_violet" in colour_set:
            return 106
        elif "random_from_consist_liveries_bauxite_grey_nightshade" in colour_set:
            return 105
        elif "random_from_consist_liveries_variety" in colour_set:
            return 104
        elif "random_from_consist_liveries_complement_company_colour" in colour_set:
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
        # should never be reached, extend this if we do
        raise Exception(
            "Unsupported number of buy menu strings for "
            + self.id
            + ": "
            + str(len(result))
        )

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
        # can't use buyable variant groups until they've been inited, which depends on model variants being inited prior, so guard for that case
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
                    "ModelType " + self.id + " has speed > 200, which is too much"
                )

    def assert_power(self):
        # power is assumed to be limited to 10,000hp
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.speed is not None:
            if self.power > 10000:
                utils.echo_message(
                    "ModelType " + self.id + " has power > 10000hp, which is too much"
                )

    def assert_weight(self):
        # weight is assumed to be limited to 500t
        # this isn't an OpenTTD limit, it's used to give a scale for buy and run cost spreads
        if self.weight is not None:
            if self.weight > 500:
                utils.echo_message(
                    "ModelType " + self.id + " has weight > 500t, which is too much"
                )

    def assert_description_foamer_facts(self):
        # if these are too noisy, comment them out temporarily
        if self.power > 0:
            if len(self.model_def.description) == 0:
                utils.echo_message("ModelType " + self.id + " has no description")
            if len(self.model_def.foamer_facts) == 0:
                utils.echo_message("ModelType " + self.id + " has no foamer_facts")
            if "." in self.model_def.foamer_facts:
                utils.echo_message(
                    "ModelType " + self.id + " foamer_facts has a '.' in it."
                )

    def render(self, templates, graphics_path):
        self.assert_speed()
        self.assert_power()
        # templating
        nml_result = ""
        for unit in self.unique_units:
            nml_result = nml_result + unit.render(templates, graphics_path)
        return nml_result


class EngineModelTypeBase(ModelTypeBase):
    """
    Base model type for Engines and other powered vehicles.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # arbitrary multiplier to floating run costs (factors are speed, power, weight)
        # adjust per subtype as needed
        self.floating_run_cost_multiplier = 8.5
        # how to handle grouping this consist type
        self.group_as_wagon = False
        # Graphics configuration only as required
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        # insert a default livery
        # CABBAGE FACTORY?
        if self.model_def.cabbage_new_livery_system:
            liveries = self.roster.get_liveries_by_name_cabbage_new(
                [self.cabbage_catalogue_entry.livery_name]
            )
        else:
            liveries = self.roster.get_liveries_by_name(
                self.model_def.additional_liveries
                if self.model_def.additional_liveries is not None
                else []
            )
        default_livery_extra_docs_examples = (
            self.model_def.default_livery_extra_docs_examples
            if self.model_def.default_livery_extra_docs_examples is not None
            else []
        )
        self.gestalt_graphics = GestaltGraphicsEngine(
            pantograph_type=self.pantograph_type,
            liveries=liveries,
            default_livery_extra_docs_examples=default_livery_extra_docs_examples,
        )

    @property
    def caboose_family(self):
        # caboose families are used to match engines to caboose variants
        # can be forced on a per engine basis
        # otherwise use default for base track type and vehicle gen
        if self.model_def.caboose_family is not None:
            return self.model_def.caboose_family
        else:
            return "default_" + str(self.gen)

    @property
    def buy_cost(self):
        # first check if this is a clone, because then we just take the costs from the clone source
        # and adjust them to account for differing number of units
        if self.model_def.cloned_from_model_def is not None:
            # we have to instantiate an actual consist, temporarily, as the factory doesn't know the calculated cost directly
            from train.factory import ModelVariantFactory

            model_variant_factory = ModelVariantFactory(
                self.model_def.cloned_from_model_def,
                self.roster_id,
                self.roster_id_providing_module,
            )
            temp_consist = model_variant_factory.produce(
                dry_run=True, catalogue_index=0
            )
            return int(
                temp_consist.buy_cost * self.model_def.clone_stats_adjustment_factor
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
        # !! assumption of AC !!
        elif self.electro_diesel_buy_cost_malus is not None:
            power_factor = (
                self.electro_diesel_buy_cost_malus * self.power_by_power_source["AC"]
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
    def fixed_run_cost_points(self):
        # fixed (baseline) run costs on this subtype, or, more rarely, instances can override this
        if self.model_def.fixed_run_cost_points is not None:
            return self.model_def.fixed_run_cost_points
        else:
            return 180

    @property
    def running_cost(self):
        # algorithmic calculation of engine run costs
        # as of Feb 2019, it's fixed cost (set by subtype) + floating costs (derived from power, speed, weight)

        # first check if this is a clone, because then we just take the costs from the clone source
        # and adjust them to account for differing number of units
        if self.model_def.cloned_from_model_def is not None:
            # we have to instantiate an actual consist, temporarily, as the factory doesn't know the calculated cost directly
            from train.factory import ModelVariantFactory

            model_variant_factory = ModelVariantFactory(
                self.model_def.cloned_from_model_def,
                self.roster_id,
                self.roster_id_providing_module,
            )
            temp_consist = model_variant_factory.produce(
                dry_run=True, catalogue_index=0
            )
            return int(
                temp_consist.running_cost * self.model_def.clone_stats_adjustment_factor
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
        # multiplier for weight, max value will be 8
        weight_factor = self.weight / (32 if is_NG else 62.5)

        # !! this is an abuse of requires_electric_rails, but it's _probably_ fine :P
        if self.requires_electric_rails:
            if "railcar" in self.subrole:
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
        if self.subrole in [
            "heavy_freight",
            "super_heavy_freight",
            "ultra_heavy_freight",
        ]:
            run_cost = 0.9 * run_cost
        elif self.subrole in [
            "branch_freight",
            "freight",
        ]:
            run_cost = 0.8 * run_cost
        # massive bonuses for NG and Gronks
        elif self.subrole == "gronk":
            run_cost = 0.66 * run_cost
        if is_NG:
            run_cost = 0.33 * run_cost
        # cap to int for nml
        return int(run_cost)

    @property
    def joker(self):
        # jokers are bonus vehicles (mostly) engines which are excluded from simplified game mode
        # all clones are automatically jokers and excluded
        if self.is_clone:
            return True
        # for engines, jokers use -ve value for subrole_child_branch_num, tech tree vehicles use +ve
        return self.subrole_child_branch_num < 0


class SimpleEngine(EngineModelTypeBase):
    """
    Basic engine (without passenger or cargo capacity).
    """

    def __init__(self, **kwargs):
        # minimal pass through to parent as of Feb 2025
        super().__init__(**kwargs)


class AutoCoachCombineEngine(EngineModelTypeBase):
    """
    Articulated auto coach combine (mail + pax).  Implemented as Engine so it can lead a consist in-game.
    To keep implementation simple + crude, first unit should be dedicated mail type, second unit should be dedicated pax type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ....buy costs adjusted to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_buy_cost_points = 6
        # Graphics configuration
        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_autocoach.pynml",
            liveries=liveries,
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["autocoach_combine"]

    @property
    def subrole(self):
        return "driving_cab_express_mixed"

    @property
    def subrole_child_branch_num(self):
        # driving cab cars are probably jokers?
        return -1

    @property
    def power_by_power_source(self):
        # confer tiny power value to make this one an engine so it can lead.
        # use 10 not 1, because 1 looks weird when added to engine HP
        return {"NULL": 10}

    @property
    def tractive_effort_coefficient(self):
        # nerf TE down to minimal value
        return 0

    @property
    def fixed_run_cost_points(self):
        # ....run costs nerfed down to match equivalent gen 2 + 3 pax / mail cars
        return 43

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class FixedFormationRailcarCombineEngine(EngineModelTypeBase):
    """
    Fixed formation articulated railcar combine (mail + pax).
    This *does* not use consist-dependent position sprite rulesets; the formation is fixed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_fixed_formation_railcar.pynml",
            liveries=self.roster.get_liveries_by_name([]),
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types[self.model_def.pax_car_capacity_type]

    @property
    def subrole(self):
        if self.base_track_type_name == "NG":
            # pony NG jank, to force a different role string for NG
            if self.gen == 4:
                return "express"
            else:
                return "universal"
        else:
            return super().subrole

    @property
    def loading_speed_multiplier(self):
        # !!!!!!!!!!!!!!!
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class MailEngineBase(EngineModelTypeBase):
    """
    Engines / units with mail (and express freight) capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # increased buy costs for having extra doors and stuff eh?
        self.buy_cost_adjustment_factor = 1.4

    @property
    def fixed_run_cost_points(self):
        # ...reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        return 84


class MailEngineCabbageDVT(MailEngineBase):
    """
    Mail DVT / cabbage.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # report mail cab cars as pax cars for consist rulesets
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "dvt_mail_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="driving_cab_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        return "driving_cab_express_mail"

    @property
    def power_by_power_source(self):
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        return {"NULL": 300}

    @property
    def tractive_effort_coefficient(self):
        # nerf TE down to minimal value
        return 0.1

    @property
    def fixed_run_cost_points(self):
        # ....run costs reduced from base to make it close to mail cars
        return 68


class MailEngineCargoSprinter(MailEngineBase):
    """
    Cab Motor for Cargo Sprinter express freight formation.
    """

    liveries = [global_constants.freight_wagon_liveries["COMPANY_COLOUR_NO_WEATHERING"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # non-standard cite
        self._cite = "Arabella Unit"
        self._loading_speed_multiplier = 2
        # Graphics configuration
        # !! there is no automatic masking of the cab overlays as of Dec 2020, currently manual - automation might be needed for well cars in future, deal with it then if that's the case
        # NOTE that cargo sprinter will NOT randomise containers on load as of Dec 2020 - there is a bug with rear unit running unwanted triggers and re-randomising in depots etc
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_cargo_sprinter.pynml",
            cargo_label_mapping=GestaltGraphicsIntermodalContainerTransporters(
                liveries=self.liveries
            ).cargo_label_mapping,
            num_extra_layers_for_spritelayer_cargos=2,
            liveries=self.liveries,
        )

    @property
    def fixed_run_cost_points(self):
        # run cost algorithm doesn't account for dual-head / high power MUs reliably, so just fix it here, using assumption that there are very few cargo sprinters and this will be fine
        return 240

    @property
    def spritelayer_cargo_layers(self):
        # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
        return ["cargo_sprinter"]

    @property
    def dual_headed(self):
        return True


class MailEngineMetro(MailEngineBase):
    """
    Mail metro train.
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
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "metro_mail_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="metro",
            liveries=liveries,
        )

    @property
    def loading_speed_multiplier(self):
        # OP bonus to mail metro loading speed
        return 4


class MailEngineRailcar(MailEngineBase):
    """
    Mail railcar.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cabs both ends
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no driving cabs (OPTIONAL - only provided for 4-unit sets)
        # Rules are 2 unit sets of 3 unit sets (4 could also be supported, but isn't at time of writing)
        # CABBAGE THIS SHOULD BE CONSIST RULESET
        if self.model_def.formation_ruleset is not None:
            formation_ruleset = self.model_def.formation_ruleset
        else:
            formation_ruleset = "railcars_2_unit_sets"

        # note that this if/elif only actually covers 2 cases as of Feb 2025 - no other cases were needed
        if formation_ruleset == "railcars_2_unit_sets":
            spriterow_group_mappings = {
                "default": 0,
                "first": 1,
                "last": 2,
                "special": 0,
            }
        elif formation_ruleset == "railcars_3_unit_sets":
            spriterow_group_mappings = {
                "default": 0,
                "first": 1,
                "last": 2,
                "special": 3,
            }
        # this will be fragile, it's dedicated to pony roster, but eh
        # for special cases, these vehicles could just use the livery keyword on init, but it would be over-ridden by this conditional block currently
        if self.subrole_child_branch_num in [2] or self.base_track_type_name == "NG":
            liveries = self.roster.get_pax_mail_liveries(
                "diesel_railcar_mail_liveries", self.model_def
            )
        else:
            liveries = self.roster.get_pax_mail_liveries(
                "electric_railcar_mail_liveries", self.model_def
            )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset=formation_ruleset,
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def subrole(self):
        if self.base_track_type_name == "NG" and self.gen == 4:
            # pony NG jank
            return "express"
        else:
            return super().subrole

    @property
    def fixed_run_cost_points(self):
        if self.base_track_type_name == "NG":
            # give NG a bonus to align run cost with NG railbus
            return 52
        else:
            return super().fixed_run_cost_points

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name


class MailEngineExpressRailcar(MailEngineBase):
    """
    Express mail railcar (single unit, combinable).
    Intended for express-speed, high-power long-distance EMUs, use railbus or railcars for short / slow / commuter routes.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 0.85
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with two cabs (will never be used if the specific consist is articulated)
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        liveries = self.roster.get_pax_mail_liveries(
            "default_mail_liveries", self.model_def
        )
        jfdi_pantograph_debug_image_y_offsets = [len(liveries) * 60, 30]
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_4_unit_sets",
            liveries=liveries,
            pantograph_type=self.pantograph_type,
            jfdi_pantograph_debug_image_y_offsets=jfdi_pantograph_debug_image_y_offsets,
        )

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name

    @property
    def fixed_run_cost_points(self):
        # to avoid these railcars being super-bargain cheap, add a cost malus compared to standard railcars (still less than standard engines)
        return 155


class PassengerEngineBase(EngineModelTypeBase):
    """
    Engine with passenger capacity
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = ["PASS"]
        # increased buy costs for having seats and stuff eh?
        self.buy_cost_adjustment_factor = 1.8

    @property
    def pax_car_capacity_type(self):
        # specific structure for capacity multiplier and loading speed, override in subclasses as needed
        if self.model_def.pax_car_capacity_type is not None:
            return self.roster.pax_car_capacity_types[
                self.model_def.pax_car_capacity_type
            ]
        else:
            return self.roster.pax_car_capacity_types["default"]

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]

    @property
    def fixed_run_cost_points(self):
        # ...but reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        return 84


class PassengerEngineCabControlCar(PassengerEngineBase):
    """
    Passenger cab control car / driving trailer.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # report cab cars as pax cars for consist rulesets
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="driving_cab_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        return "driving_cab_express_pax"

    @property
    def power_by_power_source(self):
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        return {"NULL": 300}

    @property
    def tractive_effort_coefficient(self):
        # nerf TE down to minimal value
        return 0.1

    @property
    def fixed_run_cost_points(self):
        # ....run costs reduced from base to make it close to mail cars
        return 68


class PassengerEngineHSTCab(PassengerEngineBase):
    """
    Dual-headed HST (high speed train).
    May or may not have capacity (set per vehicle).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_cost_adjustment_factor = 1.2
        # higher speed should only be effective over longer distances
        # ....run cost multiplier is adjusted up from pax base for high speed
        self.floating_run_cost_multiplier = 10
        # non-standard cite
        self._cite = "Dr Constance Speed"

    @property
    def dual_headed(self):
        return True


class PassengerEngineExpressRailcar(PassengerEngineBase):
    """
    Express pax railcar (single unit, combinable).
    Intended for express-speed, high-power long-distance EMUs, use railbus or railcars for short / slow / commuter routes.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 0.85
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        jfdi_pantograph_debug_image_y_offsets = [len(liveries) * 60, 30]
        # various rulesets are supported, per consist, (or could be extended to checks per roster)
        # this wasn't moved to @property due to laziness, as of Jan 2025
        if self.model_def.formation_ruleset is not None:
            formation_ruleset = self.model_def.formation_ruleset
        else:
            formation_ruleset = "railcars_6_unit_sets"
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset=formation_ruleset,
            liveries=liveries,
            pantograph_type=self.pantograph_type,
            jfdi_pantograph_debug_image_y_offsets=jfdi_pantograph_debug_image_y_offsets,
        )

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name

    @property
    def fixed_run_cost_points(self):
        if self.base_track_type_name == "NG":
            # cleanest way to compress run cost down sufficiently
            self.floating_run_cost_multiplier = 4
            # special case to knock costs on NG versions of these down similar to other railcars
            return 120
        else:
            # to avoid these railcars being super-bargain cheap, add a cost malus compared to standard railcars (still less than standard engines)
            return 155


class PassengerEngineMetro(PassengerEngineBase):
    """
    Pax metro train.  Just a sparse subclass to force the gestalt_graphics
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
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "metro_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="metro",
            liveries=liveries,
        )

    @property
    def loading_speed_multiplier(self):
        # super super OP bonus to pax metro loading speed
        return 8


class PassengerEngineRailbus(PassengerEngineBase):
    """
    Lightweight railbus (single unit, combinable).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # ruleset will combine these to make multiple-units 1, 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        formation_ruleset = "railcars_3_unit_sets"
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset=formation_ruleset,
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def subrole(self):
        if self.base_track_type_name == "NG":
            # pony NG jank
            if self.gen == 4:
                return "express"
            else:
                return "universal"
        else:
            return super().subrole

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name

    @property
    def fixed_run_cost_points(self):
        # big cost bonus for railbus
        return 48


class PassengerEngineRailcar(PassengerEngineBase):
    """
    High-capacity pax railcar (single unit, combinable).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        if self.subrole_child_branch_num in [2]:
            liveries = self.roster.get_pax_mail_liveries(
                "suburban_pax_liveries", self.model_def
            )
        else:
            liveries = self.roster.get_pax_mail_liveries(
                "default_pax_liveries", self.model_def
            )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_3_unit_sets",
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["high_capacity"]

    @property
    def vehicle_family_badge(self):
        return "vehicle_family/" + self.id


class SnowploughEngine(EngineModelTypeBase):
    """
    Snowplough!  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # give it mail / express capacity so it has some purpose :P
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # to reduce it from engine factor
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # Graphics configuration

        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_snowplough.pynml",
            liveries=liveries,
        )

    @property
    def subrole(self):
        # blame Pikka for the spelling eh? :)
        return "snoughplough!"

    @property
    def subrole_child_branch_num(self):
        # joker
        return -1

    @property
    def power_by_power_source(self):
        # confer a small power value for 'operational efficiency' :)
        return {"NULL": 100}

    @property
    def tractive_effort_coefficient(self):
        # nerf TE down to minimal value
        return 0.1

    @property
    def fixed_run_cost_points(self):
        # ....run costs reduced from base to make it close to mail cars
        return 68


class TGVCabEngine(EngineModelTypeBase):
    """
    TGV (very high speed) engine (leading cab motor)
    This has power by default and would usually be set as a dual-headed engine.
    Adding specific middle engines (with correct ID) will increase power for this engine.
    This does not have pax capacity, by design, to allow for TGV La Poste mail trains.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_menu_additional_text_hint_wagons_add_power = True
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
    def buy_menu_additional_text_distributed_power_substring(self):
        return "STR_WAGONS_ADD_POWER_CAB"

    @property
    def buy_menu_distributed_power_name_substring(self):
        return "STR_NAME_" + self.id.upper()

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.power

    @property
    def tilt_bonus(self):
        return True

    @property
    def lgv_capable(self):
        return True

    @property
    def dual_headed(self):
        return True


class TGVMiddleEngineMixin(EngineModelTypeBase):
    """
    Mixin for an intermediate motor unit for very high speed train (TGV etc).
    When added to the correct cab engine, this vehicle will cause cab power to increase.
    Add as additional class for e.g. pax or mail engine consist.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cab_id = self.id.split("_middle")[0] + "_cab"
        self._buyable_variant_group_id = self.cab_id
        self.wagons_add_power = True
        self.buy_menu_additional_text_hint_wagons_add_power = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        # eh as of Feb 2019, OpenTTD won't actually use this for middle cars, as not engines
        # this means the buy menu won't match, but wagons will match anyway when attached to cab
        # prop left in place in case that ever gets changed :P
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # position variants
        # * default unit
        # * unit with pantograph - leading end
        # * unit with pantograph -  rear end
        # * buffet unit
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="tgv",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            default_livery_extra_docs_examples=self.cab_consist.gestalt_graphics.default_livery_extra_docs_examples,
            pantograph_type=self.pantograph_type,
        )

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
    def buy_menu_additional_text_distributed_power_substring(self):
        return "STR_WAGONS_ADD_POWER_MIDDLE"

    @property
    def buy_menu_distributed_power_name_substring(self):
        return "STR_NAME_" + self.cab_id.upper()

    @property
    def buy_menu_distributed_power_hp_value(self):
        return self.cab_consist.power

    @property
    def intro_year_offset(self):
        # get the intro year offset and life props from the cab, to ensure they're in sync
        return self.cab_consist.intro_year_offset

    @property
    def vehicle_family_badge(self):
        return "vehicle_family/" + self._buyable_variant_group_id

    @property
    def tilt_bonus(self):
        return True

    @property
    def lgv_capable(self):
        return True


class TGVMiddleMailEngine(TGVMiddleEngineMixin, MailEngineBase):
    """
    Mail intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def subrole_child_branch_num(self):
        # force the child branches apart for middle engines, based on cab ID
        # as of Jan 2025, this is used by tech tree, and (I think) for calculating replacement
        if self.cab_consist.subrole_child_branch_num < 0:
            offset = -2000
        else:
            offset = 2000
        return offset + self.cab_consist.subrole_child_branch_num


class TGVMiddlePassengerEngine(TGVMiddleEngineMixin, PassengerEngineBase):
    """
    Pax intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def subrole_child_branch_num(self):
        # force the child branches apart for middle engines, based on cab ID
        # as of Jan 2025, this is used by tech tree, and (I think) for calculating replacement
        if self.cab_consist.subrole_child_branch_num < 0:
            offset = -1000
        else:
            offset = 1000
        return offset + self.cab_consist.subrole_child_branch_num


class CarModelTypeBase(ModelTypeBase):
    """
    Intermediate class for car (wagon) model types to subclass from, provides sparse properties, most are declared in subclasses.
    """

    # model_type_id = '' # provide in subclass

    def __init__(self, speedy=False, **kwargs):
        super().__init__(**kwargs)
        self.roster.register_wagon_consist(self)

        # override this in subclass as needed
        self._joker = False
        # override this in subclass for, e.g. express freight car model types
        self.speed_class = "standard"
        # Weight factor: override in subclass as needed
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type_name == "NG" else 1
        # used to synchronise / desynchronise groups of vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        # default all car model types to 'universal' offset, override in subclasses as needed
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "universal"
        ]
        # assume all wagons randomly swap CC, revert to False in wagon subclasses as needed
        self.use_colour_randomisation_strategies = True
        # how to handle grouping this consist type
        self.group_as_wagon = True
        # used for docs optimisation etc
        self.is_wagon_for_docs = True

    @property
    def subtype(self):
        # just a passthrough for convenience
        return self.model_def.subtype

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
        # allow this to be delegated to the consist if necessary
        if self._model_life is not None:
            return self._model_life
        # automatically span wagon model life across gap to next generation
        # FYI next generation might be +n, not +1
        # this has to handle the cases of
        # - subtype that is the end of the tree for that type and should always be available
        # - subtype that ends but *should* be replaced by another subtype that continues the tree
        # - subtype where there is a generation gap in the tree, but the subtype continues across the gap
        tree_permissive = []
        tree_strict = []
        for wagon in self.roster.wagon_consists_by_base_id[self.model_type_id_stem]:
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

    def get_input_spritesheet_delegate_id_wagon(
        self, input_spritesheet_delegate_base_id
    ):
        input_spritesheet_delegate_id = self.model_variant_factory.get_wagon_id(
            input_spritesheet_delegate_base_id,
            model_def=self.model_def,
        )
        return input_spritesheet_delegate_id

    @property
    def cabbage_subtype_badge(self):
        return "ih_wagon_length/" + self.subtype.lower()

    @property
    def wagon_title_class_str(self):
        return "STR_NAME_SUFFIX_" + self.model_type_id_stem.upper()

    @property
    def wagon_title_optional_randomised_suffix_str(self):
        if self.is_randomised_wagon_type or self.is_caboose:
            return "STR_NAME_SUFFIX_RANDOMISED_WAGON"
        else:
            return None

    def get_name_parts(self, context):
        if self.wagon_title_optional_randomised_suffix_str is not None:
            default_result = [
                self.wagon_title_class_str,
                self.wagon_title_optional_randomised_suffix_str,
            ]
        else:
            default_result = [
                self.wagon_title_class_str,
            ]

        if context == "docs":
            result = [
                self.wagon_title_class_str,
                self.wagon_title_optional_randomised_suffix_str,
            ]
        elif context in ["default_name", "purchase_level_1", "purchase_level_2"]:
            result = default_result
        elif context == "purchase_level_0":
            if self.use_named_buyable_variant_group != None:
                try:
                    result = [
                        "STR_" + self.use_named_buyable_variant_group.upper(),
                    ]
                except:
                    raise BaseException(self.id)
            # some dubious special-casing to make wagon names plural if there are variants, and a named variant group is *not* already used
            # !! this might fail for composite groups where the group has multiple variants from multiple model types, but this specific model has only one variant
            elif len(self.buyable_variants) > 1:
                result = default_result.copy()
                result[0] = result[0].replace("_CAR", "_CARS")
                result[0] = result[0].replace("STR_NAME_SUFFIX_", "STR_WAGON_GROUP_")
            else:
                # no string needed, the name switch will handle using the default name
                result = None
        else:
            raise BaseException(
                "get_name_parts called for wagon consist "
                + self.id
                + " with no context provided"
            )
        return result

    @property
    def joker_by_subclass_rules(self):
        # rules can be over-ridden per subclass, for special handling of jokers for e.g. narrow gauge pax cars etc
        return None

    @property
    def joker(self):
        # jokers are excluded in simplified game mode
        # order is significant here; this is fall through, it's deliberately not else-if
        # option to set _joker per vehicle or per subclass
        if self._joker == True:
            return True

        # can be over-ridden per subclass, for special handling of jokers for e.g. narrow gauge pax cars etc
        if self.joker_by_subclass_rules != None:
            return self.joker_by_subclass_rules

        # all metro wagons are jokers as of May 2024
        if self.base_track_type_name == "METRO":
            return True

        # for wagons/coaches, default jokers are medium and twin lengths, note that this may have been over-ridden by joker_by_subclass_rules above
        if self.subtype in ["B", "D"]:
            return True

        # fall through to default result
        return False


class RandomisedCarMixin(object):
    """
    Mixin to set certain common attributes for randomised car model types.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # eh force this to empty because randomised wagons can't be candidates for randomisation, but the base class might have set this prop
        self.randomised_candidate_groups = []
        # need to turn off colour randomisation on the random consist, it's handled explicitly by the template
        self.use_colour_randomisation_strategies = False

    @property
    def joker(self):
        # no randomised wagons in simplified gameplay mode
        return True


class AlignmentCarUnit(CarModelTypeBase):
    """
    For checking sprite alignment
    """

    model_type_id_stem = "alignment_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no speed limit
        self.speed_class = None
        # refit nothing
        self.class_refit_groups = []
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        # free
        self.buy_cost_adjustment_factor = 0
        # no random CC, no flip
        self.use_colour_randomisation_strategies = False


class AutomobileCarBase(CarModelTypeBase):
    """
    Transports automobiles (cars, trucks, tractors etc).
    'Automobile' is used as name to avoid confusion with 'Vehicles' or 'Car'.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_NO_WEATHERING"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE_NO_WEATHERING"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY_NO_WEATHERING"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["PASS", "VEHI", "ENSP", "FMSP"]
        self.label_refits_disallowed = []
        self.default_cargos = ["VEHI"]
        # special flag to turn on cargo subtypes specific to vehicles, can be made more generic if subtypes need to be extensible in future
        # self.use_cargo_subytpes_VEHI = True
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        if self.subtype == "D":
            formation_ruleset = "articulated_permanent_twin_sets"
        else:
            formation_ruleset = self._formation_ruleset
        # automobile cars can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random automobile cargos, which would also cause new random wagon colour
        # ...wouldn't be desirable anyway because they are pseudo-articulated units
        self.gestalt_graphics = GestaltGraphicsAutomobilesTransporter(
            self.spritelayer_cargo_layers,
            formation_ruleset=formation_ruleset,
            liveries=self.liveries,
        )


class AutomobileSingleDeckCar(AutomobileCarBase):
    """
    Automobile transporter with single flat deck at conventional height.
    """

    model_type_id_stem = "automobile_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_vehicle_transporter_cars"
        self._joker = True

    @property
    def _formation_ruleset(self):
        return "1_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["default"]


class AutomobileDoubleDeckCar(AutomobileCarBase):
    """
    Automobile transporter with double deck, cars only.
    """

    model_type_id_stem = "double_deck_automobile_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # blah blah, more restrictive refits for double deck, cars only
        self.label_refits_allowed = ["PASS", "VEHI"]
        self.use_cargo_subytpes_VEHI = False
        # double deck cars need an extra masked overlay, which is handled via gestalt_graphics
        self.gestalt_graphics.add_masked_overlay = True

    @property
    def _formation_ruleset(self):
        if self.subtype == "B":
            return "2_unit_sets"
        else:
            return "4_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["double_deck_lower", "double_deck_upper"]


class AutomobileLowFloorCar(AutomobileCarBase):
    """
    Automobile transporter with single deck at lowered height.
    """

    model_type_id_stem = "low_floor_automobile_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_vehicle_transporter_cars"
        self._joker = True

    @property
    def _formation_ruleset(self):
        if self.subtype == "B":
            return "2_unit_sets"
        else:
            return "4_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class AutomobileEnclosedCar(CarModelTypeBase):
    """
    Fully enclosed automobile transporter with, no vehicle sprites shown.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_NO_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_NO_WEATHERING"
        ],
    ]

    model_type_id_stem = "enclosed_automobile_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["PASS", "VEHI", "ENSP", "FMSP"]
        self.label_refits_disallowed = []
        self.default_cargos = ["VEHI"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_vehicle_transporter_cars"
        self._joker = True
        # Graphics configuration
        if self.gen in [3]:
            self.roof_type = "pax_mail_ridged"
        elif self.gen in [4]:
            self.roof_type = "pax_mail_smooth"
        elif self.gen in [5]:
            self.roof_type = None
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BolsterCarBase(CarModelTypeBase):
    """
    Base class for specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_flatbed_freight"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["long_products"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "bolster_car_randomised",
            "metal_product_car_mixed_randomised",
            "metal_product_car_uncovered_randomised",
        ]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_bolster_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat", liveries=self.liveries
        )


class BolsterCar(BolsterCarBase):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    model_type_id_stem = "bolster_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BolsterCarHighEnd(BolsterCarBase):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    model_type_id_stem = "high_end_bolster_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BolsterCarRandomised(RandomisedCarMixin, BolsterCarBase):
    """
    Random choice of bolster car sprite, from available bolster cars.
    """

    model_type_id_stem = "bolster_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_bolster_cars"
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class BoxCarBase(CarModelTypeBase):
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
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]


class BoxCarType1(BoxCarBase):
    """
    Standard box car / van
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "box_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "box_car_randomised",
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_box_cars"
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {"unweathered": graphics_constants.box_livery_recolour_map}
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BoxCarType2(BoxCarBase):
    """
    Alternative livery for standard box car / van
    """

    liveries = [
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
    ]

    model_type_id_stem = "box_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "box_car_randomised",
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_box_cars"
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.box_car_type_2_body_recolour_map,
            "weathered": graphics_constants.box_car_type_2_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            input_spritesheet_delegate_id=self.get_input_spritesheet_delegate_id_wagon(
                "box_car_type_1"
            ),
            weathered_variants=weathered_variants,
            liveries=self.liveries,
        )


class BoxCarCurtainSide(BoxCarBase):
    """
    Curtain side box car - same refits as box car.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "curtain_side_box_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_curtain_side"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "box_car_randomised",
            "piece_goods_car_covered_randomised",
            "piece_goods_car_manufacturing_parts_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_box_cars"
        self._joker = True
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.curtain_side_livery_recolour_map
        }
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BoxCarMerchandise(BoxCarBase):
    """
    Alternative livery for standard box car / van
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "merchandise_box_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_goods"]
        # don't include in random box car group, at least for pony, looks bad - other rosters may differ?
        self.randomised_candidate_groups = [
            "piece_goods_car_covered_randomised",
            "piece_goods_car_manufacturing_parts_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        # CC1 roof is a bit of a non-standard thing, but seems to work
        self.roof_type = "freight_cc1"
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BoxCarRandomised(RandomisedCarMixin, BoxCarBase):
    """
    Random choice of box car sprite, from available box cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
    ]

    model_type_id_stem = "box_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_box_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=self.liveries,
        )


class BoxCarSlidingWallBase(BoxCarBase):
    """
    Base for sliding wall van - (cargowagon, habfiss, thrall, pullman all-door car etc) - same refits as box car.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_sliding_wall"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_sliding_wall_cars"
        self._joker = True


class BoxCarSlidingWallType1(BoxCarSlidingWallBase):
    """
    Sliding wall van - (cargowagon, habfiss, thrall, pullman all-door car etc) - same refits as box car.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "sliding_wall_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        if self.base_track_type_name == "NG":
            self.roof_type = "freight_cc1"
        else:
            self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.sliding_wall_livery_recolour_map,
            "weathered": graphics_constants.sliding_wall_livery_recolour_map_weathered,
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BoxCarSlidingWallType2(BoxCarSlidingWallBase):
    """
    Sliding wall van - (cargowagon, habfiss, thrall, pullman all-door car etc) - same refits as box car.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "sliding_wall_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups.extend(
            ["piece_goods_car_manufacturing_parts_randomised"]
        )
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {"unweathered": graphics_constants.box_livery_recolour_map}
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BoxCarVehicleParts(BoxCarBase):
    """
    Vehicle parts box car, van - same refits as box car, just a specific visual variation.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "vehicle_parts_box_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["box_vehicle_parts"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self._joker = True
        self.randomised_candidate_groups = [
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_sliding_wall_cars"
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {"unweathered": graphics_constants.box_livery_recolour_map}
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class BulkOpenCarBase(CarModelTypeBase):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos, same set as hopper cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["dump_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_dump_bulk"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["dump"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, liveries=self.liveries
        )


class BulkOpenCarAggregateBase(BulkOpenCarBase):
    """
    Base class for aggregate dump car.
    Same as standard dump car, but different appearance and default cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_aggregates"]
        self.randomised_candidate_groups = [
            "aggregate_bulk_open_car_randomised",
            "bulk_car_box_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_aggregate_bulk_open_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.aggregate_bulk_open_livery_recolour_map,
            "weathered": graphics_constants.aggregate_bulk_open_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, weathered_variants=weathered_variants, liveries=self.liveries
        )


class BulkOpenCarAggregateType1(BulkOpenCarAggregateBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    model_type_id_stem = "aggregate_bulk_open_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarAggregateType2(BulkOpenCarAggregateBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    model_type_id_stem = "aggregate_bulk_open_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarAggregateType3(BulkOpenCarAggregateBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    model_type_id_stem = "aggregate_bulk_open_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarAggregateRandomised(RandomisedCarMixin, BulkOpenCarAggregateBase):
    """
    Random choice of aggregate car.
    """

    model_type_id_stem = "aggregate_bulk_open_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # needed to clear randomised set by base class
        self.randomised_candidate_groups = []
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class BulkOpenCarHeavyDuty(BulkOpenCarBase):
    """
    Heavy duty dump car, higher capacity, reduced speed (set in vehicle class, not consist)
    """

    model_type_id_stem = "heavy_duty_dump_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        # double the default weight
        self.weight_factor = 2
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        ]


class BulkOpenCarMineralBase(BulkOpenCarBase):
    """
    Base class for standard dump car (Mineral Wagon in UK terms).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "bulk_car_box_randomised",
            "bulk_car_mixed_randomised",
            "mineral_bulk_open_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_mineral_bulk_open_cars"
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        ]


class BulkOpenCarMineral(BulkOpenCarMineralBase):
    """
    Standard dump car (Mineral Wagon in UK terms).
    """

    model_type_id_stem = "mineral_bulk_open_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarMineralHighSide(BulkOpenCarMineralBase):
    """
    Standard dump car (Mineral Wagon in UK terms), with high sides.
    """

    model_type_id_stem = "mineral_bulk_open_car_high_side"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarMineralLowSide(BulkOpenCarMineralBase):
    """
    Standard dump car (Mineral Wagon in UK terms), with low sides.
    """

    model_type_id_stem = "mineral_bulk_open_car_low_side"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarMineralRandomised(RandomisedCarMixin, BulkOpenCarMineralBase):
    """
    Random choice of standard dump car (Mineral Wagon in UK terms).
    """

    model_type_id_stem = "mineral_bulk_open_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # needed to clear randomised set by base class
        self.randomised_candidate_groups = []
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_mineral_bulk_open_cars"
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class BulkOpenCarScrapMetalBase(BulkOpenCarBase):
    """
    Scrap Metal Car
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_scrap"]
        self.randomised_candidate_groups = [
            "scrap_metal_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_scrap_metal_cars"
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        ]


class BulkOpenCarScrapMetalType1(BulkOpenCarScrapMetalBase):
    """
    Scrap Metal Car
    """

    model_type_id_stem = "scrap_metal_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarScrapMetalType2(BulkOpenCarScrapMetalBase):
    """
    Scrap Metal Car
    """

    model_type_id_stem = "scrap_metal_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarScrapMetalRandomised(RandomisedCarMixin, BulkOpenCarScrapMetalBase):
    """
    Random choice of scrap metal car sprite.
    """

    model_type_id_stem = "scrap_metal_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class BulkOpenCarTipplerBase(BulkOpenCarBase):
    """
    Base class for Tippler (dump car).
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_ore"]
        self.randomised_candidate_groups = [
            "bulk_car_box_randomised",
            "bulk_car_mixed_randomised",
            "tippler_bulk_open_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_tippler_bulk_open_cars"
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        ]


class BulkOpenCarTipplerType1(BulkOpenCarTipplerBase):
    """
    Tippler (dump car).
    """

    model_type_id_stem = "tippler_bulk_open_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarTipplerType2(BulkOpenCarTipplerBase):
    """
    Tippler (dump car).
    """

    model_type_id_stem = "tippler_bulk_open_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BulkOpenCarTipplerRotaryType1(BulkOpenCarTipplerBase):
    """
    Tippler (dump car).
    """

    model_type_id_stem = "tippler_rotary_bulk_open_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # needed to clear randomised set by base class - rotary tipplers don't look good as randomisation candidates
        self.randomised_candidate_groups = []


class BulkOpenCarTipplerRandomised(RandomisedCarMixin, BulkOpenCarTipplerBase):
    """
    Random choice of tippler (dump car).
    """

    model_type_id_stem = "tippler_bulk_open_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # needed to clear randomised set by base class
        self.randomised_candidate_groups = []
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_tippler_bulk_open_cars"
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


# not in alphabetical order as it depends on subclassing BulkOpenCarBase
class BulkCarBoxRandomised(RandomisedCarMixin, BulkOpenCarBase):
    """
    Random choice of bulk car sprite, from available dump / box open cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "bulk_car_box_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_named_buyable_variant_group = "wagon_group_bulk_cars_randomised"
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class BulkCarHopperRandomised(RandomisedCarMixin, BulkOpenCarBase):
    """
    Random choice of bulk car sprite, from available dump / hopper cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "bulk_car_hopper_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_bulk_cars_randomised"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


# not in alphabetical order as it depends on subclassing BulkOpenCarBase
class BulkCarMixedRandomised(RandomisedCarMixin, BulkOpenCarBase):
    """
    Random choice of bulk car sprite, from available dump / hopper cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "bulk_car_mixed_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_bulk_cars_randomised"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class CabooseCarUnit(CarModelTypeBase):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    model_type_id_stem = "caboose_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no speed limit
        self.speed_class = None
        # refit nothing, don't mess with this, it breaks auto-replace
        self.class_refit_groups = []
        # label refits are just to get caboose to use freight car livery group
        # try to catch enough common cargos otherwise the vehicle will be hidden; don't use MAIL as that forces pax colour group
        self.label_refits_allowed = ["ENSP", "GOOD", "COAL", "WOOD", "OIL_"]
        self.label_refits_disallowed = []
        # chop down caboose costs, they're just eye candy eh
        self.buy_cost_adjustment_factor = 0.75
        self.use_colour_randomisation_strategies = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(
            recolour_map=graphics_constants.caboose_car_body_recolour_map,
            liveries=self.liveries,
            spriterow_labels=self.model_def.spriterow_labels,
            caboose_families=self.model_def.caboose_families,
            buy_menu_sprite_pairs=self.model_def.buy_menu_sprite_pairs,
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

    @property
    def random_reverse(self):
        return True


class CaneBinCar(CarModelTypeBase):
    """
    Specialist transporter (narrow gauge bin) for (sugar) cane
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "cane_bin_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        # limited refits by design eh
        self.label_refits_allowed = ["SGCN"]
        self.label_refits_disallowed = []
        self.default_cargos = ["SGCN"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        # there will unused vehicles sprites for cargo states, but it's ok in this limited case
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, weathered_variants=weathered_variants, liveries=self.liveries
        )


class CarbonBlackHopperCar(CarModelTypeBase):
    """
    Dedicated covered hopper car for carbon black.  No other cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "carbon_black_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["CBLK"]
        self.label_refits_disallowed = []
        self.default_cargos = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.carbon_black_hopper_car_livery_recolour_map,
            "weathered": graphics_constants.carbon_black_hopper_car_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class CoilBuggyCarUnit(CarModelTypeBase):
    """
    Dedicated (steel mill) buggy car for coils. Not a standard railcar. No other refits.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    # note does NOT subclass CoilCarBase - different type of consist
    model_type_id_stem = "coil_buggy_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # none needed
        self.class_refit_groups = []
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "metal_products"
        ]
        # none needed
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["coil"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        # double the default weight
        self.weight_factor = 2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self._joker = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        # cargo_row_map blank, all default to same
        cargo_row_map = {}
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            liveries=self.liveries,
            cargo_row_map=cargo_row_map,
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", 10],
                ["loading_0", 40],
                ["loaded_0", 40],
            ],
        )


class CoilCarBase(CarModelTypeBase):
    """
    Coil car - for finished metals (steel, copper etc).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = []
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "metal_products"
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]


class CoilCarCoveredAsymmetric(CoilCarBase):
    """
    Covered coil car.  No visible cargo.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
    ]

    model_type_id_stem = "coil_car_covered_asymmetric"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil_covered"]
        self.randomised_candidate_groups = [
            "dedicated_coil_car_randomised",
            "metal_product_car_covered_randomised",
            "metal_product_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_coil_car_asymmetric_body_recolour_map,
            "weathered": graphics_constants.covered_coil_car_asymmetric_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            piece="coil",
            has_cover=True,
        )

    @property
    def random_reverse(self):
        return True


class CoilCarCovered(CoilCarBase):
    """
    Covered coil car.  No visible cargo.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    model_type_id_stem = "coil_car_covered"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil_covered"]
        self.randomised_candidate_groups = [
            "dedicated_coil_car_randomised",
            "metal_product_car_covered_randomised",
            "metal_product_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            piece="coil",
            has_cover=True,
        )


class CoilCarTarpaulin(CoilCarBase):
    """
    Covered coil car.  No visible cargo.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    model_type_id_stem = "coil_car_tarpaulin"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil_covered"]
        self.randomised_candidate_groups = [
            "dedicated_coil_car_randomised",
            "metal_product_car_covered_randomised",
            "metal_product_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.coil_car_tarpaulin_body_recolour_map,
            "weathered": graphics_constants.coil_car_tarpaulin_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            piece="coil",
            has_cover=True,
        )


class CoilCarUncovered(CoilCarBase):
    """
    Uncovered coil car.  Visible cargo.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    model_type_id_stem = "coil_car_uncovered"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["coil"]
        self.randomised_candidate_groups = [
            "dedicated_coil_car_randomised",
            "metal_product_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="coil", liveries=self.liveries
        )


class DedicatedCoilCarRandomised(RandomisedCarMixin, CoilCarBase):
    """
    Random choice of covered or uncovered coil car.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
    ]

    model_type_id_stem = "dedicated_coil_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=self.liveries,
        )

    @property
    def random_reverse(self):
        return True


class CoveredHopperCarBase(CarModelTypeBase):
    """
    Bulk cargos needing covered protection.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["covered_hopper_freight_any_grade"]
        # we assume generic covered hoppers refit anything suitable from the more specialist types
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "covered_hoppers_pellet_powder"
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_hopper_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class CoveredHopperCarType1(CoveredHopperCarBase):
    """
    Default covered hopper type.
    """

    model_type_id_stem = "covered_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"


class CoveredHopperCarType2(CoveredHopperCarBase):
    """
    Default covered hopper type.
    """

    model_type_id_stem = "covered_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"
        self._joker = True


class CoveredHopperCarType3(CoveredHopperCarBase):
    """
    Default covered hopper type.
    """

    model_type_id_stem = "covered_hopper_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"
        self._joker = True


class CoveredHopperCarRandomised(RandomisedCarMixin, CoveredHopperCarBase):
    """
    Random choice of covered hopper car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    model_type_id_stem = "covered_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=1,
            liveries=self.liveries,
        )


class CoveredHopperCarSwingRoof(CoveredHopperCarBase):
    """
    Covered hopper with a swing roof hatch, same refits as standard covered hopper, just a visual variant.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "swing_roof_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._joker = True
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_hopper_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class ExpressCarUnit(CarModelTypeBase):
    """
    Express cars - express freight, valuables, mails.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_RED"],
    ]

    model_type_id_stem = "express_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["express"]
        self.randomised_candidate_groups = ["express_food_car_randomised"]
        # adjust weight factor because express car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        # keep matched to MailCar
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
        # Graphics configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        weathered_variants = {"unweathered": graphics_constants.box_livery_recolour_map}
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class ExpressFoodCarRandomised(RandomisedCarMixin, CarModelTypeBase):
    """
    Random choice of food car sprite, noting limited refits because it includes food tankers.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "express_food_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["liquids_food_grade"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["edibles_tank"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "food_wagons"
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=self.liveries,
        )


class ExpressFoodTankCarBase(CarModelTypeBase):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    Formerly known as 'Edibles Tanker', renamed in 2024 to 'Food Tanker' to be easily understand.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["liquids_food_grade"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["edibles_tank"]
        self.randomised_candidate_groups = [
            "food_express_tank_car_randomised",
            "express_food_car_randomised",
        ]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "food_wagons"
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_food_express_tank_cars"
        # Graphics configuration
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.refrigerated_livery_recolour_map,
            "weathered": graphics_constants.refrigerated_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class ExpressFoodTankCarType1(ExpressFoodTankCarBase):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    Formerly known as 'Edibles Tanker', renamed in 2024 to 'Food Tanker' to be easily understand.
    """

    model_type_id_stem = "food_express_tank_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ExpressFoodTankCarType2(ExpressFoodTankCarBase):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    Formerly known as 'Edibles Tanker', renamed in 2024 to 'Food Tanker' to be easily understand.
    """

    model_type_id_stem = "food_express_tank_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ExpressFoodTankCarRandomised(RandomisedCarMixin, ExpressFoodTankCarBase):
    """
    Random choice of express food tanker.
    """

    model_type_id_stem = "food_express_tank_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class ExpressIntermodalCarUnit(CarModelTypeBase):
    """
    Express intermodal container cars - express freight, valuables, mails.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    model_type_id_stem = "express_intermodal_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["express"]
        self._loading_speed_multiplier = 2
        # adjust weight factor because express intermodal car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        # keep matched to MailCar
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
        self._joker = True
        self.use_colour_randomisation_strategies = False
        # Graphics configuration
        # !! note to future, if e.g. NA Horse needs longer express intermodal sets, set the formation_ruleset conditionally by checking roster
        # intermodal container wagons can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            formation_ruleset="2_unit_sets", liveries=self.liveries
        )

    @property
    def spritelayer_cargo_layers(self):
        # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
        # !! express intermodal all default currently, extend as needed
        return ["default"]


class FarmProductsBoxCarBase(CarModelTypeBase):
    """
    Bae for farm type cargos - box cars / vans.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # note this is not derived from BoxCarBase, it's a standalone type
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "farm_food_products"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["farm_products_box"]
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_farm_product_box_cars"
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.farm_product_box_car_livery_recolour_map,
            "weathered": graphics_constants.farm_product_box_car_livery_recolour_map_weathered,
        }
        # company colour not used on these wagons, so set SWOOSH as JFDI
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class FarmProductsBoxCarType1(FarmProductsBoxCarBase):
    """
    Farm type cargos - box cars / vans.
    """

    model_type_id_stem = "farm_product_box_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_box_car_randomised",
        ]


class FarmProductsBoxCarType2(FarmProductsBoxCarBase):
    """
    Farm type cargos - box cars / vans.
    """

    model_type_id_stem = "farm_product_box_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_box_car_randomised",
        ]


class FarmProductsBoxCarRandomised(RandomisedCarMixin, FarmProductsBoxCarBase):
    """
    Random choice of farm products box car / van sprite.
    """

    model_type_id_stem = "farm_product_box_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=1,
            liveries=liveries,
        )


class FarmProductsHopperCarBase(CarModelTypeBase):
    """
    Farm type cargos - covered hoppers.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["covered_hopper_freight_food_grade"]
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "farm_food_products"
        ]
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["farm_products_hopper"]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_farm_product_hopper_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.farm_product_hopper_car_livery_recolour_map,
            "weathered": graphics_constants.farm_product_hopper_car_livery_recolour_map_weathered,
        }
        # company colour not used on these wagons, so use SWOOSH as JFDI
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class FarmProductsHopperCarType1(FarmProductsHopperCarBase):
    """
    Farm type cargos - covered hoppers.
    """

    model_type_id_stem = "farm_product_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_hopper_car_randomised",
        ]


class FarmProductsHopperCarType2(FarmProductsHopperCarBase):
    """
    Farm type cargos - covered hoppers.
    """

    model_type_id_stem = "farm_product_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_hopper_car_randomised",
        ]


class FarmProductsHopperCarRandomised(RandomisedCarMixin, FarmProductsHopperCarBase):
    """
    Random choice of farm products hopper sprite.
    """

    model_type_id_stem = "farm_product_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class FoodHopperCarBase(FarmProductsHopperCarBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_food_hopper_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.refrigerated_livery_recolour_map,
            "weathered": graphics_constants.refrigerated_livery_recolour_map_weathered,
        }
        # company colour not used on these wagons, so use SWOOSH as JFDI
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class FoodHopperCarType1(FoodHopperCarBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    model_type_id_stem = "food_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarType2(FoodHopperCarBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    model_type_id_stem = "food_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarType3(FoodHopperCarBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    model_type_id_stem = "food_hopper_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarRandomised(RandomisedCarMixin, FoodHopperCarBase):
    """
    Random choice of food hopper sprite.
    """

    model_type_id_stem = "food_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarBase(CarModelTypeBase):
    """
    Flatbed - refits wide range of cargos, but not bulk.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["flatbed_freight"]
        self.label_refits_allowed = ["GOOD"]
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_flatbed_freight"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["flat"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat", liveries=self.liveries
        )


class FlatCarBulkheadBase(FlatCarBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["bulkhead"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = ["bulkhead_flat_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_bulkhead_flat_cars"
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat", liveries=self.liveries
        )


class FlatCarBulkheadType1(FlatCarBulkheadBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    # low or high bulkhead? stakes or not?
    model_type_id_stem = "bulkhead_flat_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FlatCarBulkheadType2(FlatCarBulkheadBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    # low or high bulkhead? stakes or not?
    model_type_id_stem = "bulkhead_flat_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FlatCarBulkheadRandomised(RandomisedCarMixin, FlatCarBulkheadBase):
    """
    Random choice of bulkhead flat car sprite.
    """

    model_type_id_stem = "bulkhead_flat_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarDropEnd(FlatCarBase):
    """
    Wagon with droppable end flaps - variant on flat wagon, refits same
    """

    model_type_id_stem = "drop_end_flat_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["plate"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "flat_car_randomised",
            "metal_product_car_mixed_randomised",
            "metal_product_car_uncovered_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_flat_cars"
        self._joker = True


class FlatCarDropSide(FlatCarBase):
    """
    Wagon with droppable low sides - variant on flat wagon, refits same
    """

    model_type_id_stem = "drop_side_flat_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["plate"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "flat_car_randomised",
            "metal_product_car_mixed_randomised",
            "metal_product_car_uncovered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_flat_cars"
        self._joker = True


class FlatCar(FlatCarBase):
    """
    Flatbed - no stakes, visible cargo.
    """

    model_type_id_stem = "flat_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "flat_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_flat_cars"


class FlatCarHeavyDuty(FlatCarBase):
    """
    Heavy duty flat car, higher capacity, reduced speed (set in vehicle class, not consist)
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "heavy_duty_flat_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        # double the default weight
        self.weight_factor = 2
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat", liveries=self.liveries
        )


class FlatCarMillBase(FlatCarBase):
    """
    Variant of flat wagon designed specfically for steel industry.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["bulkhead"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "metal_product_car_uncovered_randomised",
            "mill_flat_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_mill_flat_cars"
        self._joker = True


class FlatCarMillType1(FlatCarMillBase):
    """
    Variant of flat wagon designed specfically for steel industry.
    """

    # low or high mill? stakes or not?
    model_type_id_stem = "mill_flat_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FlatCarMillType2(FlatCarMillBase):
    """
    Variant of flat wagon designed specfically for steel industry.
    """

    # low or high mill? stakes or not?
    model_type_id_stem = "mill_flat_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FlatCarMillRandomised(RandomisedCarMixin, FlatCarMillBase):
    """
    Random choice of mill flat car sprite.
    """

    model_type_id_stem = "mill_flat_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarRandomised(RandomisedCarMixin, FlatCarBase):
    """
    Random choice of flat car sprite, from available coil cars, bolster cars etc.
    """

    model_type_id_stem = "flat_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_flat_cars"
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_segmented_block_train",
            dice_colour=2,
            liveries=liveries,
        )


class GasTankCarBase(CarModelTypeBase):
    """
    Specialist tank cars for gases, e.g. Oxygen, Chlorine, Ammonia, Propylene etc.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        super().__init__(**kwargs)
        self.class_refit_groups = ["cryo_gases"]
        self.label_refits_allowed = []
        self.default_cargos = polar_fox.constants.default_cargos["cryo_gases"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.33
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.cryo_tanker_livery_recolour_map,
            "weathered": graphics_constants.cryo_tanker_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class GasTankCarPressure(GasTankCarBase):
    """
    Pressure tank cars for gases under pressure at low temperatue, e.g. Chlorine etc.
    """

    model_type_id_stem = "pressure_tank_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_pressure_tank_cars"


class GasTankCarCryo(GasTankCarBase):
    """
    Specialist insulated and pressurised tank cars for gases under pressure at low temperatue, e.g. Oxygen etc.
    """

    model_type_id_stem = "cryo_tank_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_pressure_tank_cars"
        self._joker = True


class HopperCarBase(CarModelTypeBase):
    """
    Common base class for dump cars.
    Limited set of bulk (mineral) cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["dump_freight"]
        # none needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_dump_bulk"
        ]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self.randomised_candidate_groups = [
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, liveries=self.liveries
        )


class HopperCarAggregateBase(HopperCarBase):
    """
    Base class for hopper for rock cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_aggregates"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_aggregate_hopper_cars"


class HopperCarAggregateType1(HopperCarAggregateBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    model_type_id_stem = "aggregate_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "aggregate_hopper_car_randomised",
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        ]


class HopperCarAggregateType2(HopperCarAggregateBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    model_type_id_stem = "aggregate_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "aggregate_hopper_car_randomised",
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        ]


class HopperCarAggregateType3(HopperCarAggregateBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    model_type_id_stem = "aggregate_hopper_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "aggregate_hopper_car_randomised",
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        ]


class HopperCarAggregateRandomised(RandomisedCarMixin, HopperCarAggregateBase):
    """
    Random choice of aggregate hopper car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "aggregate_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_aggregate_hopper_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class HopperCar(HopperCarBase):
    """
    Standard hopper car. Defaults to coal.
    """

    model_type_id_stem = "hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]
        self.randomised_candidate_groups = [
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
            "hopper_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_hopper_cars"


class HopperCarHighSide(HopperCarBase):
    """
    Hopper for ore cargos, same refits as standard hopper, just a visual variant.
    """

    model_type_id_stem = "hopper_car_high_side"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_ore"]
        self.randomised_candidate_groups = [
            "bulk_car_hopper_randomised",
            "bulk_car_mixed_randomised",
            "hopper_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_hopper_cars"
        self._joker = True


class HopperCarMGRBase(HopperCarBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SULPHUR_STRAW"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SULPHUR"],
        global_constants.freight_wagon_liveries["FREIGHT_STRAW"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # don't include MGR hoppers in randomised lists, they don't look good
        self.randomised_candidate_groups = []
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_mgr_hopper_cars"
        self._joker = True
        # adjust default liveries set by the base class
        weathered_variants = {
            "unweathered": graphics_constants.mgr_hopper_body_recolour_map,
            "weathered": graphics_constants.mgr_hopper_body_recolour_map_weathered,
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # player choice, various others tried, not needed
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, weathered_variants=weathered_variants, liveries=self.liveries
        )


class HopperCarMGR(HopperCarMGRBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    model_type_id_stem = "mgr_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HopperCarMGRTopHood(HopperCarMGRBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    model_type_id_stem = "mgr_top_hood_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HopperCarRandomised(RandomisedCarMixin, HopperCarBase):
    """
    Random choice of hopper car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
    ]

    model_type_id_stem = "hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # needed to clear randomised set by base class
        self.randomised_candidate_groups = []
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_hopper_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class HopperCarRock(HopperCarBase):
    """
    Hopper for rock cargos, same refits as standard hopper, just a visual variant.
    """

    model_type_id_stem = "rock_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_rock"]
        # don't include rock hoppers in randomised lists, they don't look good
        self.randomised_candidate_groups = ["bulk_car_hopper_randomised"]
        self._joker = True
        # Graphics configuration
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_GREMLIN_GREEN_SILVER"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
            global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
            global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
            global_constants.freight_wagon_liveries["FREIGHT_SAND"],
            global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
            global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        ]


class HopperCarSideDoor(HopperCarBase):
    """
    Side door hopper (saddle-bottom hopper).
    """

    model_type_id_stem = "side_door_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]
        # not eligible for randomisation, doesn't look right
        self.randomised_candidate_groups = []
        self._joker = True


class HopperCarSkip(HopperCarBase):
    """
    Dedicated (narrow gauge) skip variant of hoppers
    Defaults to rock/stone-type cargos.
    """

    model_type_id_stem = "skip_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_rock"]
        # not eligible for randomisation, breaks due to articulation
        self.randomised_candidate_groups = []
        self._joker = True
        # adjust default liveries set by the base class
        self.gestalt_graphics.liveries = [
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_VARIETY"
            ],
            global_constants.freight_wagon_liveries[
                "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
            ],
            global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
            global_constants.freight_wagon_liveries[
                "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
            ],
            global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
            global_constants.freight_wagon_liveries["FREIGHT_GREY"],
            global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
            # player choice, various others tried, not needed
        ]


class IngotCarUnit(CarModelTypeBase):
    """
    Dedicated car for steel / iron ingots. A steel mill ingot buggy, not a standard railcar. No other refits.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "ingot_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # none needed
        self.class_refit_groups = []
        self.label_refits_allowed = ["STIG", "IRON", "CSTI", "STCB", "STST", "STAL"]
        # none needed
        self.label_refits_disallowed = []
        self.default_cargos = ["IRON"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        # double the default weight
        self.weight_factor = 2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self._joker = True
        self.suppress_animated_pixel_warnings = True
        # leave cargo_row_map blank, all default to same
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        cargo_row_map = {}
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            liveries=self.liveries,
            cargo_row_map=cargo_row_map,
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", 10],
                ["loading_0", 40],
                ["loaded_0", 70],
            ],
        )


class IntermodalCarBase(CarModelTypeBase):
    """
    General cargo - refits everything except mail, pax.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["all_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["box_intermodal"]
        self._loading_speed_multiplier = 2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # intermodal containers can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        self.use_colour_randomisation_strategies = False
        # Graphics configuration
        # various rulesets are supported, per consist, (or could be extended to checks per roster)
        # this wasn't moved to @property due to laziness, as of Jan 2025
        if self.model_def.formation_ruleset is not None:
            formation_ruleset = self.model_def.formation_ruleset
        else:
            formation_ruleset = "4_unit_sets"
        # !! as of April 2023, company colour isn't used for default intermodal sprite, so use SWOOSH as JFDI
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            formation_ruleset=formation_ruleset, liveries=self.liveries
        )


class IntermodalCarUnit(IntermodalCarBase):
    """
    Default intermodal car - simple flat platform at default height.
    """

    model_type_id_stem = "intermodal_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_intermodal_cars"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        # the 'default' for NG is the same as for low_floor so just re-use that for now
        if self.base_track_type_name == "NG":
            return ["low_floor"]
        else:
            return ["default"]


class IntermodalLowFloorCar(IntermodalCarBase):
    """
    Low floor intermodal car - simple flat platform at height -1
    """

    model_type_id_stem = "low_floor_intermodal_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_intermodal_cars"
        self._joker = True

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class KaolinHopperCar(CarModelTypeBase):
    """
    Dedicated to kaolin (china clay).
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "kaolin_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["KAOL", "CLAY"]
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.kaolin_hopper_car_livery_recolour_map,
            "weathered": graphics_constants.kaolin_hopper_car_livery_recolour_map_weathered,
        }
        # tried more liveries, doesn't add anything
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class LivestockCar(CarModelTypeBase):
    """
    Specialist transporter for livestock.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "livestock_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["LVST"]
        self.label_refits_disallowed = []
        # no point using polar fox default_cargos for a vehicle with single refit
        self.default_cargos = ["LVST"]
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.1
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.livestock_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class LogCar(CarModelTypeBase):
    """
    Specialist transporter for logs
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
    ]

    model_type_id_stem = "log_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        # limited refits by design eh
        self.label_refits_allowed = ["WOOD"]
        self.label_refits_disallowed = []
        self.default_cargos = ["WOOD"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="tree_length_logs", liveries=self.liveries
        )


class MailCarBase(CarModelTypeBase):
    """
    Common base class for mail cars.
    """

    def __init__(self, **kwargs):
        # don't set model_type_id here, let subclasses do it
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # keep matched to ExpressCarUnit
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
        self.use_colour_randomisation_strategies = False
        # roof configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["default"]

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]

    @property
    def joker_by_subclass_rules(self):
        # special-case handling for simplified mode with narrow gauge mail cars
        # make short and medium lengths available, for flexibility
        if self.base_track_type_name == "NG":
            if self.subtype in ["A", "B"]:
                return False
            else:
                return True
        # return None if there are no special rules, then the default rules will be applied by the calling function
        return None


class MailRailcarTrailerCarBase(MailCarBase):
    """
    Common base class for mail railcar trailer cars.
    """

    def __init__(self, **kwargs):
        # don't set model_type_id here, let subclasses do it
        super().__init__(**kwargs)
        self._buyable_variant_group_id = self.cab_id
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        self.suppress_pantograph_if_no_engine_attached = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self._str_name_suffix = "STR_NAME_SUFFIX_TRAILER"
        self._joker = True
        # faff to avoid pickle failures due to roster lookups when using multiprocessing in graphics pipeline
        self._frozen_pantograph_type = self.cab_consist.pantograph_type

    @property
    def subrole(self):
        return self.cab_consist.subrole

    @property
    def cab_id(self):
        # cab_id is required, must be set in model_def
        return self.model_def.cab_id

    @property
    def power_by_power_source(self):
        # necessary to ensure that pantograph provision can work, whilst not giving the vehicle any actual power
        return {key: 0 for key in self.cab_consist.power_by_power_source.keys()}

    @property
    def intro_year_offset(self):
        # get the intro year offset and life props from the cab, to ensure they're in sync
        return self.cab_consist.intro_year_offset

    @property
    def pantograph_type(self):
        return self._frozen_pantograph_type

    @property
    def vehicle_family_badge(self):
        return "vehicle_family/" + self._buyable_variant_group_id

    def get_name_parts(self, context):
        # special name handling to use the cab name
        result = [
            "STR_NAME_" + self.cab_id.upper(),
            self._str_name_suffix,
        ]
        return result


class MailCar(MailCarBase):
    """
    Mail cars - also handle express freight, valuables.
    """

    model_type_id_stem = "mail_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_mail_car")
        # mail cars also treated as pax for rulesets (to hide adjacent pax brake coach)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.speed_class = "express"
        # adjust weight factor because mail car freight capacity is 1/2 of other wagons, but weight should be same
        self.weight_factor = polar_fox.constants.mail_multiplier
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
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
        liveries = self.roster.get_pax_mail_liveries(
            "default_mail_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="mail_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        # pony NG jank directly set role buy menu string here, handles pony gen 4 NG speed bump
        if self.base_track_type_name == "NG" and self.gen < 4:
            return "universal"
        else:
            return "express"


class MailExpressRailcarTrailerCar(MailRailcarTrailerCarBase):
    """
    Unpowered mail trailer car for express railcars.
    Position-dependent sprites for cabs etc.
    """

    model_type_id_stem = "express_railcar_mail_trailer_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 3.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_non_core"
        ]
        self._joker = True
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type_name == "NG" else 1.5
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_4_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class MailHighSpeedCar(MailCarBase):
    """
    High speed (LGV capable) variant of mail car.
    Position-dependent sprites for brake car etc.
    """

    model_type_id_stem = "high_speed_mail_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_mail_car")
        # mail cars also treated as pax for rulesets (to hide adjacent pax brake coach)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.speed_class = "express"
        # buy costs and run costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.9
        self.floating_run_cost_multiplier = 4
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1
        # Graphics configuration
        # mail cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {
            "default": 0,
            "first": 1,
            "last": 1,
            "special": 2,
        }
        liveries = self.roster.get_pax_mail_liveries(
            "default_mail_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="mail_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        return "very_high_speed"

    @property
    def lgv_capable(self):
        return True


class MailHSTCar(MailCarBase):
    """
    Trailer dedicated for Mail on HST-type trains (no wagon attach, but matching stats and livery).
    """

    model_type_id_stem = "hst_mail_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._buyable_variant_group_id = self.cab_id
        self._badges.append("ih_ruleset_flags/report_as_mail_car")
        # mail cars also treated as pax for rulesets (to hide adjacent pax brake coach)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.speed_class = "hst"
        self.buy_cost_adjustment_factor = 1.66
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (buffet) coach
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="mail_cars",
            liveries=self.cab_consist.gestalt_graphics.liveries,
        )

    @property
    def subrole(self):
        return self.cab_consist.subrole

    @property
    def cab_id(self):
        # cab_id is required, must be set in model_def
        return self.model_def.cab_id

    @property
    def intro_year_offset(self):
        # get the intro year offset and life props from the cab, to ensure they're in sync
        return self.cab_consist.intro_year_offset

    def get_name_parts(self, context):
        # special name handling to use the cab name
        result = [
            "STR_NAME_" + self.cab_id.upper(),
            "STR_NAME_SUFFIX_HST_MAIL_CAR",
        ]
        return result

    @property
    def is_general_purpose_true_wagon(self):
        return False


class MetalProductCarRandomisedBase(RandomisedCarMixin, CoilCarBase):
    """
    Base class for randomised cold metal car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # because the asymmetric covered wagons can reverse
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = (
            "wagon_group_metal_product_cars_randomised"
        )
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=self.liveries,
        )

    @property
    def random_reverse(self):
        return True


class MetalProductCarCoveredRandomised(MetalProductCarRandomisedBase):
    """
    Random choice of cold metal car sprite, from suitable covered coil cars, vans etc.
    """

    model_type_id_stem = "metal_product_car_covered_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetalProductCarMixedRandomised(MetalProductCarRandomisedBase):
    """
    Random choice of cold metal car sprite, from all suitable metal carrying wagons cars etc.
    """

    model_type_id_stem = "metal_product_car_mixed_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetalProductCarUncoveredRandomised(MetalProductCarRandomisedBase):
    """
    Random choice of cold metal car sprite, from suitable bolster, flat, open cars etc.
    """

    model_type_id_stem = "metal_product_car_uncovered_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarBase(CarModelTypeBase):
    """
    Bulk mineral cargos needing covered protection.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["covered_hopper_freight_non_food_grade"]
        self.label_refits_allowed = polar_fox.constants.allowed_refits_by_label[
            "covered_hoppers_mineral"
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.covered_hopper_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class MineralCoveredHopperCarLimeBase(MineralCoveredHopperCarBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_mineral"]
        self.randomised_candidate_groups = [
            "lime_covered_hopper_car_randomised",
            "covered_bulk_car_randomised",
        ]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_lime_covered_hopper_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.lime_hopper_car_livery_recolour_map,
            "weathered": graphics_constants.lime_hopper_car_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class MineralCoveredHopperCarLimeType1(MineralCoveredHopperCarLimeBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    model_type_id_stem = "lime_covered_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeType2(MineralCoveredHopperCarLimeBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    model_type_id_stem = "lime_covered_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeType3(MineralCoveredHopperCarLimeBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    model_type_id_stem = "lime_covered_hopper_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeRandomised(
    RandomisedCarMixin, MineralCoveredHopperCarLimeBase
):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    model_type_id_stem = "lime_covered_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # clear from randomisation groups
        self.randomised_candidate_groups = []
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


# not in alphabetical order as it depends on subclassing CoveredHopperCarBase
class MineralCoveredHopperCarRandomised(
    RandomisedCarMixin, MineralCoveredHopperCarBase
):
    """
    Random choice of mineral covered hopper car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "covered_bulk_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=3,
            liveries=self.liveries,
        )


class MineralCoveredHopperCarRollerRoofBase(MineralCoveredHopperCarBase):
    """
    Mineral covered hopper with a rollover roof.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._joker = True
        self.default_cargos = polar_fox.constants.default_cargos["covered_roller_roof"]
        self.randomised_candidate_groups = [
            "roller_roof_hopper_car_randomised",
            "covered_bulk_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_roller_roof_hopper_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.roller_roof_hopper_body_recolour_map,
            "weathered": graphics_constants.roller_roof_hopper_body_recolour_map_weathered,
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class MineralCoveredHopperCarRollerRoofType1(MineralCoveredHopperCarRollerRoofBase):
    """
    Mineral covered hopper with a rollover roof.
    """

    model_type_id_stem = "roller_roof_hopper_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarRollerRoofType2(MineralCoveredHopperCarRollerRoofBase):
    """
    Mineral covered hopper with a rollover roof.
    """

    model_type_id_stem = "roller_roof_hopper_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarRollerRoofRandomised(
    RandomisedCarMixin, MineralCoveredHopperCarRollerRoofBase
):
    """
    Mineral covered hopper with a rollover roof.
    """

    model_type_id_stem = "roller_roof_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # clear from randomisation groups
        self.randomised_candidate_groups = []
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class MineralCoveredHopperCarSaltBase(MineralCoveredHopperCarBase):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OCHRE_SAND"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_GREMLIN_GREEN_SILVER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREMLIN_GREEN"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SAND"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_chemical"]
        self.randomised_candidate_groups = [
            "covered_bulk_car_randomised",
            "salt_covered_hopper_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_salt_covered_hopper_cars"
        self._joker = True
        # Graphics configuration
        # the weathering is baked in to the sprite on these so no weathered remap
        weathered_variants = {
            "unweathered": graphics_constants.chemical_covered_hopper_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class MineralCoveredHopperCarSalt(MineralCoveredHopperCarSaltBase):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    model_type_id_stem = "salt_covered_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarSaltSwingRoof(MineralCoveredHopperCarSaltBase):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    model_type_id_stem = "salt_swing_roof_hopper_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MineralCoveredHopperCarSaltRandomised(
    RandomisedCarMixin, MineralCoveredHopperCarSaltBase
):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    model_type_id_stem = "salt_covered_hopper_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # clear from randomisation groups
        self.randomised_candidate_groups = []
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class OpenCarBase(CarModelTypeBase):
    """
    General cargo - refits everything except mail, pax.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["all_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self.randomised_candidate_groups = [
            "open_car_randomised",
            "piece_goods_car_mixed_randomised",
        ]


class OpenCar(OpenCarBase):
    """
    Standard open car
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    model_type_id_stem = "open_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_open_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, piece="open", liveries=self.liveries
        )


class OpenCarHood(OpenCarBase):
    """
    Open car with a hood when fully loaded
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    model_type_id_stem = "hood_open_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = ["KAOL"]
        self.default_cargos.extend(polar_fox.constants.default_cargos["open"])
        self.randomised_candidate_groups.extend(["piece_goods_car_covered_randomised"])
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_open_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.hood_open_car_body_recolour_map,
            "weathered": graphics_constants.hood_open_car_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            piece="open",
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            has_cover=True,
        )


class OpenCarHighEnd(OpenCarBase):
    """
    Open car with alternative livery
    """

    liveries = [
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    model_type_id_stem = "high_end_open_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_open_cars"
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.box_car_type_2_body_recolour_map,
            "weathered": graphics_constants.box_car_type_2_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True,
            piece="open",
            weathered_variants=weathered_variants,
            liveries=self.liveries,
        )


class OpenCarMill(OpenCarBase):
    """
    Open car for use in the steel industry, but widely repurposed and refittable.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    model_type_id_stem = "mill_open_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        self.randomised_candidate_groups = [
            "metal_product_car_mixed_randomised",
            "metal_product_car_uncovered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.box_car_type_2_body_recolour_map,
            "weathered": graphics_constants.box_car_type_2_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, piece="open", liveries=self.liveries
        )


class OpenCarRandomised(RandomisedCarMixin, OpenCarBase):
    """
    Random choice of open car sprite, from available open cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
    ]

    model_type_id_stem = "open_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_open_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class PassengerCarBase(CarModelTypeBase):
    """
    Common base class for passenger cars.
    """

    def __init__(self, **kwargs):
        # don't set model_type_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["pax"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
        self.use_colour_randomisation_strategies = False
        # roof configuration
        if self.gen in [1]:
            self.roof_type = "pax_mail_clerestory"
        elif self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["default"]

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]

    @property
    def joker_by_subclass_rules(self):
        # special-case handling for simplified mode with narrow gauge pax cars
        if self.base_track_type_name == "NG":
            if self.subtype in ["A", "B"]:
                return False
            else:
                return True
        # return None if there are no special rules, then the default rules will be applied by the calling function
        return None


class PassengeRailcarTrailerCarBase(PassengerCarBase):
    """
    Common base class for railcar trailer cars.
    """

    def __init__(self, **kwargs):
        # don't set model_type_id here, let subclasses do it
        super().__init__(**kwargs)
        self._buyable_variant_group_id = self.cab_id
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        self.suppress_pantograph_if_no_engine_attached = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self._str_name_suffix = "STR_NAME_SUFFIX_TRAILER"
        self._joker = True
        # faff to avoid pickle failures due to roster lookups when using multiprocessing in graphics pipeline
        self._frozen_pantograph_type = self.cab_consist.pantograph_type

    @property
    def subrole(self):
        return self.cab_consist.subrole

    @property
    def cab_id(self):
        # cab_id is required, must be set in model_def
        return self.model_def.cab_id

    @property
    def power_by_power_source(self):
        # necessary to ensure that pantograph provision can work, whilst not giving the vehicle any actual power
        return {key: 0 for key in self.cab_consist.power_by_power_source.keys()}

    @property
    def pantograph_type(self):
        return self._frozen_pantograph_type

    @property
    def intro_year_offset(self):
        # get the intro year offset and life props from the cab, to ensure they're in sync
        return self.cab_consist.intro_year_offset

    def get_name_parts(self, context):
        # special name handling to use the cab name
        result = [
            "STR_NAME_" + self.cab_id.upper(),
            self._str_name_suffix,
        ]
        return result

    @property
    def vehicle_family_badge(self):
        return "vehicle_family/" + self._buyable_variant_group_id


class PanoramicCar(PassengerCarBase):
    """
    Panoramic car / observation car / dome car.
    No special effects, just an explicitly buildable visual variant of standard passenger car.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    model_type_id_stem = "panoramic_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        """
        # not working as expected, unwanted nesting of panoramic car, needs debugged
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_passenger_cars"
        """
        # buy costs and run costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.4
        self.floating_run_cost_multiplier = 3.33
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        # Graphics configuration
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        return "express"


class PassengerCar(PassengerCarBase):
    """
    Standard passenger car.
    Default decay rate, capacities within reasonable distance of original base set pax coaches.
    Position-dependent sprites for brake car etc.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    model_type_id_stem = "passenger_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        """
        # not working as expected, unwanted nesting of panoramic car, needs debugged
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_passenger_cars"
        """
        # buy costs and run costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.4
        self.floating_run_cost_multiplier = 3.33
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special coaches from PassengerCar Feb 2021, as Restaurant cars were added
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        # pony NG jank directly set role buy menu string here, handles pony gen 4 NG speed bump
        if self.base_track_type_name == "NG" and self.gen < 4:
            return "universal"
        else:
            return "express"


class PassengerHighSpeedCar(PassengerCarBase):
    """
    High speed (LGV capable) variant of passenger car.
    Default decay rate, capacities within reasonable distance of original base set pax coaches.
    Position-dependent sprites for brake car etc.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    model_type_id_stem = "high_speed_passenger_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # buy costs and run costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.9
        self.floating_run_cost_multiplier = 4
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=liveries,
        )

    @property
    def subrole(self):
        return "very_high_speed"

    @property
    def lgv_capable(self):
        return True


class PassengerExpressRailcarTrailerCar(PassengeRailcarTrailerCarBase):
    """
    Unpowered passenger trailer car for express railcars.
    Position-dependent sprites for cabs etc.
    """

    model_type_id_stem = "express_railcar_passenger_trailer_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_non_core"
        ]
        self._joker = True
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.66 if self.base_track_type_name == "NG" else 1.5
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_6_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerHSTCar(PassengerCarBase):
    """
    Trailer dedicated for HST-type trains (no wagon attach, but matching stats and livery).
    Moderately improved decay rate compared to standard pax car.
    Position-dependent sprites for buffet car, brake car etc.
    """

    model_type_id_stem = "hst_passenger_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "hst"
        # used to get insert the name of the parent into vehicle name
        self._buyable_variant_group_id = self.cab_id
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.buy_cost_adjustment_factor = 1.66
        # run cost multiplier matches standard pax coach costs; higher speed is accounted for automatically already
        self.floating_run_cost_multiplier = 3.33
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type_name == "NG" else 1.6
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * special (buffet) coach
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=self.cab_consist.gestalt_graphics.liveries,
        )

    @property
    def subrole(self):
        return self.cab_consist.subrole

    @property
    def cab_id(self):
        # cab_id is required, must be set in model_def
        return self.model_def.cab_id

    @property
    def intro_year_offset(self):
        # get the intro year offset and life props from the cab, to ensure they're in sync
        return self.cab_consist.intro_year_offset

    def get_name_parts(self, context):
        # special name handling to use the cab name
        result = [
            "STR_NAME_" + self.cab_id.upper(),
            "STR_NAME_SUFFIX_HST_PASSENGER_CAR",
        ]
        return result

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerRailbusTrailerCar(PassengeRailcarTrailerCarBase):
    """
    Unpowered passenger trailer car for railbus (not railcar).
    Position-dependent sprites for cabs etc.
    """

    model_type_id_stem = "railbus_passenger_trailer_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.base_track_type_name == "NG" and self.gen == 4:
            # pony NG jank, gen 4 railbus trailers get a speed bump to 'express'
            self.speed_class = "express"
        else:
            # PassengerCarBase sets 'express' speed, but railbus trailers should override this
            self.speed_class = "standard"
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "suburban_or_universal_railcar"
        ]
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # ruleset will combine these to make multiple-units 1, 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_3_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerRailcarTrailerCar(PassengeRailcarTrailerCarBase):
    """
    Unpowered high-capacity passenger trailer car for railcars (not railbus).
    Position-dependent sprites for cabs etc.
    """

    model_type_id_stem = "railcar_passenger_trailer_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # PassengerCarBase sets 'express' speed, but railcar trailers should override this
        self.speed_class = "suburban"
        self.buy_cost_adjustment_factor = 2.1
        self.floating_run_cost_multiplier = 4.75
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "suburban_or_universal_railcar"
        ]
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        # for railcar trailers, the capacity is doubled, so halve the weight factor, this could have been automated with some constants etc but eh, TMWFTLB
        self.weight_factor = 0.33 if self.base_track_type_name == "NG" else 1
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        # * special unit with no cabs (center car)
        # ruleset will combine these to make multiple-units 1, 2, or 3 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="railcars_3_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["high_capacity"]

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerRestaurantCar(PassengerCarBase):
    """
    Special pax coach that modifies run costs and decay rates for other pax coaches in the consist.
    """

    model_type_id_stem = "restaurant_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # flag pax car ruleset behaviour
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.buy_cost_adjustment_factor = 2.5
        # double the luxury pax car amount; balance between the bonus amount (which scales with num. pax coaches) and the run cost of running this booster
        self.floating_run_cost_multiplier = 12
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        self._joker = True
        # Graphics configuration
        # position based variants are not used for restaurant cars, but they use the pax ruleset and sprite compositor for convenience
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 0, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "default_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=liveries,
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["restaurant"]

    @property
    def subrole(self):
        return "restaurant_car"


class PassengerSuburbanCar(PassengerCarBase):
    """
    Suburban pax car.
    Position-dependent sprites for brake car etc.
    """

    model_type_id_stem = "suburban_passenger_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # PassengerCarBase sets 'express' speed, but suburban coaches should override this
        # note that setting the speed lower doesn't actually balance profitability vs. standard pax coaches, but it gives a possibly comforting delusion about roles of each type
        self.speed_class = "suburban"
        # buy costs are levelled for standard and lux pax cars, not an interesting factor for variation
        self.buy_cost_adjustment_factor = 1.4
        # give it a run cost nerf due to the very high capacity
        self.floating_run_cost_multiplier = 4.75
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        # for suburban cars, the capacity is doubled, so halve the weight factor, this could have been automated with some constants etc but eh, TMWFTLB
        self.weight_factor = 0.33 if self.base_track_type_name == "NG" else 1
        self._joker = True
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special coaches from PassengerCarBase Dec 2018, overkill
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries(
            "suburban_pax_liveries", self.model_def
        )
        self.gestalt_graphics = GestaltGraphicsFormationDependent(
            spriterow_group_mappings,
            formation_ruleset="pax_cars",
            liveries=liveries,
        )

    @property
    def pax_car_capacity_type(self):
        return self.roster.pax_car_capacity_types["high_capacity"]

    @property
    def subrole(self):
        return "pax_suburban_coach"


class PeatCar(CarModelTypeBase):
    """
    Specialist transporter (narrow gauge bin) for peat
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "peat_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        # limited refits by design eh
        self.label_refits_allowed = ["PEAT"]
        self.label_refits_disallowed = []
        self.default_cargos = ["PEAT"]
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        # there will unused vehicles sprites for cargo states, but it's ok in this limited case
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, weathered_variants=weathered_variants, liveries=self.liveries
        )


class PieceGoodsCarRandomisedBase(RandomisedCarMixin, CarModelTypeBase):
    """
    Base class for randomised general (piece goods) cargo wagon.
    Refits match box vans, this is a compromise and means some cargos won't match e.g. non-randomised plate wagons or opens.
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
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_piece_goods_cars_randomised"
        self._joker = True


class PieceGoodsCarCoveredRandomised(PieceGoodsCarRandomisedBase):
    """
    Randomised (piece goods) cargo wagon, using covered sprites - mostly vans.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "piece_goods_car_covered_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=self.liveries,
        )


class PieceGoodsCarMixedRandomised(PieceGoodsCarRandomisedBase):
    """
    Randomised general (piece goods) cargo wagon.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "piece_goods_car_mixed_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=self.liveries,
        )


class PieceGoodsCarManufacturingPartsRandomised(PieceGoodsCarRandomisedBase):
    """
    Randomised general (piece goods) cargo wagon - using vehicles suitable for auto parts and similar manufacturing cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
    ]

    model_type_id_stem = "piece_goods_car_manufacturing_parts_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_segmented_block_train",
            dice_colour=1,
            liveries=self.liveries,
        )


class PipeCar(FlatCarBase):
    """
    Pipe wagon with fixed stakes & cradles, reusable for tube and other long products.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
    ]

    model_type_id_stem = "pipe_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["flat"]
        self.randomised_candidate_groups = []
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.box_car_type_2_body_recolour_map,
            "weathered": graphics_constants.box_car_type_2_body_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat", liveries=self.liveries
        )


class ReeferCarBase(CarModelTypeBase):
    """
    Refrigerated cargos.
    No actual cargo aging change - doesn't really work - so trade higher speed against lower capacity instead.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["refrigerated_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["reefer"]
        self.randomised_candidate_groups = [
            "reefer_car_randomised",
            "express_food_car_randomised",
        ]
        self.buy_cost_adjustment_factor = 1.33
        self.floating_run_cost_multiplier = 1.5
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "food_wagons"
        ]
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.refrigerated_livery_recolour_map,
            "weathered": graphics_constants.refrigerated_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsBoxCarOpeningDoors(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class ReeferCarType1(ReeferCarBase):
    """
    Standard reefer car.
    """

    model_type_id_stem = "reefer_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_reefer_cars"


class ReeferCarType2(ReeferCarBase):
    """
    Alternative reefer car style.
    """

    model_type_id_stem = "reefer_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_reefer_cars"
        self._joker = True


class ReeferCarRandomised(RandomisedCarMixin, ReeferCarBase):
    """
    Random choice of reefer car sprite.
    """

    model_type_id_stem = "reefer_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_reefer_cars"
        # Graphics configuration
        self.roof_type = "freight"
        weathered_variants = {
            "unweathered": graphics_constants.refrigerated_livery_recolour_map,
            "weathered": graphics_constants.refrigerated_livery_recolour_map_weathered,
        }
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class SiloCarBase(CarModelTypeBase):
    """
    Powder bulk cargos needing protection and special equipment for unloading.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_VIOLET"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_VIOLET"],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_refit_groups = ["silo_powders"]
        # labels are for legacy support, prior to CC_GAS class; this left in place as of Oct 2024
        # move to Polar Fox (maybe??)
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
        ]
        self.label_refits_disallowed = []
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.v_barrel_silo_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class SiloCarType1(SiloCarBase):
    """
    Standard silo car.
    """

    model_type_id_stem = "silo_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarType2(SiloCarBase):
    """
    Silo car with V-shaped barrel.
    """

    model_type_id_stem = "silo_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarType3(SiloCarBase):
    """
    Silo car with V-shaped barrel.
    """

    model_type_id_stem = "silo_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarRandomised(RandomisedCarMixin, SiloCarBase):
    """
    Random choice of silo car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_VIOLET"
        ],
    ]

    model_type_id_stem = "silo_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=self.liveries,
        )


class SiloCarCementType1(SiloCarBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "cement_silo_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_cement"]
        self.randomised_candidate_groups = ["cement_silo_car_randomised"]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_cement_silo_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.cement_silo_livery_recolour_map,
            "weathered": graphics_constants.cement_silo_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class SiloCarCementType2(SiloCarBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "cement_silo_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_cement"]
        self.randomised_candidate_groups = ["cement_silo_car_randomised"]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_cement_silo_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.cement_silo_livery_recolour_map,
            "weathered": graphics_constants.cement_silo_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class SiloCarCementType3(SiloCarBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "cement_silo_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_cement"]
        self.randomised_candidate_groups = ["cement_silo_car_randomised"]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_cement_silo_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.cement_silo_livery_recolour_map,
            "weathered": graphics_constants.cement_silo_livery_recolour_map_weathered,
        }
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class SiloCarCementRandomised(RandomisedCarMixin, SiloCarBase):
    """
    Random choice of cement silo car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    model_type_id_stem = "cement_silo_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_cement"]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_cement_silo_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=self.liveries,
        )


class SlidingRoofCar(BoxCarBase):
    """
    Sliding roof flat - sfins2 holdall and similar - same refits as box van.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    model_type_id_stem = "sliding_roof_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "metal_product_car_covered_randomised",
            "metal_product_car_mixed_randomised",
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.sliding_roof_car_body_recolour_map,
            "weathered": graphics_constants.sliding_roof_car_body_recolour_map_weathered,
        }
        # these make little difference visually for this wagon, but are needed to make this wagon a candidate for relevant randomised wagons
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            piece="flat",
            has_cover=True,
        )


class SlidingRoofCarHiCube(BoxCarBase):
    """
    Sliding roof high volume wagon - rover KSA cube and similar - same refits as box van.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
    ]

    model_type_id_stem = "sliding_roof_hi_cube_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # minor abuse of existing list
        self.default_cargos = polar_fox.constants.default_cargos["box_vehicle_parts"]
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "piece_goods_car_manufacturing_parts_randomised"
        ]
        self._joker = True
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        # teal before pewter to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            weathered_variants=weathered_variants,
            liveries=self.liveries,
            piece="flat",
            has_cover=True,
        )


class SlagLadleCarUnit(CarModelTypeBase):
    """
    Dedicated car for iron / steel slag.  No other refits.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "slag_ladle_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # none needed
        self.class_refit_groups = []
        self.label_refits_allowed = ["SLAG"]
        # none needed
        self.label_refits_disallowed = []
        self.default_cargos = ["SLAG"]
        self._loading_speed_multiplier = 2
        self.buy_cost_adjustment_factor = 1.2
        # double the default weight
        self.weight_factor = 2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self._joker = True
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt due to non-standard load sprites, which are hand coloured, not generated
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_with_visible_cargo.pynml",
            liveries=self.liveries,
            cargo_row_map={"SLAG": [0]},
            generic_rows=[0],
            unique_spritesets=[
                ["empty_unweathered", 10],
                ["loading_0", 40],
                ["loaded_0", 70],
            ],
        )


class TankCarBase(CarModelTypeBase):
    """
    All non-edible liquid cargos
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        # they may also change livery at stations if refitted between certain cargo types <shrug>
        super().__init__(**kwargs)
        self.class_refit_groups = ["liquids_non_food_grade"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_generic_liquids"
        ]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]


class TankCarAcidBase(TankCarBase):
    """
    Base class for acid visual variant of the standard tank car, same refits, different default cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SULPHUR_OCHRE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_SULPHUR"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["product_tank"]
        self.randomised_candidate_groups = [
            "acid_tank_car_randomised",
            "chemical_tank_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_acid_tank_cars"
        self._joker = True
        # Graphics configuration
        # empty, set in subclasses
        weathered_variants = {}
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # # teal before pewter for buy menu appearance reasons
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class TankCarAcidType1(TankCarAcidBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    model_type_id_stem = "acid_tank_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.acid_tank_car_type_1_livery_recolour_map,
            "weathered": graphics_constants.acid_tank_car_type_1_livery_recolour_map_weathered,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarAcidType2(TankCarAcidBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    model_type_id_stem = "acid_tank_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.acid_tank_car_type_2_livery_recolour_map,
            "weathered": graphics_constants.acid_tank_car_type_2_livery_recolour_map_weathered,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarAcidRandomised(RandomisedCarMixin, TankCarAcidBase):
    """
    Random choice of acid tank car sprites.
    """

    model_type_id_stem = "acid_tank_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarChemicalRandomised(RandomisedCarMixin, TankCarBase):
    """
    Random choice of tank car sprite, from available acid / product tank cars.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SULPHUR_OCHRE"
        ],
    ]

    model_type_id_stem = "chemical_tank_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=self.liveries,
        )


class TankCarProductBase(TankCarBase):
    """
    Tank car with more visible ribs etc than standard tank car, for chemicals, specialist cargos etc.
    Same refits as standard tank car, just a visual variant.
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_GREY_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SILVER_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SULPHUR_OCHRE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_SULPHUR"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["product_tank"]
        self.randomised_candidate_groups = [
            "chemical_tank_car_randomised",
            "product_tank_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_product_tank_cars"
        self._joker = True
        # Graphics configuration
        # set in variant subclasses
        weathered_variants = {}
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # # teal before pewter for buy menu appearance reasons
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class TankCarProductType1(TankCarProductBase):
    """
    Tank car with more visible ribs etc than standard tank car, for chemicals, specialist cargos etc.
    Same refits as standard tank car, just a visual variant.
    """

    model_type_id_stem = "product_tank_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.body_recolour_CC1,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarProductType2(TankCarProductBase):
    """
    Tank car with more visible ribs etc than standard tank car, for chemicals, specialist cargos etc.
    Same refits as standard tank car, just a visual variant.
    """

    model_type_id_stem = "product_tank_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.body_recolour_CC1,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarProductRandomised(RandomisedCarMixin, TankCarProductBase):
    """
    Random choice of product tank car.
    """

    model_type_id_stem = "product_tank_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarStandardBase(TankCarBase):
    """
    Standard tank car
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_SULPHUR_OCHRE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
        global_constants.freight_wagon_liveries["FREIGHT_SULPHUR"],
        global_constants.freight_wagon_liveries["FREIGHT_OCHRE"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["tank"]
        self.randomised_candidate_groups = ["tank_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_tank_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.tank_car_livery_recolour_map
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter for buy menu appearance reasons
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class TankCarStandardType1(TankCarStandardBase):
    """
    Standard tank car
    """

    model_type_id_stem = "tank_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TankCarStandardType2(TankCarStandardBase):
    """
    Standard tank car
    """

    model_type_id_stem = "tank_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TankCarStandardType3(TankCarStandardBase):
    """
    Standard tank car
    """

    model_type_id_stem = "tank_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TankCarStandardRandomised(RandomisedCarMixin, TankCarStandardBase):
    """
    Random choice of acid tank car sprites.
    """

    model_type_id_stem = "tank_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarVolatilesBase(TankCarBase):
    """
    Tank car with reflective silver or white finish (for low-flashpoint / volative liquids such as petrol).
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RED_RUBY"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RED"],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["tank"]
        """
        self.randomised_candidate_groups = [
            "volatives_tank_car_randomised",
        ]
        """
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_volatiles_tank_cars"
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.silver_grey_tank_car_livery_recolour_map,
            "weathered": graphics_constants.silver_grey_tank_car_livery_recolour_map_weathered,
        }
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsSimpleBodyColourRemaps(
            weathered_variants=weathered_variants, liveries=self.liveries
        )


class TankCarVolatilesType1(TankCarVolatilesBase):
    """
    Tank car with reflective silver or white finish (for low-flashpoint / volative liquids such as petrol).
    """

    model_type_id_stem = "volatiles_tank_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TarpaulinCarBase(BoxCarBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_PEWTER"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_OIL_BLACK"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
        global_constants.freight_wagon_liveries["FREIGHT_SILVER"],
        global_constants.freight_wagon_liveries["FREIGHT_PEWTER"],
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buy_cost_adjustment_factor = 1.1
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "non_core_wagons"
        ]
        self.randomised_candidate_groups = [
            "metal_product_car_covered_randomised",
            "metal_product_car_mixed_randomised",
            "piece_goods_car_covered_randomised",
            "piece_goods_car_mixed_randomised",
            "tarpaulin_car_randomised",
        ]
        self._joker = True
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_tarpaulin_cars"
        # Graphics configuration
        weathered_variants = {"unweathered": graphics_constants.body_recolour_CC1}
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        # teal before pewter and nightshade to ensure it appears in buy menu order for mixed version
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat",
            has_cover=True,
            weathered_variants=weathered_variants,
            liveries=self.liveries,
        )


class TarpaulinCarType1(TarpaulinCarBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    model_type_id_stem = "tarpaulin_car_type_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TarpaulinCarType2(TarpaulinCarBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    model_type_id_stem = "tarpaulin_car_type_2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TarpaulinCarType3(TarpaulinCarBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_RUBY"],
        global_constants.freight_wagon_liveries["FREIGHT_TEAL"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "tarpaulin_car_type_3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        # slightly fewer liveries than TarpaulinCarBase
        weathered_variants = {
            "unweathered": graphics_constants.tarpaulin_car_body_recolour_maps,
            "weathered": graphics_constants.tarpaulin_car_body_recolour_maps_weathered,
        }
        # we use TEAL_NIGHTSHADE here not TEAL_PEWTER to improve contrast, as the wagon hood is white
        # reduced set of liveries here
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            piece="flat",
            has_cover=True,
            weathered_variants=weathered_variants,
            liveries=self.liveries,
        )


class TarpaulinCarRandomised(RandomisedCarMixin, TarpaulinCarBase):
    """
    Random choice of tarpaulin car sprite
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        # we use TEAL_NIGHTSHADE here not TEAL_PEWTER to improve contrast when the wagon hood is white
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_RUBY_BAUXITE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_OIL_BLACK_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_TEAL_NIGHTSHADE"
        ],
    ]

    model_type_id_stem = "tarpaulin_car_randomised"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=self.liveries,
        )


class TorpedoCarUnit(CarModelTypeBase):
    """
    Specialist wagon for hauling molten pig iron.
    May or may not extend to other metal cargos (probably not).
    """

    liveries = [
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_COMPLEMENT_COMPANY_COLOUR"
        ],
        global_constants.freight_wagon_liveries[
            "RANDOM_FROM_CONSIST_LIVERIES_BAUXITE_GREY_NIGHTSHADE"
        ],
        global_constants.freight_wagon_liveries["RANDOM_FROM_CONSIST_LIVERIES_VARIETY"],
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING"
        ],
        global_constants.freight_wagon_liveries["FREIGHT_BAUXITE"],
        global_constants.freight_wagon_liveries["FREIGHT_GREY"],
        global_constants.freight_wagon_liveries["FREIGHT_NIGHTSHADE"],
    ]

    model_type_id_stem = "torpedo_car"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no classes, use explicit labels
        self.class_refit_groups = []
        self.label_refits_allowed = ["IRON"]
        self.label_refits_disallowed = []
        self.default_cargos = ["IRON"]
        self._loading_speed_multiplier = 1.5
        self.buy_cost_adjustment_factor = 1.2
        self.floating_run_cost_multiplier = 1.33
        # double the default weight
        self.weight_factor = 2
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]
        self._joker = True
        self.suppress_animated_pixel_warnings = True
        # Graphics configuration
        # custom gestalt with dedicated template as these wagons are articulated which standard wagon templates don't support
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_torpedo_car.pynml", liveries=self.liveries
        )


class BuyableVariant(object):
    """
    Simple class to hold buyable variants of the consist.
    """

    def __init__(self, consist, livery):
        self.consist = consist
        # option to point this livery to a specific row in the spritesheet, relative to the block of livery spriterows for the specific unit or similar
        # this is just for convenience if spritesheets are a chore to re-order
        self._relative_spriterow_num = livery.get("relative_spriterow_num", None)
        # possibly we don't need to store the livery, as we could look it up from the gestalt, but eh
        self.livery = livery

    @property
    def buyable_variant_num(self):
        # convenience method
        return self.consist.buyable_variants.index(self)

    @property
    def relative_spriterow_num(self):
        # either
        # (1) match to variant number (index in variants array), in which case the order in the spritesheet must match what is expected
        # (2) or can be forced manually to allow the spritesheet to be out of order (for convenience, or legacy support or any other reason)
        if self._relative_spriterow_num == None:
            return self.buyable_variant_num
        else:
            return self._relative_spriterow_num

    @property
    def lead_unit_variant_matching_buyable_variant(self):
        # convenience function
        for unit_variant in self.consist.units[0].unit_variants:
            if unit_variant.buyable_variant == self:
                return unit_variant
        # if not found, fail
        raise BaseException(
            "unit_variant not found for " + self + " for consist " + self.consist.id
        )

    @property
    def uses_random_livery(self):
        colour_set = self.livery.get("colour_set", None)
        if colour_set is not None:
            return colour_set.find("random_from_consist_liveries") != -1
        # fall through to default
        return False

    @property
    def is_default_buyable_variant_for_consist(self):
        # convenience method
        if self.buyable_variant_num == 0:
            return True
        else:
            return False

    @property
    def use_named_buyable_variant_group(self):
        # convenience pass through
        return self.consist.use_named_buyable_variant_group

    def get_variant_group_parent_vehicle_id(self):
        # we can't set variant group for a vehicle that is intended to be the ultimate parent of a group tree
        # this function is just a wrapper to handle returning that to nml templates
        # we still want to be able to get the variant group when needed without this check so this is handled separately
        if (
            self.buyable_variant_group.parent_vehicle.id
            == self.lead_unit_variant_matching_buyable_variant.id
        ):
            # handle nested group case, which is only used on first unit
            if self.buyable_variant_group.parent_group is None:
                return None
            else:
                return self.buyable_variant_group.parent_group.parent_vehicle.id
        else:
            return self.buyable_variant_group.parent_vehicle.id

    @property
    def buyable_variant_group(self):
        self.consist.assert_buyable_variant_groups()
        variant_group = self.consist.roster.buyable_variant_groups[
            self.buyable_variant_group_id
        ]
        return variant_group

    def compose_variant_group_id(self, group_name, consist, fixed_mixed_suffix):
        # composes a group id from a group name, and some properties from the consist
        return "{a}_{b}_gen_{c}{d}_{e}".format(
            a=group_name,
            b=consist.base_track_type_name.lower(),
            c=consist.gen,
            d=consist.subtype,
            e=fixed_mixed_suffix,
        )

    @property
    def buyable_variant_group_id(self):
        self.consist.assert_buyable_variant_groups()
        if self.consist._buyable_variant_group_id is not None:
            # explicitly defined group id
            id = self.consist._buyable_variant_group_id
        elif self.consist.group_as_wagon:
            if self.consist.use_named_buyable_variant_group is not None:
                group_id_base = self.consist.use_named_buyable_variant_group
            else:
                group_id_base = self.consist.id
            if not self.uses_random_livery:
                # we nest buyable variants with fixed colours into sub-groups
                fixed_mixed_suffix = "fixed"
            else:
                # everything else goes into one group, either on the consist group, or a named parent group which composes multiple model variants
                fixed_mixed_suffix = None
            id = self.compose_variant_group_id(
                group_id_base, self.consist, fixed_mixed_suffix
            )
        else:
            # assume group is composed from self (for simple case of variant liveries etc)
            id = self.consist.id
        return id


class UnitVariant(object):
    """
    Simple class for unit variants.
    Model variants have buyable_variants, and each unit of the consist needs a corresponding unit_variant.
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
            and self.buyable_variant.is_default_buyable_variant_for_consist
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
    def intro_year(self):
        return self.unit.consist.intro_year

    @property
    def uses_random_livery(self):
        return self.buyable_variant.uses_random_livery

    @property
    def uses_buy_menu_additional_text(self):
        if self.unit.consist.power_by_power_source is not None:
            if len(self.unit.consist.power_by_power_source) > 1:
                return True
        if self.unit.consist.buy_menu_additional_text_hint_wagons_add_power:
            return True
        if self.uses_random_livery:
            return True
        return False

    def get_buy_menu_additional_text_format(self, vehicle):
        # keep the template logic simple, present strings for a switch/case tree
        # variable_power and wagons_add_power are mutually exclusive (asserted by engine_varies_power_by_power_source as of August 2019)
        if self.unit.consist.engine_varies_power_by_power_source(vehicle):
            # !! this combinatorial handling of power, lgv capable etc is a bad sign - we have the wrong kind of tree, as it's switch/case, not composeable / recursive
            # !!! we need a better tree, similar to get_name_parts
            if self.unit.consist.lgv_capable:
                return "variable_power_and_lgv_capable"
            else:
                return "variable_power"
        elif self.unit.consist.lgv_capable:
            # yeah, simplicity failed when lgv_capable was added, this simple tree needs rethought to allow better composition of arbitrary strings
            if self.unit.consist.buy_menu_additional_text_hint_wagons_add_power:
                return "lgv_capable_and_wagons_add_power"
            else:
                return "lgv_capable"
        elif self.uses_random_livery:
            return "livery_variants"
        else:
            return None

    @property
    def all_candidate_livery_colour_sets_for_variant(self):
        # this may be a real variant, or a randomised variant, which delegates out to a set of real variants
        # therefore we need to get the possible liveries across all possible variants
        unit_variants = []
        if self.unit.consist.is_randomised_wagon_type:
            for (
                unit_variant
            ) in self.unit.consist.roster.get_wagon_randomisation_candidates(
                self.buyable_variant
            ):
                unit_variants.append(unit_variant)
        else:
            # we will just use one variant in this case, but we put it in a list so we can iterate later to get liveries
            unit_variants.append(self)

        eligible_colours = global_constants.wagon_livery_mixes[
            self.buyable_variant.livery["colour_set"]
        ]
        variant_colour_set = []
        for unit_variant in unit_variants:
            for (
                candidate_livery
            ) in unit_variant.unit.consist.gestalt_graphics.all_liveries:
                if candidate_livery["colour_set"] not in variant_colour_set:
                    if candidate_livery["colour_set"] in eligible_colours:
                        variant_colour_set.append(candidate_livery["colour_set"])

        if len(variant_colour_set) == 0:
            raise BaseException(
                self.id
                + " has variant_colour_set length 0, which won't work - check what livery colour_set it's using"
            )

        return variant_colour_set

    def get_buy_menu_hint_livery_variant_text_stack(self):
        variant_colour_set = self.all_candidate_livery_colour_sets_for_variant

        stack_values = []
        stack_values.append(
            "string(STR_BUY_MENU_ADDITIONAL_TEXT_HINT_LIVERY_VARIANTS_LENGTH_"
            + str(len(variant_colour_set))
            + ")"
        )

        # note the OR with 0xD000 to get correct string range
        for colour_name in variant_colour_set:
            if colour_name == "company_colour":
                stack_values.append("string(STR_COMPANY_COLOUR_CABBAGE) | 0xD000")
            elif colour_name == "complement_company_colour":
                stack_values.append("string(STR_COMPANY_COLOUR_CABBAGE) | 0xD000")
            else:
                stack_values.append(
                    "switch_get_colour_name("
                    + str(list(global_constants.colour_sets.keys()).index(colour_name))
                    + ") | 0xD000"
                )
        return utils.convert_flat_list_to_pairs_of_tuples(stack_values)

    def get_wagon_recolour_strategy_params(self, context=None):
        wagon_recolour_strategy_num = self.unit.consist.get_wagon_recolour_strategy_num(
            self.buyable_variant.livery
        )

        if self.uses_random_livery:
            available_liveries = (
                self.unit.consist.get_candidate_liveries_for_randomised_strategy(
                    self.buyable_variant.livery
                )
            )
            if self.buyable_variant.livery.get("purchase", None) is not None:
                wagon_recolour_strategy_num_purchase = (
                    self.unit.consist.get_wagon_recolour_strategy_num(
                        self.buyable_variant.livery, context="purchase"
                    )
                )
            else:
                wagon_recolour_strategy_num_purchase = available_liveries[0]
        else:
            # we have to provide 8 options for nml params, but in this case they are all unused, so just pass them as 0
            available_liveries = [0, 0, 0, 0, 0, 0, 0, 0]
            # purchase strategy will be same as non-purchase
            wagon_recolour_strategy_num_purchase = wagon_recolour_strategy_num

        flag_use_weathering = self.buyable_variant.livery.get("use_weathering", False)
        flag_context_is_purchase = True if context == "purchase" else False

        params_numeric = [
            flag_use_weathering,
            flag_context_is_purchase,
            wagon_recolour_strategy_num,
            wagon_recolour_strategy_num_purchase,
        ]

        params_numeric.extend(available_liveries)

        # int used to convert False|True bools to 0|1 values for nml
        return ", ".join(str(int(i)) for i in params_numeric)

    def get_wagon_recolour_colour_set_num(self, context=None):
        params = self.get_wagon_recolour_strategy_params(context)
        return self.unit.consist.roster.wagon_recolour_colour_sets.index(params)
