import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import copy
import math
import random
from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
class UnitDef:
    """Simple wrapper obj to unpack/default required kwargs (the rest are arbitrary)"""

    # CABBAGE DOCUMENT
    class_name: str
    repeat: int = 1
    capacity: Optional[int] = None
    weight: Optional[int] = None
    vehicle_length: Optional[int] = None
    spriterow_num: Optional[int] = 0
    chassis: Optional[str] = None
    effects: Optional[dict] = None
    effect_offsets: Optional[list] = None
    # z offset is rarely used and is handled separately, mostly just for low-height engines
    effect_z_offset: Optional[int] = None
    tail_light: Optional[str] = None
    suppress_roof_sprite: bool = False
    symmetry_type: Optional[str] = None
    # mostly vehicles figure out their own spriterows in output, but occasionaly we need explicit control
    force_spriterow_group_in_output_spritesheet: Optional[int] = 0
    # optional - we might want to force the sprites to reverse in some contexts, for example rear cabs of multiple-unit articulated railcars
    reverse_sprite_template: bool = False


class ModelDef(object):

    def __init__(self, class_name, **kwargs):
        self.class_name = class_name
        self.kwargs = kwargs
        self.unit_defs = []
        # used for clone book-keeping
        self.cloned_from_model_def = None
        self.clones = []
        # unpack some keywords
        self.gen = kwargs["gen"]

    def add_unit(self, **kwargs):
        self.unit_defs.append(UnitDef(**kwargs))

    def define_description(self, description):
        # note we store in kwargs, as the 'recipe' for the consist
        self.kwargs["description"] = description

    def define_foamer_facts(self, foamer_facts):
        # note we store in kwargs, as the 'recipe' for the consist
        self.kwargs["foamer_facts"] = foamer_facts

    def begin_clone(self, base_numeric_id, unit_repeats, **kwargs):
        if self.cloned_from_model_def is not None:
            # cloning clones isn't supported, it will cause issues resolving spritesheets etc, and makes it difficult to manage clone id suffixes
            raise Exception(
                "Don't clone a consist factory that is itself a clone, it won't work as expected. \nClone the original consist factory. \nConsist is: "
                + self.kwargs["id"]
            )
        cloned_model_def = copy.deepcopy(self)
        # cloned consist factory may need to reference original source
        cloned_model_def.cloned_from_model_def = self
        # keep a reference locally for book-keeping
        self.clones.append(cloned_model_def)
        # deepcopy will have created new unit factory instances, but we might want to modify the sequence for the cloned consist factory
        # the format is unit_repeats=[x, y z]
        # for each existing unit factory, this will specify which unit factories to copy, and what their repeat values are
        # e.g. [1, 0] will keep the first and drop the second
        # [2, 1] will repeat the first unit twice
        # [0, 2] will drop the first unit and repeat the second twice
        unit_defs_old = cloned_model_def.unit_defs.copy()
        cloned_model_def.unit_defs = []
        for counter, unit_def in enumerate(unit_defs_old):
            # don't use unit if repeat is 0
            if unit_repeats[counter] > 0:
                cloned_model_def.unit_defs.append(unit_def)
                unit_def.repeat = unit_repeats[counter]

        cloned_model_def.kwargs["base_numeric_id"] = base_numeric_id
        # this method of resolving id will probably fail with wagons, untested as of Feb 2025, not expected to work, deal with that later if needed
        cloned_model_def.kwargs["id"] = (
            self.kwargs["id"] + "_clone_" + str(len(self.clones))
        )
        cloned_model_def.kwargs["buyable_variant_group_id"] = self.kwargs["id"]
        return cloned_model_def

    def complete_clone(self):
        # book-keeping and adjustments after all changes are made to a cloned consist factory
        self.kwargs["power_by_power_source"] = self.clone_adjust_power_by_power_source()
        # purchase menu variant decor isn't supported if the consist is articulated, so just forcibly clear this property
        if self.produced_unit_total > 1:
            self.kwargs["show_decor_in_purchase_for_variants"] = []

    @property
    def clone_stats_adjustment_factor(self):
        # clones need to adjust some stats, e.g. power, running_cost etc, we do this by inferring a multiple by comparing number of units that will be produced
        # call on clone, not source, will except (correctly) if called on source
        try:
            source_unit_count = self.cloned_from_model_def.produced_unit_total
        except:
            raise Exception("source_unit_count failed" + str(self.kwargs))
        clone_unit_count = self.produced_unit_total
        result = clone_unit_count / source_unit_count
        return result

    def clone_adjust_power_by_power_source(self):
        # recalculate power in 'recipe' for a cloned consist factory
        result = {}
        for (
            power_type,
            power_value,
        ) in self.kwargs["power_by_power_source"].items():
            result[power_type] = int(power_value * self.clone_stats_adjustment_factor)
        return result

    @property
    def produced_unit_total(self):
        # convenience way to find out how many units in total this model def will produce
        return sum(unit_def.repeat for unit_def in self.unit_defs)


class ModelTypeFactory(object):
    """
    ModelTypeFactory instances:
    - hold a roster_id identifier
    - store a ModelDef object with vehicle-specific parameters
    - maintain a sequence of one or more UnitDef instances
    - include the set of available liveries for the vehicle model
    - for each livery, create a model variant (an instance of the ModelType subclass)
        - each model variant will appear in the in-game buy menu
    - attach to each model variant unique UnitType instances in the proper order
    - resulting in model_variant.units = [<UnitType>, <UnitType>]

    # examples
    - class_name = class SmallVan(ModelType)
    - model_type_id = "ford_transit"
        - model_variant = "ford_transit_blue"
            - model_variant.units = [<FreightRoadVehicleUnitType>]
        - model_variant = "ford_transit_red"
            - model_variant.units = [<FreightRoadVehicleUnitType>]

    - class_name = class Engine(ModelType)
    - model_type_id = "challenger"
        - model_variant = "challenger_grey"
            - model_variant.units = [<SteamEngineUnitType>, <SteamEngineTenderUnitType>]
        - model_variant = "challenger_black"
            - model_variant.units = [<SteamEngineUnitType>, <SteamEngineTenderUnitType>]
    """

    def __init__(self, model_def):
        self.class_name = model_def.class_name
        self.model_def = model_def
        # used for book-keeping related consists, does not define consists in roster
        self.produced_consists = []

    def set_roster_ids(self, roster_id, roster_id_providing_module):
        # rosters can optionally init consist factories from other rosters
        # store the roster that inited the consist factory, and the roster that the consist factory module is in the filesystem path for
        # we don't store the roster object directly as it can fail to pickle with multiprocessing
        self.roster_id = roster_id
        self.roster_id_providing_module = roster_id_providing_module

    def produce(self, livery=None, dry_run=False):
        if livery == None:
            # just do the default livery, this means that calling ModelTypeFactory.produce() without params will always just return a default consist, which is useful
            # ASSIGN LIVERY HERE
            pass

        consist_cls = getattr(sys.modules[__name__], self.class_name)
        consist = consist_cls(model_type_factory=self, **self.model_def.kwargs)

        """
        if hasattr(consist_cls, "liveries"):
            print(consist_cls, len(consist_cls.liveries))
        if self.kwargs.get("additional_liveries", None) != None:
            print(consist_cls, self.kwargs["additional_liveries"])
        """

        # orchestrate addition of units
        for unit_def in self.model_def.unit_defs:
            try:
                unit_cls = getattr(sys.modules[__name__], unit_def.class_name)
            except:
                raise Exception(
                    "class_name not found for "
                    + self.model_def.kwargs["id"]
                    + ", "
                    + unit_def.class_name
                )
            # CABBAGE - this is delegating to consist currently, by passing unit classes, we want to pass actual units from here, consist knows too much
            # print(unit_cls, unit)
            consist.add_unit(unit_cls, unit_def)

        if dry_run == False:
            self.produced_consists.append(consist)
        return consist

    def get_wagon_id(self, base_id, **kwargs):
        # auto id creator, used for wagons not locos
        # handled by consist factory not consist, better this way
        substrings = []
        # prepend cab_id if present, used for e.g. railcar trailers, HST coaches etc where the wagon matches a specific 'cab' engine
        if kwargs.get("cab_id", None) is not None:
            substrings.append(kwargs["cab_id"])
        # special case NG - extend this for other track_types as needed
        # 'normal' rail and 'elrail' doesn't require an id modifier
        if kwargs.get("base_track_type_name", None) == "NG":
            base_id = base_id + "_ng"
        if kwargs.get("base_track_type_name", None) == "METRO":
            base_id = base_id + "_metro"
        substrings.append(base_id)
        try:
            substrings.append(self.roster_id)
        except:
            raise Exception(base_id + str(kwargs))
        substrings.append("gen")
        substrings.append(str(kwargs["gen"]) + str(kwargs["subtype"]))
        result = "_".join(substrings)
        return result


class Consist(object):
    """
    'Vehicles' (appearing in buy menu) are composed as articulated consists.
    Each consist comprises one or more 'units' (visible).
    """

    def __init__(self, **kwargs):
        self.model_type_factory = kwargs[
            "model_type_factory"
        ]  # mandatory, fail if missing
        self.id = kwargs.get("id", None)
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        # private var, used to store a name substr for engines, composed into name with other strings as needed
        self._name = kwargs.get("name", None)
        self.base_numeric_id = kwargs.get("base_numeric_id", None)
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
        # either gen xor intro_year is required, don't set both, one will be interpolated from the other
        # CABBAGE model_def?
        self._intro_year = kwargs.get("intro_year", None)
        # override this in subclasses if needed, there's no case currently for setting it via keyword
        self._model_life = None
        # if gen is used, the calculated intro year can be adjusted with +ve or -ve offset
        # CABBAGE model_def?
        self.intro_year_offset = kwargs.get("intro_year_offset", None)
        # used for synchronising / desynchronising intro dates for groups vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147
        self._intro_year_days_offset = (
            None  # defined in subclasses, no need for instances to define this
        )
        # vehicle life uses a default value, but can be extended automatically via a bool keyword, or it can be set manually
        # CABBAGE model_def?
        self.extended_vehicle_life = kwargs.get("extended_vehicle_life", False)
        # CABBAGE model_def?
        self._vehicle_life = kwargs.get("vehicle_life", None)
        #  most consists are automatically replaced by the next consist in the subrole tree
        # ocasionally we need to merge two branches of the subrole, in this case set replacement consist id
        # CABBAGE model_def?
        self._replacement_consist_id = kwargs.get("replacement_consist_id", None)
        # default loading speed multiplier, override in subclasses as needed
        self._loading_speed_multiplier = 1
        # CABBAGE model_def?
        self.base_track_type_name = kwargs.get("base_track_type_name", "RAIL")
        # modify base_track_type_name for electric engines when writing out the actual rail type
        # without this, RAIL and ELRL have to be specially handled whenever a list of compatible consists is wanted
        # CABBAGE model_def?
        self.tractive_effort_coefficient = kwargs.get(
            "tractive_effort_coefficient", 0.3
        )  # 0.3 is recommended default value
        # private var, can be used to overrides default (per generation, per class) speed
        # CABBAGE model_def?
        self._speed = kwargs.get("speed", None)
        # used by multi-mode engines such as electro-diesel, otherwise ignored
        # CABBAGE model_def?
        self.power_by_power_source = kwargs.get("power_by_power_source", None)
        # some engines require pantograph sprites composited, don't bother setting this unless required
        # CABBAGE model_def?
        self.pantograph_type = kwargs.get("pantograph_type", None)
        # some consists don't show pans in the buy menu (usually unpowered)
        self.suppress_pantograph_if_no_engine_attached = False
        # some engines have an optional decor layer, which is a manual spriterow num (as decor might not be widely used?)
        # CABBAGE model_def?
        self.decor_spriterow_num = kwargs.get("decor_spriterow_num", None)
        # stupid extra-detail, control which variants show decor in purchase menu
        # CABBAGE model_def?
        self.show_decor_in_purchase_for_variants = kwargs.get(
            "show_decor_in_purchase_for_variants", []
        )
        # CABBAGE model_def?
        self.dual_headed = kwargs.get("dual_headed", False)
        # CABBAGE model_def?
        self.tilt_bonus = kwargs.get("tilt_bonus", False)
        # CABBAGE model_def?
        self.lgv_capable = kwargs.get("lgv_capable", False)
        # CABBAGE model_def?
        self.requires_high_clearance = kwargs.get("requires_high_clearance", False)
        # solely used for ottd livery (company colour) selection, set in subclass as needed
        self.train_flag_mu = False
        # some wagons will provide power if specific engine IDs are in the consist
        self.wagons_add_power = False
        self.buy_menu_additional_text_hint_wagons_add_power = False
        # structure to hold badges, add badges in subclass as needed
        self._badges = []
        # wagons can be candidates for the magic randomised wagons
        # this is on Consist not CarConsist as we need to check it when determining order for all consists
        self.randomised_candidate_groups = []
        # some vehicles will get a higher speed if hauled by an express engine (use rarely)
        # CABBAGE model_def?
        self.easter_egg_haulage_speed_bonus = kwargs.get(
            "easter_egg_haulage_speed_bonus", False
        )
        # option to force a specific name suffix, if the auto-detected ones aren't appropriate
        self._str_name_suffix = None
        # random_reverse means (1) randomised flip of vehicle when built (2) player can also flip vehicle manually
        # random_reverse is not supported in some templates
        # CABBAGE model_def?
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
        # subrole and branches
        # CABBAGE model_def?
        self.subrole = kwargs.get("subrole", None)
        # subrole child branch num places this vehicle on a specific child branch of the tech tree, where the subrole and role are the parent branches
        # 0 = null, no branch (for wagons etc)
        #  1..n for branches
        # -1..-n for jokers
        # CABBAGE model_def?
        self.subrole_child_branch_num = kwargs.get("subrole_child_branch_num", 0)
        # optionally suppress nmlc warnings about animated pixels for consists where they're intentional
        # CABBAGE model_def?
        self.suppress_animated_pixel_warnings = kwargs.get(
            "suppress_animated_pixel_warnings", False
        )
        # extended description (and a cite from a made up person) for docs etc
        self.description = """"""  # to be set per vehicle, multi-line supported
        self._cite = ""  # optional, set per subclass as needed
        # for 'inspired by' stuff
        self.foamer_facts = """"""  # to be set per vehicle, multi-line supported
        # 0 indexed spriterows, position in generated spritesheet, used by brake vans to get a docs image for 4th gen, not 1st
        # CABBAGE model_def?
        self.docs_image_spriterow = kwargs.get("docs_image_spriterow", None)
        # used for docs management
        self.is_wagon_for_docs = False
        # aids 'project management'
        # CABBAGE model_def?
        self.sprites_complete = kwargs.get("sprites_complete", False)
        # CABBAGE model_def?
        self.sprites_additional_liveries_potential = kwargs.get(
            "sprites_additional_liveries_potential", False
        )

    @property
    def model_def(self):
        # just a pass through for convenience
        return self.model_type_factory.model_def

    @property
    def roster_id(self):
        # just a pass through for convenience
        return self.model_type_factory.roster_id

    @property
    def roster_id_providing_module(self):
        # just a pass through for convenience
        return self.model_type_factory.roster_id_providing_module

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
    def role(self):
        # returns first matched, assumption is consists only have one valid subrole
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
    def gen(self):
        # just a passthrough for convenience
        return self.model_def.gen

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
        if self._speed:
            return self._speed
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
                    self.model_def.cloned_from_model_def.kwargs["id"]
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
        # required
        self.description = kwargs["description"]
        # required
        self.foamer_facts = kwargs["foamer_facts"]
        # arbitrary multiplier to floating run costs (factors are speed, power, weight)
        # adjust per subtype as needed
        self.floating_run_cost_multiplier = 8.5
        # fixed (baseline) run costs on this subtype, or more rarely instances can override this
        # CABBAGE model_def?
        self.fixed_run_cost_points = kwargs.get("fixed_run_cost_points", 180)
        # optionally force a specific caboose family to be used
        # CABBAGE model_def?
        self._caboose_family = kwargs.get("caboose_family", None)
        # how to handle grouping this consist type
        self.group_as_wagon = False
        # Graphics configuration only as required
        # (pantographs can also be generated by other gestalts as needed, this isn't the exclusive gestalt for it)
        # note that this Gestalt might get replaced by subclasses as needed
        # insert a default livery
        # CABBAGE FACTORY?
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
        # first check if this is a clone, because then we just take the costs from the clone source
        # and adjust them to account for differing number of units
        if self.model_def.cloned_from_model_def is not None:
            # we have to instantiate an actual consist, temporarily, as the factory doesn't know the calculated cost directly
            model_type_factory = ModelTypeFactory(self.model_def.cloned_from_model_def)
            model_type_factory.set_roster_ids(self.roster_id, self.roster_id_providing_module)
            temp_consist = model_type_factory.produce(dry_run=True)
            return int(
                temp_consist.buy_cost
                * self.model_def.clone_stats_adjustment_factor
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
    def running_cost(self):
        # algorithmic calculation of engine run costs
        # as of Feb 2019, it's fixed cost (set by subtype) + floating costs (derived from power, speed, weight)

        # first check if this is a clone, because then we just take the costs from the clone source
        # and adjust them to account for differing number of units
        if self.model_def.cloned_from_model_def is not None:
            # we have to instantiate an actual consist, temporarily, as the factory doesn't know the calculated cost directly
            model_type_factory = ModelTypeFactory(self.model_def.cloned_from_model_def)
            model_type_factory.set_roster_ids(self.roster_id, self.roster_id_providing_module)
            temp_consist = model_type_factory.produce(dry_run=True)
            return int(
                temp_consist.running_cost
                * self.model_def.clone_stats_adjustment_factor
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


class AutoCoachCombineConsist(EngineConsist):
    """
    Consist for an articulated auto coach combine (mail + pax).  Implemented as Engine so it can lead a consist in-game.
    To keep implementation simple + crude, first unit should be dedicated mail type, second unit should be dedicated pax type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subrole = "driving_cab_express_mixed"
        # driving cab cars are probably jokers?
        self.subrole_child_branch_num = -1
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types[
            "autocoach_combine"
        ]
        # confer tiny power value to make this one an engine so it can lead.
        # use 10 not 1, because 1 looks weird when added to engine HP
        self.power_by_power_source = {"NULL": 10}
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0
        # ....buy costs adjusted to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_buy_cost_points = 6
        # ....run costs nerfed down to match equivalent gen 2 + 3 pax / mail cars
        self.fixed_run_cost_points = 43
        # Graphics configuration
        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_autocoach.pynml",
            liveries=liveries,
        )

    @property
    def loading_speed_multiplier(self):
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class FixedFormationRailcarCombineConsist(EngineConsist):
    """
    Consist for a fixed formation articulated railcar combine (mail + pax).
    This *does* not use consist-dependent position sprite rulesets; the formation is fixed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types[
            kwargs["pax_car_capacity_type"]
        ]
        if self.base_track_type_name == "NG":
            # pony NG jank, to force a different role string for NG
            if self.gen == 4:
                self.subrole = "express"
            else:
                self.subrole = "universal"
        # Graphics configuration
        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_fixed_formation_railcar.pynml",
            liveries=self.roster.get_liveries_by_name([]),
        )

    @property
    def loading_speed_multiplier(self):
        # !!!!!!!!!!!!!!!
        return self.pax_car_capacity_type["loading_speed_multiplier"]


class MailEngineConsist(EngineConsist):
    """
    Consist of engines / units that has mail (and express freight) capacity
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
        # ...but reduce fixed (baseline) run costs on this subtype, purely for balancing reasons
        self.fixed_run_cost_points = 84


class MailEngineCabbageDVTConsist(MailEngineConsist):
    """
    Consist for a mail DVT / cabbage.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subrole = "driving_cab_express_mail"
        # report mail cab cars as pax cars for consist rulesets
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        self.power_by_power_source = {"NULL": 300}
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0.1
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("dvt_mail_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="driving_cab_cars",
            liveries=liveries,
        )


class MailEngineCargoSprinterEngineConsist(MailEngineConsist):
    """
    Consist for a cab motor unit for Cargo Sprinter express freight unit.
    """

    liveries = [global_constants.freight_wagon_liveries["COMPANY_COLOUR_NO_WEATHERING"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dual_headed = True
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
            cargo_label_mapping=GestaltGraphicsIntermodalContainerTransporters(
                liveries=self.liveries
            ).cargo_label_mapping,
            num_extra_layers_for_spritelayer_cargos=2,
            liveries=self.liveries,
        )

    @property
    def spritelayer_cargo_layers(self):
        # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
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
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("metro_mail_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="metro",
            liveries=liveries,
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
        if self.base_track_type_name == "NG" and self.gen == 4:
            # pony NG jank
            self.subrole = "express"
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
        # this will be fragile, it's dedicated to pony roster, but eh
        # for special cases, these vehicles could just use the livery keyword on init, but it would be over-ridden by this conditional block currently
        if self.subrole_child_branch_num in [2] or self.base_track_type_name == "NG":
            liveries = self.roster.get_pax_mail_liveries(
                "diesel_railcar_mail_liveries", **kwargs
            )
        else:
            liveries = self.roster.get_pax_mail_liveries(
                "electric_railcar_mail_liveries", **kwargs
            )
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset=consist_ruleset,
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name


class MailEngineExpressRailcarConsist(MailEngineConsist):
    """
    Consist for an express mail railcar (single unit, combinable).
    Intended for express-speed, high-power long-distance EMUs, use railbus or railcars for short / slow / commuter routes.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        # position variants
        # * unit with two cabs (will never be used if the specific consist is articulated)
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # * unit with no cabs (center car)
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        liveries = self.roster.get_pax_mail_liveries("default_mail_liveries", **kwargs)
        jfdi_pantograph_debug_image_y_offsets = [len(liveries) * 60, 30]
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_4_unit_sets",
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
        # specific structure for capacity multiplier and loading speed, override in subclasses as needed
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
        self.subrole = "driving_cab_express_pax"
        # report cab cars as pax cars for consist rulesets
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # confer a small power value for 'operational efficiency' (HEP load removed from engine eh?) :)
        self.power_by_power_source = {"NULL": 300}
        # nerf TE down to minimal value
        self.tractive_effort_coefficient = 0.1
        # ....buy costs reduced from base to make it close to mail cars
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration
        # driving cab cars have consist cargo mappings for pax, mail (freight uses mail)
        # * pax matches pax liveries for generation
        # * mail gets a TPO/RPO striped livery, and a 1CC/2CC duotone livery
        # position based variants
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="driving_cab_cars",
            liveries=liveries,
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
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self.buy_cost_adjustment_factor = 0.85
        if self.base_track_type_name == "NG":
            # special case to knock costs on NG versions of these down similar to other railcars
            self.fixed_run_cost_points = 120
            # cleanest way to compress run cost down sufficiently
            self.floating_run_cost_multiplier = 4
        else:
            # to avoid these railcars being super-bargain cheap, add a cost malus compared to standard railcars (still less than standard engines)
            self.fixed_run_cost_points = 155
        # non-standard cite
        self._cite = "Dr Constance Speed"
        # Graphics configuration
        if self.gen in [2, 3]:
            self.roof_type = "pax_mail_ridged"
        else:
            self.roof_type = "pax_mail_smooth"
        # position variants
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        jfdi_pantograph_debug_image_y_offsets = [len(liveries) * 60, 30]
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset=kwargs.get("consist_ruleset", "railcars_6_unit_sets"),
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
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 1, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("metro_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="metro",
            liveries=liveries,
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
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        # big cost bonus for railbus
        self.fixed_run_cost_points = 48
        # optional keyword override, intended for Combine type railbuses, otherwise just use the default for this class
        if "pax_car_capacity_type" in kwargs:
            self.pax_car_capacity_type = self.roster.pax_car_capacity_types[
                kwargs["pax_car_capacity_type"]
            ]
        if self.base_track_type_name == "NG":
            # pony NG jank
            if self.gen == 4:
                self.subrole = "express"
            else:
                self.subrole = "universal"
        # non-standard cite
        self._cite = "Arabella Unit"
        # Graphics configuration
        self.roof_type = "pax_mail_smooth"
        # position variants
        # * unit with driving cab front end
        # * unit with driving cab rear end
        # ruleset will combine these to make multiple-units 1, 2 vehicles long, then repeating the pattern
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 3}
        consist_ruleset = "railcars_3_unit_sets"
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset=consist_ruleset,
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def vehicle_family_badge(self):
        if self._buyable_variant_group_id is not None:
            family_name = self._buyable_variant_group_id
        else:
            family_name = self.id
        return "vehicle_family/" + family_name


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
                "suburban_pax_liveries", **kwargs
            )
        else:
            liveries = self.roster.get_pax_mail_liveries(
                "default_pax_liveries", **kwargs
            )
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_3_unit_sets",
            liveries=liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def vehicle_family_badge(self):
        return "vehicle_family/" + self.id


class SnowploughEngineConsist(EngineConsist):
    """
    Consist for a snowplough.  Implemented as Engine so it can lead a consist in-game.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # blame Pikka for the spelling eh? :)
        self.subrole = "snoughplough!"
        self.subrole_child_branch_num = -1
        # nerf power and TE down to minimal values, these confer a tiny performance boost to the train, 'operational efficiency' :P
        self.power_by_power_source = {"NULL": 100}
        self.tractive_effort_coefficient = 0.1
        # give it mail / express capacity so it has some purpose :P
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = ["TOUR"]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # to reduce it from engine factor
        self.fixed_buy_cost_points = 1
        self.buy_cost_adjustment_factor = 1
        # ....run costs reduced from base to make it close to mail cars
        self.fixed_run_cost_points = 68
        # Graphics configuration

        # inserts the default liveries for docs examples
        liveries = self.roster.get_liveries_by_name([])
        self.gestalt_graphics = GestaltGraphicsCustom(
            "vehicle_snowplough.pynml",
            liveries=liveries,
        )


class TGVCabEngineConsist(EngineConsist):
    """
    Consist for a TGV (very high speed) engine cab (leading motor unit)
    This has power by default and would usually be set as a dual-headed engine.
    Adding specific middle engines (with correct ID) will increase power for this engine.
    This does not have pax capacity, by design, to allow for TGV La Poste mail trains.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dual_headed = True
        self.buy_menu_additional_text_hint_wagons_add_power = True
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
    def buy_menu_additional_text_distributed_power_substring(self):
        return "STR_WAGONS_ADD_POWER_CAB"

    @property
    def buy_menu_distributed_power_name_substring(self):
        return "STR_NAME_" + self.id.upper()

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
        self._buyable_variant_group_id = self.cab_id
        self.wagons_add_power = True
        self.buy_menu_additional_text_hint_wagons_add_power = True
        self.tilt_bonus = True
        self.lgv_capable = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        # eh as of Feb 2019, OpenTTD won't actually use this for middle cars, as not engines
        # this means the buy menu won't match, but wagons will match anyway when attached to cab
        # prop left in place in case that ever gets changed :P
        # !! commented out as of July 2019 because the middle engines won't pick this up, which causes inconsistency in the buy menu
        # self.train_flag_mu = True
        # get the intro year offset and life props from the cab, to ensure they're in sync
        self.intro_year_offset = self.cab_consist.intro_year_offset
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="tgv",
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
    def vehicle_family_badge(self):
        return "vehicle_family/" + self._buyable_variant_group_id


class TGVMiddleMailEngineConsist(TGVMiddleEngineConsistMixin, MailEngineConsist):
    """
    Mail intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # force the child branches apart for middle engines, based on cab ID
        # as of Jan 2025, this is used by tech tree, and (I think) for calculating replacement
        if self.cab_consist.subrole_child_branch_num < 0:
            offset = -2000
        else:
            offset = 2000
        self.subrole_child_branch_num = (
            offset + self.cab_consist.subrole_child_branch_num
        )


class TGVMiddlePassengerEngineConsist(
    TGVMiddleEngineConsistMixin, PassengerEngineConsist
):
    """
    Pax intermediate motor unit for TGV.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # force the child branches apart for middle engines, based on cab ID
        # as of Jan 2025, this is used by tech tree, and (I think) for calculating replacement
        if self.cab_consist.subrole_child_branch_num < 0:
            offset = -1000
        else:
            offset = 1000
        self.subrole_child_branch_num = (
            offset + self.cab_consist.subrole_child_branch_num
        )


class CarConsist(Consist):
    """
    Intermediate class for car (wagon) consists to subclass from, provides sparse properties, most are declared in subclasses.
    """

    def __init__(self, speedy=False, **kwargs):
        # self.base_id = '' # provide in subclass
        # we can't called super yet, because we need the id
        # but we need to call the consist factory to get the id, so duplicate the assignment here (Consist will also set it)
        # CABBAGE model_def?
        kwargs["id"] = kwargs["model_type_factory"].get_wagon_id(self.base_id, **kwargs)
        super().__init__(**kwargs)
        self.roster.register_wagon_consist(self)

        # override this in subclass as needed
        self._joker = False
        # override this in subclass for, e.g. express freight consists
        self.speed_class = "standard"
        # CABBAGE model_def?
        self.subtype = kwargs["subtype"]
        # Weight factor: override in subclass as needed
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 0.8 if self.base_track_type_name == "NG" else 1
        # used to synchronise / desynchronise groups of vehicles, see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
        # default all to car consists to 'universal' offset, override in subclasses as needed
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
        for wagon in self.roster.wagon_consists_by_base_id[self.base_id]:
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
        if self.base_track_type_name == "NG":
            input_spritesheet_delegate_base_id = (
                input_spritesheet_delegate_base_id + "_ng"
            )

        input_spritesheet_delegate_id = self.model_type_factory.get_wagon_id(
            base_id=input_spritesheet_delegate_base_id,
            gen=self.gen,
            subtype=self.subtype,
        )
        return input_spritesheet_delegate_id

    @property
    def cabbage_subtype_badge(self):
        return "ih_wagon_length/" + self.subtype.lower()

    @property
    def wagon_title_class_str(self):
        return "STR_NAME_SUFFIX_" + self.base_id.upper()

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
            # !! this might fail for composite groups where the group has multiple variants from multiple consists, but this specific consist has only one variant
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


class RandomisedConsistMixin(object):
    """
    Mixin to set certain common attributes for randomised consists.
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


class AlignmentCarConsist(CarConsist):
    """
    For checking sprite alignment
    """

    def __init__(self, **kwargs):
        self.base_id = "alignment_car"
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


class AutomobileCarConsistBase(CarConsist):
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
            consist_ruleset = "articulated_permanent_twin_sets"
        else:
            consist_ruleset = self._consist_ruleset
        # automobile cars can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random automobile cargos, which would also cause new random wagon colour
        # ...wouldn't be desirable anyway because they are pseudo-articulated units
        self.gestalt_graphics = GestaltGraphicsAutomobilesTransporter(
            self.spritelayer_cargo_layers,
            consist_ruleset=consist_ruleset,
            liveries=self.liveries,
        )


class AutomobileCarConsist(AutomobileCarConsistBase):
    """
    Automobile transporter with single flat deck at conventional height.
    """

    def __init__(self, **kwargs):
        self.base_id = "automobile_car"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_vehicle_transporter_cars"
        self._joker = True

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
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_vehicle_transporter_cars"
        self._joker = True

    @property
    def _consist_ruleset(self):
        if self.subtype == "B":
            return "2_unit_sets"
        else:
            return "4_unit_sets"

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class AutomobileEnclosedCarConsist(CarConsist):
    """
    Fully enclosed automobile transporter with, no vehicle sprites shown.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_NO_WEATHERING"],
        global_constants.freight_wagon_liveries[
            "COMPLEMENT_COMPANY_COLOUR_NO_WEATHERING"
        ],
    ]

    def __init__(self, **kwargs):
        self.base_id = "enclosed_automobile_car"
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


class BolsterCarConsistBase(CarConsist):
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


class BolsterCarConsist(BolsterCarConsistBase):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    def __init__(self, **kwargs):
        self.base_id = "bolster_car"
        super().__init__(**kwargs)


class BolsterCarHighEndConsist(BolsterCarConsistBase):
    """
    Specialist wagon with side stakes and bolsters for long products, limited refits.
    """

    def __init__(self, **kwargs):
        self.base_id = "high_end_bolster_car"
        super().__init__(**kwargs)


class BolsterCarConsistRandomisedConsist(RandomisedConsistMixin, BolsterCarConsistBase):
    """
    Random choice of bolster car sprite, from available bolster cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "bolster_car_randomised"
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
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "freight_core"
        ]


class BoxCarConsistType1(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "box_car_type_1"
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


class BoxCarConsistType2(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "box_car_type_2"
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


class BoxCarCurtainSideConsist(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "curtain_side_box_car"
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


class BoxCarMerchandiseConsist(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "merchandise_box_car"
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


class BoxCarRandomisedConsist(RandomisedConsistMixin, BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "box_car_randomised"
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


class BoxCarSlidingWallConsistBase(BoxCarConsistBase):
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


class BoxCarSlidingWallConsistType1(BoxCarSlidingWallConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "sliding_wall_car_type_1"
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


class BoxCarSlidingWallConsistType2(BoxCarSlidingWallConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "sliding_wall_car_type_2"
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


class BoxCarVehiclePartsConsist(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "vehicle_parts_box_car"
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


class BulkOpenCarConsistBase(CarConsist):
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


class BulkOpenCarAggregateConsistBase(BulkOpenCarConsistBase):
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


class BulkOpenCarAggregateConsistType1(BulkOpenCarAggregateConsistBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_bulk_open_car_type_1"
        super().__init__(**kwargs)


class BulkOpenCarAggregateConsistType2(BulkOpenCarAggregateConsistBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_bulk_open_car_type_2"
        super().__init__(**kwargs)


class BulkOpenCarAggregateConsistType3(BulkOpenCarAggregateConsistBase):
    """
    Aggregate Car.
    Same as standard dump car, but different appearance and default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_bulk_open_car_type_3"
        super().__init__(**kwargs)


class BulkOpenCarAggregateRandomisedConsist(
    RandomisedConsistMixin, BulkOpenCarAggregateConsistBase
):
    """
    Random choice of aggregate car.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_bulk_open_car_randomised"
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


class BulkOpenCarHeavyDutyConsist(BulkOpenCarConsistBase):
    """
    Heavy duty dump car, higher capacity, reduced speed (set in vehicle class, not consist)
    """

    def __init__(self, **kwargs):
        self.base_id = "heavy_duty_dump_car"
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


class BulkOpenCarMineralConsistBase(BulkOpenCarConsistBase):
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


class BulkOpenCarMineralConsist(BulkOpenCarMineralConsistBase):
    """
    Standard dump car (Mineral Wagon in UK terms).
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_bulk_open_car"
        super().__init__(**kwargs)


class BulkOpenCarMineralHighSideConsist(BulkOpenCarMineralConsistBase):
    """
    Standard dump car (Mineral Wagon in UK terms), with high sides.
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_bulk_open_car_high_side"
        super().__init__(**kwargs)


class BulkOpenCarMineralLowSideConsist(BulkOpenCarMineralConsistBase):
    """
    Standard dump car (Mineral Wagon in UK terms), with low sides.
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_bulk_open_car_low_side"
        super().__init__(**kwargs)


class BulkOpenCarMineralRandomisedConsist(
    RandomisedConsistMixin, BulkOpenCarMineralConsistBase
):
    """
    Random choice of standard dump car (Mineral Wagon in UK terms).
    """

    def __init__(self, **kwargs):
        self.base_id = "mineral_bulk_open_car_randomised"
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


class BulkOpenCarScrapMetalConsistBase(BulkOpenCarConsistBase):
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


class BulkOpenCarScrapMetalConsistType1(BulkOpenCarScrapMetalConsistBase):
    """
    Scrap Metal Car
    """

    def __init__(self, **kwargs):
        self.base_id = "scrap_metal_car_type_1"
        super().__init__(**kwargs)


class BulkOpenCarScrapMetalConsistType2(BulkOpenCarScrapMetalConsistBase):
    """
    Scrap Metal Car
    """

    def __init__(self, **kwargs):
        self.base_id = "scrap_metal_car_type_2"
        super().__init__(**kwargs)


class BulkOpenCarScrapMetalRandomisedConsist(
    RandomisedConsistMixin, BulkOpenCarScrapMetalConsistBase
):
    """
    Random choice of scrap metal car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "scrap_metal_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class BulkOpenCarTipplerConsistBase(BulkOpenCarConsistBase):
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


class BulkOpenCarTipplerConsistType1(BulkOpenCarTipplerConsistBase):
    """
    Tippler (dump car).
    """

    def __init__(self, **kwargs):
        self.base_id = "tippler_bulk_open_car_type_1"
        super().__init__(**kwargs)


class BulkOpenCarTipplerConsistType2(BulkOpenCarTipplerConsistBase):
    """
    Tippler (dump car).
    """

    def __init__(self, **kwargs):
        self.base_id = "tippler_bulk_open_car_type_2"
        super().__init__(**kwargs)


class BulkOpenCarTipplerRotaryConsistType1(BulkOpenCarTipplerConsistBase):
    """
    Tippler (dump car).
    """

    def __init__(self, **kwargs):
        self.base_id = "tippler_rotary_bulk_open_car_type_1"
        super().__init__(**kwargs)
        # needed to clear randomised set by base class - rotary tipplers don't look good as randomisation candidates
        self.randomised_candidate_groups = []


class BulkOpenCarTipplerRandomisedConsist(
    RandomisedConsistMixin, BulkOpenCarTipplerConsistBase
):
    """
    Random choice of tippler (dump car).
    """

    def __init__(self, **kwargs):
        self.base_id = "tippler_bulk_open_car_randomised"
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


# not in alphabetical order as it depends on subclassing BulkOpenCarConsistBase
class BulkCarBoxRandomisedConsist(RandomisedConsistMixin, BulkOpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "bulk_car_box_randomised"
        super().__init__(**kwargs)
        self.use_named_buyable_variant_group = "wagon_group_bulk_cars_randomised"
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=1,
            liveries=self.liveries,
        )


class BulkCarHopperRandomisedConsist(RandomisedConsistMixin, BulkOpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "bulk_car_hopper_randomised"
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


# not in alphabetical order as it depends on subclassing BulkOpenCarConsistBase
class BulkCarMixedRandomisedConsist(RandomisedConsistMixin, BulkOpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "bulk_car_mixed_randomised"
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


class CabooseCarConsist(CarConsist):
    """
    Caboose, brake van etc - no gameplay purpose, just eye candy.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        self.base_id = "caboose_car"
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
        self.random_reverse = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsCaboose(
            recolour_map=graphics_constants.caboose_car_body_recolour_map,
            liveries=self.liveries,
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


class CaneBinCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "cane_bin_car"
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


class CarbonBlackHopperCarConsist(CarConsist):
    """
    Dedicated covered hopper car for carbon black.  No other cargos.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "carbon_black_hopper_car"
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


class CoilBuggyCarConsist(CarConsist):
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

    # note does NOT subclass CoilCarConsistBase - different type of consist
    def __init__(self, **kwargs):
        self.base_id = "coil_buggy_car"
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


class CoilCarConsistBase(CarConsist):
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


class CoilCarCoveredAsymmetricConsist(CoilCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "coil_car_covered_asymmetric"
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
        self.random_reverse = True
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


class CoilCarCoveredConsist(CoilCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "coil_car_covered"
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


class CoilCarTarpaulinConsist(CoilCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "coil_car_tarpaulin"
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


class CoilCarUncoveredConsist(CoilCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "coil_car_uncovered"
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


class DedicatedCoilCarRandomisedConsist(RandomisedConsistMixin, CoilCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "dedicated_coil_car_randomised"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_coil_cars"
        self._joker = True
        # because the asymmetric covered wagons can reverse
        self.random_reverse = True
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=self.liveries,
        )


class CoveredHopperCarConsistBase(CarConsist):
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


class CoveredHopperCarConsistType1(CoveredHopperCarConsistBase):
    """
    Default covered hopper type.
    """

    def __init__(self, **kwargs):
        self.base_id = "covered_hopper_car_type_1"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"


class CoveredHopperCarConsistType2(CoveredHopperCarConsistBase):
    """
    Default covered hopper type.
    """

    def __init__(self, **kwargs):
        self.base_id = "covered_hopper_car_type_2"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"
        self._joker = True


class CoveredHopperCarConsistType3(CoveredHopperCarConsistBase):
    """
    Default covered hopper type.
    """

    def __init__(self, **kwargs):
        self.base_id = "covered_hopper_car_type_3"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["covered_pellet"]
        self.randomised_candidate_groups = ["covered_hopper_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_covered_hopper_cars"
        self._joker = True


class CoveredHopperCarRandomisedConsist(
    RandomisedConsistMixin, CoveredHopperCarConsistBase
):
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

    def __init__(self, **kwargs):
        self.base_id = "covered_hopper_car_randomised"
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


class CoveredHopperCarSwingRoofConsist(CoveredHopperCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "swing_roof_hopper_car"
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


class ExpressCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "express_car"
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
        # keep matched to MailCarConsist
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


class ExpressFoodCarRandomisedConsist(RandomisedConsistMixin, CarConsist):
    """
    Random choice of food car sprite, noting limited refits because it includes food tankers.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "express_food_car_randomised"
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


class ExpressFoodTankCarConsistBase(CarConsist):
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


class ExpressFoodTankCarConsistType1(ExpressFoodTankCarConsistBase):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    Formerly known as 'Edibles Tanker', renamed in 2024 to 'Food Tanker' to be easily understand.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_express_tank_car_type_1"
        super().__init__(**kwargs)


class ExpressFoodTankCarConsistType2(ExpressFoodTankCarConsistBase):
    """
    Wine, milk, water etc.
    No actual cargo aging change - doesn't really work - so trades higher speed against lower capacity instead.
    Formerly known as 'Edibles Tanker', renamed in 2024 to 'Food Tanker' to be easily understand.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_express_tank_car_type_2"
        super().__init__(**kwargs)


class ExpressFoodTankCarRandomisedConsist(
    RandomisedConsistMixin, ExpressFoodTankCarConsistBase
):
    """
    Random choice of express food tanker.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_express_tank_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=2,
            liveries=liveries,
        )


class ExpressIntermodalCarConsist(CarConsist):
    """
    Express intermodal container cars - express freight, valuables, mails.
    """

    liveries = [global_constants.freight_wagon_liveries["SWOOSH"]]

    def __init__(self, **kwargs):
        self.base_id = "express_intermodal_car"
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
        # keep matched to MailCarConsist
        self.floating_run_cost_multiplier = 2.33
        self._intro_year_days_offset = global_constants.intro_month_offsets_by_role[
            "express_core"
        ]
        self._joker = True
        self.use_colour_randomisation_strategies = False
        # Graphics configuration
        # !! note to future, if e.g. NA Horse needs longer express intermodal sets, set the consist_ruleset conditionally by checking roster
        # intermodal container wagons can't use random colour swaps on the wagons...
        # ...because the random bits are re-randomised when new cargo loads, to get new random containers, which would also cause new random wagon colour
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            consist_ruleset="2_unit_sets", liveries=self.liveries
        )

    @property
    def spritelayer_cargo_layers(self):
        # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
        # !! express intermodal all default currently, extend as needed
        return ["default"]


class FarmProductsBoxCarConsistBase(CarConsist):
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


class FarmProductsBoxCarConsistType1(FarmProductsBoxCarConsistBase):
    """
    Farm type cargos - box cars / vans.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_box_car_type_1"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_box_car_randomised",
        ]


class FarmProductsBoxCarConsistType2(FarmProductsBoxCarConsistBase):
    """
    Farm type cargos - box cars / vans.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_box_car_type_2"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_box_car_randomised",
        ]


class FarmProductsBoxCarRandomisedConsist(
    RandomisedConsistMixin, FarmProductsBoxCarConsistBase
):
    """
    Random choice of farm products box car / van sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_box_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=1,
            liveries=liveries,
        )


class FarmProductsHopperCarConsistBase(CarConsist):
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


class FarmProductsHopperCarConsistType1(FarmProductsHopperCarConsistBase):
    """
    Farm type cargos - covered hoppers.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_hopper_car_type_1"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_hopper_car_randomised",
        ]


class FarmProductsHopperCarConsistType2(FarmProductsHopperCarConsistBase):
    """
    Farm type cargos - covered hoppers.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_hopper_car_type_2"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "farm_product_hopper_car_randomised",
        ]


class FarmProductsHopperCarRandomisedConsist(
    RandomisedConsistMixin, FarmProductsHopperCarConsistBase
):
    """
    Random choice of farm products hopper sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "farm_product_hopper_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class FoodHopperCarConsistBase(FarmProductsHopperCarConsistBase):
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


class FoodHopperCarConsistType1(FoodHopperCarConsistBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_hopper_car_type_1"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarConsistType2(FoodHopperCarConsistBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_hopper_car_type_2"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarConsistType3(FoodHopperCarConsistBase):
    """
    Food type covered hoppers - same refits as farm product cars.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_hopper_car_type_3"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "food_hopper_car_randomised",
        ]


class FoodHopperCarRandomisedConsist(RandomisedConsistMixin, FoodHopperCarConsistBase):
    """
    Random choice of food hopper sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "food_hopper_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarConsistBase(CarConsist):
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


class FlatCarBulkheadConsistBase(FlatCarConsistBase):
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


class FlatCarBulkheadConsistType1(FlatCarBulkheadConsistBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    # low or high bulkhead? stakes or not?
    def __init__(self, **kwargs):
        self.base_id = "bulkhead_flat_car_type_1"
        super().__init__(**kwargs)


class FlatCarBulkheadConsistType2(FlatCarBulkheadConsistBase):
    """
    Variant of flat wagon with heavy reinforced ends - refits same as flat wagon
    """

    # low or high bulkhead? stakes or not?
    def __init__(self, **kwargs):
        self.base_id = "bulkhead_flat_car_type_2"
        super().__init__(**kwargs)


class FlatCarBulkheadRandomisedConsist(
    RandomisedConsistMixin, FlatCarBulkheadConsistBase
):
    """
    Random choice of bulkhead flat car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "bulkhead_flat_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarDropEndConsist(FlatCarConsistBase):
    """
    Wagon with droppable end flaps - variant on flat wagon, refits same
    """

    def __init__(self, **kwargs):
        self.base_id = "drop_end_flat_car"
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


class FlatCarDropSideConsist(FlatCarConsistBase):
    """
    Wagon with droppable low sides - variant on flat wagon, refits same
    """

    def __init__(self, **kwargs):
        self.base_id = "drop_side_flat_car"
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


class FlatCarConsist(FlatCarConsistBase):
    """
    Flatbed - no stakes, visible cargo.
    """

    def __init__(self, **kwargs):
        self.base_id = "flat_car"
        super().__init__(**kwargs)
        self.randomised_candidate_groups = [
            "flat_car_randomised",
        ]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_flat_cars"


class FlatCarHeavyDutyConsist(FlatCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "heavy_duty_flat_car"
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


class FlatCarMillConsistBase(FlatCarConsistBase):
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


class FlatCarMillConsistType1(FlatCarMillConsistBase):
    """
    Variant of flat wagon designed specfically for steel industry.
    """

    # low or high mill? stakes or not?
    def __init__(self, **kwargs):
        self.base_id = "mill_flat_car_type_1"
        super().__init__(**kwargs)


class FlatCarMillConsistType2(FlatCarMillConsistBase):
    """
    Variant of flat wagon designed specfically for steel industry.
    """

    # low or high mill? stakes or not?
    def __init__(self, **kwargs):
        self.base_id = "mill_flat_car_type_2"
        super().__init__(**kwargs)


class FlatCarMillRandomisedConsist(RandomisedConsistMixin, FlatCarMillConsistBase):
    """
    Random choice of mill flat car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "mill_flat_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=2,
            liveries=liveries,
        )


class FlatCarRandomisedConsist(RandomisedConsistMixin, FlatCarConsistBase):
    """
    Random choice of flat car sprite, from available coil cars, bolster cars etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "flat_car_randomised"
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


class GasTankCarConsistBase(CarConsist):
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


class GasTankCarPressureConsist(GasTankCarConsistBase):
    """
    Pressure tank cars for gases under pressure at low temperatue, e.g. Chlorine etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = "pressure_tank_car"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_pressure_tank_cars"


class GasTankCarCryoConsist(GasTankCarConsistBase):
    """
    Specialist insulated and pressurised tank cars for gases under pressure at low temperatue, e.g. Oxygen etc.
    """

    def __init__(self, **kwargs):
        # tank cars are unrealistically autorefittable, and at no cost
        # Pikka: if people complain that it's unrealistic, tell them "don't do it then"
        self.base_id = "cryo_tank_car"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_pressure_tank_cars"
        self._joker = True


class HopperCarConsistBase(CarConsist):
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


class HopperCarAggregateConsistBase(HopperCarConsistBase):
    """
    Base class for hopper for rock cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["dump_aggregates"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_aggregate_hopper_cars"


class HopperCarAggregateConsistType1(HopperCarAggregateConsistBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_hopper_car_type_1"
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


class HopperCarAggregateConsistType2(HopperCarAggregateConsistBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_hopper_car_type_2"
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


class HopperCarAggregateConsistType3(HopperCarAggregateConsistBase):
    """
    Hopper for rock cargos, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "aggregate_hopper_car_type_3"
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


class HopperCarAggregateRandomisedConsist(
    RandomisedConsistMixin, HopperCarAggregateConsistBase
):
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

    def __init__(self, **kwargs):
        self.base_id = "aggregate_hopper_car_randomised"
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


class HopperCarConsist(HopperCarConsistBase):
    """
    Standard hopper car. Defaults to coal.
    """

    def __init__(self, **kwargs):
        self.base_id = "hopper_car"
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


class HopperCarHighSideConsist(HopperCarConsistBase):
    """
    Hopper for ore cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "hopper_car_high_side"
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


class HopperCarMGRConsistBase(HopperCarConsistBase):
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


class HopperCarMGRConsist(HopperCarMGRConsistBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    def __init__(self, **kwargs):
        self.base_id = "mgr_hopper_car"
        super().__init__(**kwargs)


class HopperCarMGRTopHoodConsist(HopperCarMGRConsistBase):
    """
    Hopper for coal industry cargos, same refits as standard hopper, just a visual variant. UK-specific lolz.
    """

    def __init__(self, **kwargs):
        self.base_id = "mgr_top_hood_hopper_car"
        super().__init__(**kwargs)


class HopperCarRandomisedConsist(RandomisedConsistMixin, HopperCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "hopper_car_randomised"
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


class HopperCarRockConsist(HopperCarConsistBase):
    """
    Hopper for rock cargos, same refits as standard hopper, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "rock_hopper_car"
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


class HopperCarSideDoorConsist(HopperCarConsistBase):
    """
    Side door hopper (saddle-bottom hopper).
    """

    def __init__(self, **kwargs):
        self.base_id = "side_door_hopper_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["hopper_coal"]
        # not eligible for randomisation, doesn't look right
        self.randomised_candidate_groups = []
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


class IngotCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "ingot_car"
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


class IntermodalCarConsistBase(CarConsist):
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
        if kwargs.get("consist_ruleset", None) is not None:
            consist_ruleset = kwargs.get("consist_ruleset")
        else:
            consist_ruleset = "4_unit_sets"
        # !! as of April 2023, company colour isn't used for default intermodal sprite, so use SWOOSH as JFDI
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(
            consist_ruleset=consist_ruleset, liveries=self.liveries
        )


class IntermodalCarConsist(IntermodalCarConsistBase):
    """
    Default intermodal car - simple flat platform at default height.
    """

    def __init__(self, **kwargs):
        self.base_id = "intermodal_car"
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


class IntermodalLowFloorCarConsist(IntermodalCarConsistBase):
    """
    Low floor intermodal car - simple flat platform at height -1
    """

    def __init__(self, **kwargs):
        self.base_id = "low_floor_intermodal_car"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_intermodal_cars"
        self._joker = True

    @property
    # layers for spritelayer cargos, and the platform type (cargo pattern and deck height)
    def spritelayer_cargo_layers(self):
        return ["low_floor"]


class KaolinHopperCarConsist(CarConsist):
    """
    Dedicated to kaolin (china clay).
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "kaolin_hopper_car"
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


class LivestockCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "livestock_car"
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


class LogCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "log_car"
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


class MailCarConsistBase(CarConsist):
    """
    Common base class for mail cars.
    """

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.class_refit_groups = ["mail", "express_freight"]
        # no specific labels needed
        self.label_refits_allowed = []
        self.label_refits_disallowed = polar_fox.constants.disallowed_refits_by_label[
            "non_freight_special_cases"
        ]
        self.default_cargos = polar_fox.constants.default_cargos["mail"]
        # specific structure for capacity multiplier and loading speed, override in subclasses as needed
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["default"]
        # keep matched to ExpressCarConsist
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


class MailRailcarTrailerCarConsistBase(MailCarConsistBase):
    """
    Common base class for mail railcar trailer cars.
    """

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        # cab_id must be passed, do not mask errors with .get()
        self.cab_id = kwargs["cab_id"]
        self._buyable_variant_group_id = self.cab_id
        self.subrole = self.cab_consist.subrole
        # get the intro year offset and life props from the cab, to ensure they're in sync
        self.intro_year_offset = self.cab_consist.intro_year_offset
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        # necessary to ensure that pantograph provision can work, whilst not giving the vehicle any actual power
        self.power_by_power_source = {
            key: 0 for key in self.cab_consist.power_by_power_source.keys()
        }
        self.pantograph_type = self.cab_consist.pantograph_type
        self.suppress_pantograph_if_no_engine_attached = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self._str_name_suffix = "STR_NAME_SUFFIX_TRAILER"
        self._joker = True

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


class MailCarConsist(MailCarConsistBase):
    """
    Mail cars - also handle express freight, valuables.
    """

    def __init__(self, **kwargs):
        self.base_id = "mail_car"
        super().__init__(**kwargs)
        # pony NG jank directly set role buy menu string here, handles pony gen 4 NG speed bump
        if self.base_track_type_name == "NG" and self.gen < 4:
            self.subrole = "universal"
        else:
            self.subrole = "express"
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
        liveries = self.roster.get_pax_mail_liveries("default_mail_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="mail_cars",
            liveries=liveries,
        )


class MailExpressRailcarTrailerCarConsist(MailRailcarTrailerCarConsistBase):
    """
    Unpowered mail trailer car for express railcars.
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "express_railcar_mail_trailer_car"
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_4_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class MailHighSpeedCarConsist(MailCarConsistBase):
    """
    High speed (LGV capable) variant of mail car.
    Position-dependent sprites for brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "high_speed_mail_car"
        super().__init__(**kwargs)
        self.subrole = "very_high_speed"
        self._badges.append("ih_ruleset_flags/report_as_mail_car")
        # mail cars also treated as pax for rulesets (to hide adjacent pax brake coach)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.speed_class = "express"
        self.lgv_capable = True
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
        liveries = self.roster.get_pax_mail_liveries("default_mail_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="mail_cars",
            liveries=liveries,
        )


class MailHSTCarConsist(MailCarConsistBase):
    """
    Trailer dedicated for Mail on HST-type trains (no wagon attach, but matching stats and livery).
    """

    def __init__(self, **kwargs):
        self.base_id = "hst_mail_car"
        super().__init__(**kwargs)
        # cab_id must be passed, do not mask errors with .get()
        self.cab_id = kwargs["cab_id"]
        self._buyable_variant_group_id = self.cab_id
        self.subrole = self.cab_consist.subrole
        self._badges.append("ih_ruleset_flags/report_as_mail_car")
        # mail cars also treated as pax for rulesets (to hide adjacent pax brake coach)
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.speed_class = "hst"
        self.buy_cost_adjustment_factor = 1.66
        # get the intro year offset and life props from the cab, to ensure they're in sync
        self.intro_year_offset = self.cab_consist.intro_year_offset
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="mail_cars",
            liveries=self.cab_consist.gestalt_graphics.liveries,
        )

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


class MetalProductCarRandomisedConsistBase(RandomisedConsistMixin, CoilCarConsistBase):
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
        self.random_reverse = True
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


class MetalProductCarCoveredRandomisedConsist(MetalProductCarRandomisedConsistBase):
    """
    Random choice of cold metal car sprite, from suitable covered coil cars, vans etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "metal_product_car_covered_randomised"
        super().__init__(**kwargs)


class MetalProductCarMixedRandomisedConsist(MetalProductCarRandomisedConsistBase):
    """
    Random choice of cold metal car sprite, from all suitable metal carrying wagons cars etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "metal_product_car_mixed_randomised"
        super().__init__(**kwargs)


class MetalProductCarUncoveredRandomisedConsist(MetalProductCarRandomisedConsistBase):
    """
    Random choice of cold metal car sprite, from suitable bolster, flat, open cars etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "metal_product_car_uncovered_randomised"
        super().__init__(**kwargs)


class MineralCoveredHopperCarConsistBase(CarConsist):
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


class MineralCoveredHopperCarLimeConsistBase(MineralCoveredHopperCarConsistBase):
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


class MineralCoveredHopperCarLimeConsistType1(MineralCoveredHopperCarLimeConsistBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "lime_covered_hopper_car_type_1"
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeConsistType2(MineralCoveredHopperCarLimeConsistBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "lime_covered_hopper_car_type_2"
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeConsistType3(MineralCoveredHopperCarLimeConsistBase):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "lime_covered_hopper_car_type_3"
        super().__init__(**kwargs)


class MineralCoveredHopperCarLimeRandomisedConsist(
    RandomisedConsistMixin, MineralCoveredHopperCarLimeConsistBase
):
    """
    Visual variant of mineral / chemical covered hopper.
    Heavily weathered white - powdered lime / burnt lime / quicklime and similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "lime_covered_hopper_car_randomised"
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


# not in alphabetical order as it depends on subclassing CoveredHopperCarConsistBase
class MineralCoveredHopperCarRandomisedConsist(
    RandomisedConsistMixin, MineralCoveredHopperCarConsistBase
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

    def __init__(self, **kwargs):
        self.base_id = "covered_bulk_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # ruby before bauxite to ensure it appears in buy menu order for mixed version
        # patching get_candidate_liveries_for_randomised_strategy to preserve order from wagon_livery_mixes would be better, but that's non-trivial right now
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_mixed_train_one_car_type_more_common",
            dice_colour=3,
            liveries=self.liveries,
        )


class MineralCoveredHopperCarRollerRoofConsistBase(MineralCoveredHopperCarConsistBase):
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


class MineralCoveredHopperCarRollerRoofConsistType1(
    MineralCoveredHopperCarRollerRoofConsistBase
):
    """
    Mineral covered hopper with a rollover roof.
    """

    def __init__(self, **kwargs):
        self.base_id = "roller_roof_hopper_car_type_1"
        super().__init__(**kwargs)


class MineralCoveredHopperCarRollerRoofConsistType2(
    MineralCoveredHopperCarRollerRoofConsistBase
):
    """
    Mineral covered hopper with a rollover roof.
    """

    def __init__(self, **kwargs):
        self.base_id = "roller_roof_hopper_car_type_2"
        super().__init__(**kwargs)


class MineralCoveredHopperCarRollerRoofRandomisedConsist(
    RandomisedConsistMixin, MineralCoveredHopperCarRollerRoofConsistBase
):
    """
    Mineral covered hopper with a rollover roof.
    """

    def __init__(self, **kwargs):
        self.base_id = "roller_roof_hopper_car_randomised"
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


class MineralCoveredHopperCarSaltConsistBase(MineralCoveredHopperCarConsistBase):
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


class MineralCoveredHopperCarSaltConsist(MineralCoveredHopperCarSaltConsistBase):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "salt_covered_hopper_car"
        super().__init__(**kwargs)


class MineralCoveredHopperCarSaltSwingRoofConsist(
    MineralCoveredHopperCarSaltConsistBase
):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "salt_swing_roof_hopper_car"
        super().__init__(**kwargs)


class MineralCoveredHopperCarSaltRandomisedConsist(
    RandomisedConsistMixin, MineralCoveredHopperCarSaltConsistBase
):
    """
    Mineral covered hopper for salt, potash, similar cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "salt_covered_hopper_car_randomised"
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


class OpenCarConsistBase(CarConsist):
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


class OpenCarConsist(OpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "open_car"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["open"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_open_cars"
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsVisibleCargo(
            bulk=True, piece="open", liveries=self.liveries
        )


class OpenCarHoodConsist(OpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "hood_open_car"
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


class OpenCarHighEndConsist(OpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "high_end_open_car"
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


class OpenCarMillConsist(OpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "mill_open_car"
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


class OpenCarRandomisedConsist(RandomisedConsistMixin, OpenCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "open_car_randomised"
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


class PassengerCarConsistBase(CarConsist):
    """
    Common base class for passenger cars.
    """

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        self.speed_class = "express"
        self.class_refit_groups = ["pax"]
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargos = polar_fox.constants.default_cargos["pax"]
        # specific structure for capacity multiplier and loading speed, override in subclasses as needed
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["default"]
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


class PassengeRailcarTrailerCarConsistBase(PassengerCarConsistBase):
    """
    Common base class for railcar trailer cars.
    """

    def __init__(self, **kwargs):
        # don't set base_id here, let subclasses do it
        super().__init__(**kwargs)
        # cab_id must be passed, do not mask errors with .get()
        self.cab_id = kwargs["cab_id"]
        self._buyable_variant_group_id = self.cab_id
        self.subrole = self.cab_consist.subrole
        # get the intro year offset and life props from the cab, to ensure they're in sync
        self.intro_year_offset = self.cab_consist.intro_year_offset
        self._model_life = self.cab_consist.model_life
        self._vehicle_life = self.cab_consist.vehicle_life
        # necessary to ensure that pantograph provision can work, whilst not giving the vehicle any actual power
        self.power_by_power_source = {
            key: 0 for key in self.cab_consist.power_by_power_source.keys()
        }
        self.pantograph_type = self.cab_consist.pantograph_type
        self.suppress_pantograph_if_no_engine_attached = True
        # train_flag_mu solely used for ottd livery (company colour) selection
        self.train_flag_mu = True
        self._str_name_suffix = "STR_NAME_SUFFIX_TRAILER"
        self._joker = True

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


class PanoramicCarConsist(PassengerCarConsistBase):
    """
    Panoramic car / observation car / dome car.
    No special effects, just an explicitly buildable visual variant of standard passenger car.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    def __init__(self, **kwargs):
        self.base_id = "panoramic_car"
        super().__init__(**kwargs)
        self.subrole = "express"
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
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=liveries,
        )


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
        # pony NG jank directly set role buy menu string here, handles pony gen 4 NG speed bump
        if self.base_track_type_name == "NG" and self.gen < 4:
            self.subrole = "universal"
        else:
            self.subrole = "express"
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
        #   * I removed special coaches from PassengerLuxuryCarConsist Feb 2021, as Restaurant cars were added
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=liveries,
        )


class PassengerHighSpeedCarConsist(PassengerCarConsistBase):
    """
    High speed (LGV capable) variant of passenger car.
    Default decay rate, capacities within reasonable distance of original base set pax coaches.
    Position-dependent sprites for brake car etc.
    """

    # very specific flag used for variable run costs and cargo aging factor with restaurant cars
    # !! this will need made more general if e.g. motorail or observation cars are added
    # not sure why I did this as a class property, but eh
    affected_by_restaurant_car_in_consist = True

    def __init__(self, **kwargs):
        self.base_id = "high_speed_passenger_car"
        super().__init__(**kwargs)
        self.subrole = "very_high_speed"
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.lgv_capable = True
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
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=liveries,
        )


class PassengerExpressRailcarTrailerCarConsist(PassengeRailcarTrailerCarConsistBase):
    """
    Unpowered passenger trailer car for express railcars.
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "express_railcar_passenger_trailer_car"
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_6_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


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
        # cab_id must be passed, do not mask errors with .get()
        self.cab_id = kwargs["cab_id"]
        self._buyable_variant_group_id = self.cab_id
        self.subrole = self.cab_consist.subrole
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.buy_cost_adjustment_factor = 1.66
        # run cost multiplier matches standard pax coach costs; higher speed is accounted for automatically already
        self.floating_run_cost_multiplier = 3.33
        # get the intro year offset and life props from the cab, to ensure they're in sync
        self.intro_year_offset = self.cab_consist.intro_year_offset
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=self.cab_consist.gestalt_graphics.liveries,
        )

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


class PassengerRailbusTrailerCarConsist(PassengeRailcarTrailerCarConsistBase):
    """
    Unpowered passenger trailer car for railbus (not railcar).
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "railbus_passenger_trailer_car"
        super().__init__(**kwargs)
        if self.base_track_type_name == "NG" and self.gen == 4:
            # pony NG jank, gen 4 railbus trailers get a speed bump to 'express'
            self.speed_class = "express"
        else:
            # PassengerCarConsistBase sets 'express' speed, but railbus trailers should override this
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_3_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerRailcarTrailerCarConsist(PassengeRailcarTrailerCarConsistBase):
    """
    Unpowered high-capacity passenger trailer car for railcars (not railbus).
    Position-dependent sprites for cabs etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "railcar_passenger_trailer_car"
        super().__init__(**kwargs)
        # PassengerCarConsistBase sets 'express' speed, but railcar trailers should override this
        self.speed_class = "suburban"
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["high_capacity"]
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
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="railcars_3_unit_sets",
            liveries=self.cab_consist.gestalt_graphics.liveries,
            pantograph_type=self.pantograph_type,
        )

    @property
    def is_general_purpose_true_wagon(self):
        return False


class PassengerRestaurantCarConsist(PassengerCarConsistBase):
    """
    Special pax coach that modifies run costs and decay rates for other pax coaches in the consist.
    """

    def __init__(self, **kwargs):
        self.base_id = "restaurant_car"
        super().__init__(**kwargs)
        self.subrole = "restaurant_car"
        # flag pax car ruleset behaviour
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        self.pax_car_capacity_type = self.roster.pax_car_capacity_types["restaurant"]
        self.buy_cost_adjustment_factor = 2.5
        # double the luxury pax car amount; balance between the bonus amount (which scales with num. pax coaches) and the run cost of running this booster
        self.floating_run_cost_multiplier = 12
        # I'd prefer @property, but it was TMWFTLB to replace instances of weight_factor with _weight_factor for the default value
        self.weight_factor = 1 if self.base_track_type_name == "NG" else 2
        self._joker = True
        # Graphics configuration
        # position based variants are not used for restaurant cars, but they use the pax ruleset and sprite compositor for convenience
        spriterow_group_mappings = {"default": 0, "first": 0, "last": 0, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("default_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=liveries,
        )


class PassengerSuburbanCarConsist(PassengerCarConsistBase):
    """
    Suburban pax car.
    Position-dependent sprites for brake car etc.
    """

    def __init__(self, **kwargs):
        self.base_id = "suburban_passenger_car"
        super().__init__(**kwargs)
        self.subrole = "pax_suburban_coach"
        self._badges.append("ih_ruleset_flags/report_as_pax_car")
        # PassengerCarConsistBase sets 'express' speed, but suburban coaches should override this
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
        # Graphics configuration
        # pax cars only have one consist cargo mapping, which they always default to, whatever the consist cargo is
        # position based variants:
        #   * standard coach
        #   * brake coach front
        #   * brake coach rear
        #   * I removed special coaches from PassengerCarConsistBase Dec 2018, overkill
        spriterow_group_mappings = {"default": 0, "first": 1, "last": 2, "special": 0}
        liveries = self.roster.get_pax_mail_liveries("suburban_pax_liveries", **kwargs)
        self.gestalt_graphics = GestaltGraphicsConsistPositionDependent(
            spriterow_group_mappings,
            consist_ruleset="pax_cars",
            liveries=liveries,
        )


class PeatCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "peat_car"
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


class PieceGoodsCarRandomisedConsistBase(RandomisedConsistMixin, CarConsist):
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


class PieceGoodsCarCoveredRandomisedConsist(PieceGoodsCarRandomisedConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "piece_goods_car_covered_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=2,
            liveries=self.liveries,
        )


class PieceGoodsCarMixedRandomisedConsist(PieceGoodsCarRandomisedConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "piece_goods_car_mixed_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=self.liveries,
        )


class PieceGoodsCarManufacturingPartsRandomisedConsist(
    PieceGoodsCarRandomisedConsistBase
):
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

    def __init__(self, **kwargs):
        self.base_id = "piece_goods_car_manufacturing_parts_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_segmented_block_train",
            dice_colour=1,
            liveries=self.liveries,
        )


class PipeCarConsist(FlatCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "pipe_car"
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


class ReeferCarConsistBase(CarConsist):
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


class ReeferCarConsistType1(ReeferCarConsistBase):
    """
    Standard reefer car.
    """

    def __init__(self, **kwargs):
        self.base_id = "reefer_car_type_1"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_reefer_cars"


class ReeferCarConsistType2(ReeferCarConsistBase):
    """
    Alternative reefer car style.
    """

    def __init__(self, **kwargs):
        self.base_id = "reefer_car_type_2"
        super().__init__(**kwargs)
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_reefer_cars"
        self._joker = True


class ReeferCarRandomisedConsist(RandomisedConsistMixin, ReeferCarConsistBase):
    """
    Random choice of reefer car sprite.
    """

    def __init__(self, **kwargs):
        self.base_id = "reefer_car_randomised"
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


class SiloCarConsistBase(CarConsist):
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


class SiloCarConsistType1(SiloCarConsistBase):
    """
    Standard silo car.
    """

    def __init__(self, **kwargs):
        self.base_id = "silo_car_type_1"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarConsistType2(SiloCarConsistBase):
    """
    Silo car with V-shaped barrel.
    """

    def __init__(self, **kwargs):
        self.base_id = "silo_car_type_2"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarConsistType3(SiloCarConsistBase):
    """
    Silo car with V-shaped barrel.
    """

    def __init__(self, **kwargs):
        self.base_id = "silo_car_type_3"
        super().__init__(**kwargs)
        self.default_cargos = polar_fox.constants.default_cargos["silo_chemical"]
        self.randomised_candidate_groups = ["silo_car_randomised"]
        # buyable variant groups are created post-hoc and can group across subclasses
        # any buyable variants (liveries) within the subclass will be automatically added to the group
        self.use_named_buyable_variant_group = "wagon_group_silo_cars"


class SiloCarRandomisedConsist(RandomisedConsistMixin, SiloCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "silo_car_randomised"
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


class SiloCarCementConsistType1(SiloCarConsistBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "cement_silo_car_type_1"
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


class SiloCarCementConsistType2(SiloCarConsistBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "cement_silo_car_type_2"
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


class SiloCarCementConsistType3(SiloCarConsistBase):
    """
    Cement-coloured silo car.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "cement_silo_car_type_3"
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


class SiloCarCementRandomisedConsist(RandomisedConsistMixin, SiloCarConsistBase):
    """
    Random choice of cement silo car sprite.
    """

    liveries = [
        global_constants.freight_wagon_liveries["COMPANY_COLOUR_USE_WEATHERING"]
    ]

    def __init__(self, **kwargs):
        self.base_id = "cement_silo_car_randomised"
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


class SlidingRoofCarConsist(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "sliding_roof_car"
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


class SlidingRoofCarConsistHiCube(BoxCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "sliding_roof_hi_cube_car"
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


class SlagLadleCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "slag_ladle_car"
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


class TankCarConsistBase(CarConsist):
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


class TankCarAcidConsistBase(TankCarConsistBase):
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


class TankCarAcidConsistType1(TankCarAcidConsistBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "acid_tank_car_type_1"
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.acid_tank_car_type_1_livery_recolour_map,
            "weathered": graphics_constants.acid_tank_car_type_1_livery_recolour_map_weathered,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarAcidConsistType2(TankCarAcidConsistBase):
    """
    Visual variant of the standard tank car, same refits, different default cargos.
    """

    def __init__(self, **kwargs):
        self.base_id = "acid_tank_car_type_2"
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.acid_tank_car_type_2_livery_recolour_map,
            "weathered": graphics_constants.acid_tank_car_type_2_livery_recolour_map_weathered,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarAcidRandomisedConsist(RandomisedConsistMixin, TankCarAcidConsistBase):
    """
    Random choice of acid tank car sprites.
    """

    def __init__(self, **kwargs):
        self.base_id = "acid_tank_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarChemicalRandomisedConsist(RandomisedConsistMixin, TankCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "chemical_tank_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=self.liveries,
        )


class TankCarProductConsistBase(TankCarConsistBase):
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


class TankCarProductConsistType1(TankCarProductConsistBase):
    """
    Tank car with more visible ribs etc than standard tank car, for chemicals, specialist cargos etc.
    Same refits as standard tank car, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "product_tank_car_type_1"
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.body_recolour_CC1,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarProductConsistType2(TankCarProductConsistBase):
    """
    Tank car with more visible ribs etc than standard tank car, for chemicals, specialist cargos etc.
    Same refits as standard tank car, just a visual variant.
    """

    def __init__(self, **kwargs):
        self.base_id = "product_tank_car_type_2"
        super().__init__(**kwargs)
        # Graphics configuration
        weathered_variants = {
            "unweathered": graphics_constants.body_recolour_CC1,
        }
        self.gestalt_graphics.weathered_variants = weathered_variants


class TankCarProductRandomisedConsist(
    RandomisedConsistMixin, TankCarProductConsistBase
):
    """
    Random choice of product tank car.
    """

    def __init__(self, **kwargs):
        self.base_id = "product_tank_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarStandardConsistBase(TankCarConsistBase):
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


class TankCarStandardConsistType1(TankCarStandardConsistBase):
    """
    Standard tank car
    """

    def __init__(self, **kwargs):
        self.base_id = "tank_car_type_1"
        super().__init__(**kwargs)


class TankCarStandardConsistType2(TankCarStandardConsistBase):
    """
    Standard tank car
    """

    def __init__(self, **kwargs):
        self.base_id = "tank_car_type_2"
        super().__init__(**kwargs)


class TankCarStandardConsistType3(TankCarStandardConsistBase):
    """
    Standard tank car
    """

    def __init__(self, **kwargs):
        self.base_id = "tank_car_type_3"
        super().__init__(**kwargs)


class TankCarStandardRandomisedConsist(
    RandomisedConsistMixin, TankCarStandardConsistBase
):
    """
    Random choice of acid tank car sprites.
    """

    def __init__(self, **kwargs):
        self.base_id = "tank_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        # note we copy the liveries from the base class gestalt, but then replace the gestalt in this instance with the randomised gestalt
        liveries = self.gestalt_graphics.liveries.copy()
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_loose_mixed_train",
            dice_colour=3,
            liveries=liveries,
        )


class TankCarVolatilesConsistBase(TankCarConsistBase):
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


class TankCarVolatilesConsistType1(TankCarVolatilesConsistBase):
    """
    Tank car with reflective silver or white finish (for low-flashpoint / volative liquids such as petrol).
    """

    def __init__(self, **kwargs):
        self.base_id = "volatiles_tank_car_type_1"
        super().__init__(**kwargs)


class TarpaulinCarConsistBase(BoxCarConsistBase):
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


class TarpaulinCarConsistType1(TarpaulinCarConsistBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    def __init__(self, **kwargs):
        self.base_id = "tarpaulin_car_type_1"
        super().__init__(**kwargs)


class TarpaulinCarConsistType2(TarpaulinCarConsistBase):
    """
    Tarpaulin car - refits similar to box van for gameplay reasons, unlike IRL (which is flat)
    """

    def __init__(self, **kwargs):
        self.base_id = "tarpaulin_car_type_2"
        super().__init__(**kwargs)


class TarpaulinCarConsistType3(TarpaulinCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "tarpaulin_car_type_3"
        super().__init__(**kwargs)
        # Graphics configuration
        # slightly fewer liveries than TarpaulinCarConsistBase
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


class TarpaulinCarRandomisedConsist(RandomisedConsistMixin, TarpaulinCarConsistBase):
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

    def __init__(self, **kwargs):
        self.base_id = "tarpaulin_car_randomised"
        super().__init__(**kwargs)
        # Graphics configuration
        self.gestalt_graphics = GestaltGraphicsRandomisedWagon(
            random_vehicle_map_type="map_block_train_with_minor_variation",
            dice_colour=3,
            liveries=self.liveries,
        )


class TorpedoCarConsist(CarConsist):
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

    def __init__(self, **kwargs):
        self.base_id = "torpedo_car"
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
                # everything else goes into one group, either on the consist group, or a named parent group which composes multiple consists
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
    Consists have buyable_variants, and each unit of the consist needs a corresponding unit_variant.
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


class Train(object):
    """
    Base class for all types of trains
    """

    def __init__(self, **kwargs):
        self._unit_def = kwargs["unit_def"]
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
        self._weight = self._unit_def.weight
        # !! the need to copy cargo refits from the consist is legacy from the default multi-unit articulated consists in Iron Horse 1
        # !! could likely be refactored !!
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.autorefit = True
        # nml constant (STEAM is sane default)
        self.engine_class = "ENGINE_CLASS_STEAM"
        # structure for effect spawn and sprites, default and per railtype as needed
        # optional, use to override automatic effect positioning
        # expects a list of offset pairs [(x, y), (x, y)] etc
        # n.b max 4 effects (nml limit)
        # CABBAGE unit_def?
        self._effect_offsets = kwargs.get("effect_offsets", None)
        self.default_effect_z_offset = (
            12  # optimised for Pony diesel and electric trains
        )
        # 'symmetric' or 'asymmetric'?
        # defaults to symmetric, override in subclasses or per vehicle as needed
        self._symmetry_type = "symmetric"
        # optional - a switch name to trigger re-randomising vehicle random bits - override as need in subclasses
        self.random_trigger_switch = None
        # store the kwargs so we can clone this unit later if we need to
        self.kwargs_for_optional_consist_cloning_later = kwargs

    @property
    def tail_light(self):
        # optional - some engine units need to set explicit tail light spritesheets
        # subclasses may override this, e.g. wagons have an automatic tail light based on vehicle length
        if self._unit_def.tail_light is not None:
            return self._unit_def.tail_light
        else:
            return "empty"

    @property
    def effects(self):
        # empty by default, set in subtypes as needed
        return {}

    @property
    def spriterow_num(self):
        if self._unit_def.spriterow_num is not None:
            return self._unit_def.spriterow_num
        else:
            return 0

    @property
    def CABBAGE_capacity(self):
        if self._unit_def.capacity is not None:
            return self._unit_def.capacity
        else:
            return 0

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # allow that integer maths is needed for newgrf cb results; round up for safety
        try:
            result = [
                int(math.ceil(capacity * multiplier))
                for multiplier in global_constants.capacity_multipliers
            ]
        except:
            raise Exception(
                "get_capacity_variations" + " " + self.id + " " + self.consist.id
            )
        return result

    @property
    def capacities(self):
        return self.get_capacity_variations(self.CABBAGE_capacity)

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

    def get_mail_car_capacity(self):
        result = (
            int(self.get_freight_car_capacity()) / polar_fox.constants.mail_multiplier
        )
        return result

    def get_freight_car_capacity(self):
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        result = int(self.vehicle_length * base_capacity)
        return result

    @property
    def weight(self):
        # weight can be set explicitly or by methods on subclasses
        return self._weight

    @property
    def vehicle_length(self):
        # length of this unit, either derived from from chassis length, or set explicitly via keyword
        # first guard that one and only one of these props is set
        if (
            self._unit_def.vehicle_length is not None
            and self._unit_def.chassis is not None
        ):
            utils.echo_message(
                self.consist.id
                + " has units with both chassis and length properties set"
            )
        if self._unit_def.vehicle_length is None and self._unit_def.chassis is None:
            utils.echo_message(
                self.consist.id
                + " has units with neither chassis nor length properties set"
            )

        if self._unit_def.chassis is not None:
            # assume that chassis name format is 'foo_bar_ham_eggs_24px' or similar - true as of Nov 2020
            # if chassis name format changes / varies in future, just update the string slice accordingly, safe enough
            # splits on _, then takes last entry, then slices to remove 'px'
            result = int(self._unit_def.chassis.split("_")[-1][0:-2])
            return int(result / 4)
        else:
            return self._unit_def.vehicle_length

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
        if self._unit_def.symmetry_type is not None:
            symmetry_type = self._unit_def.symmetry_type
        else:
            symmetry_type = self._symmetry_type
        assert symmetry_type in [
            "symmetric",
            "asymmetric",
        ], "symmetry_type '%s' is invalid in %s" % (
            symmetry_type,
            self.consist.id,
        )
        return symmetry_type

    @property
    def misc_flags(self):
        # note that there are both misc_flags and extra_flags, for grf_spec reasons
        misc_flags = ["TRAIN_FLAG_2CC", "TRAIN_FLAG_SPRITE_STACK"]
        if self.autorefit:
            misc_flags.append("TRAIN_FLAG_AUTOREFIT")
        if self.consist.tilt_bonus:
            misc_flags.append("TRAIN_FLAG_TILT")
        if self.consist.train_flag_mu:
            misc_flags.append("TRAIN_FLAG_MU")
        return ",".join(misc_flags)

    def get_extra_flags(self, unit_variant):
        extra_flags = []
        if unit_variant.buyable_variant.buyable_variant_group is not None:
            # some of these aren't needed for wagons or articulated trailing parts, but eh, probably fine?
            # disable news and exclusive preview for all variants except the default
            if (
                unit_variant.buyable_variant.get_variant_group_parent_vehicle_id()
                is not None
            ):
                extra_flags.append("VEHICLE_FLAG_DISABLE_NEW_VEHICLE_MESSAGE")
                extra_flags.append("VEHICLE_FLAG_DISABLE_EXCLUSIVE_PREVIEW")
            extra_flags.append("VEHICLE_FLAG_SYNC_VARIANT_EXCLUSIVE_PREVIEW")
            extra_flags.append("VEHICLE_FLAG_SYNC_VARIANT_RELIABILITY")
        return ",".join(extra_flags)

    def get_cargo_classes_for_nml(self, allow_disallow_key):
        result = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        if hasattr(self, "articulated_unit_different_class_refit_groups"):
            # in *rare* cases an articulated unit might need different refit classes to its parent consist
            class_refit_groups = self.articulated_unit_different_class_refit_groups
        else:
            # by default get the refit classes from the consist
            class_refit_groups = self.consist.class_refit_groups
        for class_refit_group in class_refit_groups:
            for cargo_class in global_constants.base_refits_by_class[class_refit_group][
                allow_disallow_key
            ]:
                result.append(cargo_class)
        # !! this does not currently support train prop 0x32 (filter allowed classes)
        # !! if that's needed, then branch on allow_disallow_key == "allowed":
        return "bitmask(" + ",".join(result) + ")"

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
            return None

    @property
    def effects_vary_by_power_source(self):
        # simple check if more than one type of effect is defined
        return len(self.effects) > 1

    @property
    def default_effect_offsets(self):
        # override this in subclasses as needed (e.g. to move steam engine smoke to front by default
        # vehicles can also override this on init (stored on each model_variant as _effect_offsets)
        return [(0, 0)]

    def get_nml_expression_for_effects(self, railtype="default"):
        # provides part of nml switch for effects (smoke)

        # effects can be over-ridden per vehicle, or use a default from the vehicle subclass
        if self._effect_offsets is not None:
            effect_offsets = self._effect_offsets
        else:
            effect_offsets = self.default_effect_offsets

        # z offset is handled independently to x, y for simplicity, option to override z offset default per vehicle
        if self._unit_def.effect_z_offset is not None:
            z_offset = self._unit_def.effect_z_offset
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

    def get_spriteset_template_name(self, reversed, y):
        template_name = "_".join(
            [
                "spriteset_template",
                self.symmetry_type,
                reversed,
                str(self.vehicle_length),
                "8",
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
        template_name = self.consist.gestalt_graphics.nml_template
        template = templates[template_name]
        nml_result = template(
            vehicle=self,
            consist=self.consist,
            global_constants=global_constants,
            utils=utils,
            temp_storage_ids=global_constants.temp_storage_ids,  # convenience measure
            graphics_path=graphics_path,
            spritelayer_cargos=spritelayer_cargos,
        )
        return nml_result


class BatteryHybridEngineUnit(Train):
    """
    Unit for a battery hybrid engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # most battery hybrid engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_STEAM"]}


class CabbageDVTUnit(Train):
    """
    Unit for a DVT / Cabbage (driving cab with mail capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class CabControlPaxCarUnit(Train):
    """
    Unit for a cab control car (driving cab with pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class CombineUnitMailBase(Train):
    """
    Mail unit for a combine vehicle (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = [
            "mail"
        ]  # note mail only, no other express cargos

    @property
    def CABBAGE_capacity(self):
        # 0.75 is to account for some pax capacity 'on' this unit (implemented on adjacent pax unit)
        return 0.75 * self.get_mail_car_capacity()


class CombineUnitPaxBase(Train):
    """
    Pax unit for a combine vehicle (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = ["pax"]

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class AutoCoachCombineUnitMail(CombineUnitMailBase):
    """
    Mail unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

class AutoCoachCombineUnitPax(CombineUnitPaxBase):
    """
    Pax unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}


class DieselRailcarCombineUnitMail(CombineUnitMailBase):
    """
    Mail unit for a combine diesel railcar (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]
        }


class DieselRailcarCombineUnitPax(CombineUnitPaxBase):
    """
    Pax unit for a combine diesel railcar (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]
        }

class DieselEngineUnit(Train):
    """
    Unit for a diesel engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # most diesel engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]
        }

class DieselRailcarBaseUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to set symmetry.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # the cab magic won't work unless it's asymmetric eh? :)
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")
        # note that railcar effects are left in default position, no attempt to move them to end of vehicle, or double them (tried, looks weird)


class DieselExpressRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel express railcar.  Just a sparse subclass to set capacity and effects.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # effects
        self.engine_class = "ENGINE_CLASS_DIESEL"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]
        }

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class DieselRailcarMailUnit(DieselRailcarBaseUnit):
    """
    Unit for a mail diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class DieselRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class ElectricEngineUnit(Train):
    """
    Unit for an electric engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        # almost all electric engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        # option to suppress default effects here via unit_def
        if self._unit_def.effects is not None:
            return self._unit_def.effects
        else:
            return {
                "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
            }


class ElectricHighSpeedUnitBase(Train):
    """
    Unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        # option to suppress default effects here via unit_def
        if self._unit_def.effects is not None:
            return self._unit_def.effects
        else:
            return {
                "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
            }

class ElectricHighSpeedMailUnit(ElectricHighSpeedUnitBase):
    """
    Mail unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class ElectricHighSpeedPaxUnit(ElectricHighSpeedUnitBase):
    """
    Passenger unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        # this won't work with double deck high speed in future, extend a class for that then if needed
        return self.get_pax_car_capacity()


class ElectroDieselEngineUnit(Train):
    """
    Unit for a bi-mode Locomotive - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1  # will get same buy cost factor as electric engine of same gen (blah balancing)
        # almost all electro-diesel engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }


class ElectroDieselRailcarBaseUnit(Train):
    """
    Unit for a bi-mode railcar - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1.15  # will get higher buy cost factor than electric railcar of same gen (blah balancing)
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }


class ElectroDieselRailcarMailUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a mail electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class ElectroDieselExpressRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel express railcar.  Just a sparse subclass to set and effects.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # effects
        self.engine_class = "ENGINE_CLASS_DIESEL"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class ElectricRailcarBaseUnit(Train):
    """
    Unit for an electric railcar.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }


class ElectricExpressRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a express pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class ElectricRailcarMailUnit(ElectricRailcarBaseUnit):
    """
    Unit for a mail electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class ElectricRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a pax electric railcar.  Just a sparse subclass to set capacity and force the second livery to be used via dubious means.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class MetroUnit(Train):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs["consist"].base_track_type_name = "METRO"
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.default_effect_z_offset = (
            1  # optimised for Pony diesel and electric trains
        )
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
        }

    @property
    def CABBAGE_capacity(self):
        print("CABBAGE_capacity", "Metro")
        return 0


class SnowploughUnit(Train):
    """
    Unit for a snowplough.  Snowploughs have express cargo capacity, so they can actually be useful. :P
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # !! needs changing??
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


class SteamEngineUnit(Train):
    """
    Unit for a steam engine, with smoke
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self.default_effect_z_offset = 13  # optimised for Pony steam trains
        self._symmetry_type = "asymmetric"  # assume all steam engines are asymmetric

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_STEAM", "EFFECT_SPRITE_STEAM"]
        }

    @property
    def default_effect_offsets(self):
        # force steam engine smoke to front by default, can also override per unit for more precise positioning
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
        # most wagons are symmetric, override per vehicle or subclass as needed
        self._symmetry_type = kwargs.get("symmetry_type", "symmetric")

    @property
    def tail_light(self):
        # all wagons use auto tail-lights based on length
        # override in subclass if needed
        return str(self.vehicle_length * 4) + "px"

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
    Caboose Car. This subclass only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # caboose cars may be asymmetric, they are also user-flippable as of August 2022
        self._symmetry_type = "asymmetric"

    @property
    def weight(self):
        # special handling of weight
        weight_factor = 3 if self.consist.base_track_type_name == "NG" else 5
        return weight_factor * self.vehicle_length

    @property
    def CABBAGE_capacity(self):
        return 0


class PaxCar(TrainCar):
    """
    Pax wagon. This subclass only exists to set capacity and symmetry_type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"

    @property
    def CABBAGE_capacity(self):
        return self.get_pax_car_capacity()


class PaxRailcarTrailerCar(PaxCar):
    """
    Railcar (or railbus) unpowered pax trailer. This subclass only exists to set tail light
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def tail_light(self):
        # TrainCar sets auto tail light, override it in unit_def, fail if not set
        assert (
            self._unit_def.tail_light is not None
        ), "%s consist has a unit without tail_light set, which is required for %s" % (
            self.id,
            self.__class__.__name__,
        )
        return self._unit_def.tail_light


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

    @property
    def CABBAGE_capacity(self):
        return self.get_mail_car_capacity()


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


class MailRailcarTrailerCar(ExpressCar):
    """
    Railcar (or railbus) unpowered mail trailer. This subclass only exists to set tail light and symmetry type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"

    @property
    def tail_light(self):
        # TrainCar sets auto tail light, override it in unit_def, fail if not set
        assert (
            self._unit_def.tail_light is not None
        ), "%s consist has a unit without tail_light set, which is required for %s" % (
            self.id,
            self.__class__.__name__,
        )
        return self._unit_def.tail_light


class AutomobileCarAsymmetric(ExpressCar):
    """
    Automobile (cars, trucks, tractors) transporter car, subclassed from express car.
    This subclass exists to set symmetry_type and random trigger.
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
    This subclass exists to set symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # some vehicle transporter cars are symmetric
        self._symmetry_type = "symmetric"
        utils.echo_message(
            "AutomobileCarSymmetric random_trigger_switch is using _switch_graphics_spritelayer_cargos "
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

    @property
    def CABBAGE_capacity(self):
        if self._unit_def.capacity is not None:
            print(
                self.consist.id,
                self.id,
                " has a capacity set in init - possibly incorrect",
                kwargs.get("capacity", None),
            )
        # magic to set freight car capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        return self.vehicle_length * base_capacity


class BinCar(FreightCar):
    """
    Peat wagon, cane bin car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class CoilBuggyCar(FreightCar):
    """
    Coil buggy car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class CoilCarAsymmetric(FreightCar):
    """
    Asymmetric coil car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


class HeavyDutyCar(FreightCar):
    """
    Heavy duty car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class IngotCar(FreightCar):
    """
    Ingot car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def CABBAGE_capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


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

    @property
    def CABBAGE_capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class TorpedoCar(FreightCar):
    """
    Torpedo car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # just multiply whatever is set by the init, what could go wrong? :)
        self._symmetry_type = "asymmetric"

    @property
    def CABBAGE_capacity(self):
        # capacity bonus is solely to support using small stations in Steeltown where space between industries is constrained
        return 1.5 * self.get_freight_car_capacity()
