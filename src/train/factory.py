import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import copy
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from train import model_type as model_type_module
from train import unit as unit_module


@dataclass
class ModelDef:
    # Required fields (lexically sorted)
    class_name: str
    gen: Any
    sprites_complete: bool

    # Optional common fields (lexically sorted)
    additional_liveries: List[Any] = None
    liveries: List[Any] = None
    model_type_id: Optional[str] = None
    base_numeric_id: Optional[int] = None
    base_track_type_name: Optional[str] = None
    buyable_variant_group_id: Optional[str] = None
    cab_id: Optional[str] = None
    decor_spriterow_num: Optional[int] = None
    default_livery_extra_docs_examples: List[Any] = None
    dual_headed: bool = False
    easter_egg_haulage_speed_bonus: Optional[Any] = None
    extended_vehicle_life: bool = False
    fixed_run_cost_points: Optional[int] = None
    intro_year_offset: Optional[int] = None
    lgv_capable: bool = False
    name: Optional[str] = None
    pax_car_capacity_type: Optional[str] = None
    pantograph_type: Optional[str] = None
    power_by_power_source: Optional[Dict[Any, Any]] = None
    random_reverse: bool = False
    replacement_model_model_type_id: Optional[str] = None
    speed: Optional[int] = None
    subrole: Optional[str] = None
    subrole_child_branch_num: Optional[int] = None
    subtype: Optional[str] = None
    tractive_effort_coefficient: Optional[float] = None

    # Optional esoteric fields (lexically sorted)
    buy_menu_sprite_pairs: Optional[Any] = None
    caboose_family: Optional[Any] = None
    caboose_families: Optional[Any] = None
    formation_ruleset: Optional[str] = None
    docs_image_spriterow: Optional[int] = None
    livery_group_name: Optional[Any] = None
    requires_high_clearance: bool = False
    show_decor_in_purchase_for_variants: List[Any] = None
    spriterow_labels: Optional[Any] = None
    tilt_bonus: bool = False

    # Migration / refactoring shims
    cabbage_new_livery_system: bool = False

    # Internal attributes (not provided via __init__) (lexically sorted)
    cloned_from_model_def: Optional["ModelDef"] = field(default=None, init=False)
    clones: List[Any] = field(default_factory=list, init=False)
    unit_defs: List[Any] = field(default_factory=list, init=False)

    def add_unit_def(self, **kwargs):
        self.unit_defs.append(UnitDef(**kwargs))

    def define_description(self, description):
        self.description = description

    def define_foamer_facts(self, foamer_facts):
        self.foamer_facts = foamer_facts

    def begin_clone(self, base_numeric_id, unit_repeats, **kwargs):
        if self.cloned_from_model_def is not None:
            # cloning clones isn't supported, it will cause issues resolving spritesheets etc, and makes it difficult to manage clone id suffixes
            raise Exception(
                "Don't clone a model def that is itself a clone, it won't work as expected. \nClone the original model def. \nModel def is: "
                + self.model_type_id,
            )
        cloned_model_def = copy.deepcopy(self)
        # clone may need to reference original source
        cloned_model_def.cloned_from_model_def = self
        # keep a reference locally for book-keeping
        self.clones.append(cloned_model_def)
        # deepcopy will have created new unit instances, but we might want to modify the sequence for the clone
        # the format is unit_repeats=[x, y z]
        # for each existing unit, this will specify which units to copy, and what their repeat values are
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

        cloned_model_def.base_numeric_id = base_numeric_id
        # this method of resolving id will probably fail with wagons, untested as of Feb 2025, not expected to work, deal with that later if needed
        cloned_model_def.model_type_id = (
            self.model_type_id + "_clone_" + str(len(self.clones))
        )
        cloned_model_def.buyable_variant_group_id = self.model_type_id
        return cloned_model_def

    def complete_clone(self):
        # book-keeping and adjustments after all changes are made to a clone
        self.power_by_power_source = self.clone_adjust_power_by_power_source()
        # purchase menu variant decor isn't supported if the vehicle is articulated, so just forcibly clear this property
        if self.produced_unit_total > 1:
            self.show_decor_in_purchase_for_variants = None

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
        # recalculate power in a clone
        result = {}
        for (
            power_type,
            power_value,
        ) in self.power_by_power_source.items():
            result[power_type] = int(power_value * self.clone_stats_adjustment_factor)
        return result

    @property
    def produced_unit_total(self):
        # convenience way to find out how many units in total this model def will produce
        return sum(unit_def.repeat for unit_def in self.unit_defs)


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


@dataclass
class CatalogueEntry:
    model_variant_id: str
    unit_variant_ids: List[str]
    unit_numeric_ids: List[int]
    livery_name: str


class Catalogue(list):
    """
    CABBAGE - METADATA ABOUT ALL PRODUCED MODEL VARIANTS
        # all available model variants, with ids, numeric ids etc
        # ordered by livery index
    """

    def __init__(self, model_variant_factory):
        self.model_variant_factory = model_variant_factory
        if self.model_variant_factory.cabbage_liveries is not None:
            for livery_counter, livery_name in enumerate(
                self.model_variant_factory.cabbage_liveries
            ):
                if "RANDOM_FROM_CONSIST_LIVERIES_" in livery_name:
                    continue
                model_variant_id = (
                    f"{self.model_variant_factory.model_type_id}_mv_{livery_counter}"
                )
                unit_variant_ids = [
                    f"{model_variant_id}_unit_{i}"
                    for i, _ in enumerate(self.model_def.unit_defs)
                ]
                # pre-calculated numeric IDs provided for every unit
                numeric_id_offset = self.model_def.base_numeric_id + (
                    livery_counter * len(self.model_def.unit_defs)
                )
                unit_numeric_ids = [
                    numeric_id_offset + i
                    for i, _ in enumerate(self.model_def.unit_defs)
                ]
                # note that livery_name is an arbitrary string and might be repeated across model variants
                catalogue_entry = CatalogueEntry(
                    model_variant_id=model_variant_id,
                    unit_variant_ids=unit_variant_ids,
                    unit_numeric_ids=unit_numeric_ids,
                    livery_name=livery_name,
                )
                self.append(catalogue_entry)

    @property
    def model_def(self):
        # just a passthrough for convenience
        return self.model_variant_factory.model_def


class ModelVariantFactory:
    """
    ModelVariantFactory instances:
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

    def __init__(self, model_def, roster_id, roster_id_providing_module):
        self.class_name = model_def.class_name
        self.model_def = model_def
        # rosters can optionally init model variants from other rosters
        # store the roster that inited the model variant, and the roster that the model variant module is in the filesystem path for
        # we don't store the roster object directly as it can fail to pickle with multiprocessing
        self.roster_id = roster_id
        self.roster_id_providing_module = roster_id_providing_module
        # catalogue is a singleton that provides basic metadata for produced model variants
        self.catalogue = Catalogue(self)
        # used for book-keeping related model_variants
        # CABBAGE THIS MIGHT NOT BE NEEDED AT ALL - GO VIA CATALOGUE?
        # DON'T SEE WHY THE FACTORY INSTANCE NEEDS TO TRACK SPECIFIC OBJECT REFERENCES
        self.produced_model_variants = []
        self.produced_units = []

    def produce(self, catalogue_index=None, dry_run=False):

        if catalogue_index == None:
            raise BaseException(
                "no catalogue_index passed for ModelVariantFactory; model_def is "
                + str(self.model_type_cls)
            )

        if self.cabbage_new_livery_system:
            catalogue_entry = self.catalogue[catalogue_index]

            # HAX
            # WE ARE MID-REFACTORING, AND id IS VERY SHIMMED CURRENTLY
            # NEEDS REPLACED WITH BOTH model_type_id and catalogue_entry.mv_id, to be used in templates as appropriate
            if len(self.produced_model_variants) == 0:
                id = self.model_type_id
            else:
                id = (
                    self.model_type_id
                    + "_variant_"
                    + str(len(self.produced_model_variants))
                )

            # CABBAGE FAILS WITH CLONES - HAX TO RESOLVE, THIS SHOULD ALREADY BE FIGURED OUT BY THE CLONE THOUGH
            # CHECK if buyable_variant_group_id is already set?  If it is, leave it alone?
            if self.model_def.cloned_from_model_def is not None:
                self.model_def.buyable_variant_group_id = (
                    self.model_def.cloned_from_model_def.model_type_id
                )
            else:
                self.model_def.buyable_variant_group_id = self.model_def.model_type_id

            model_variant = self.model_type_cls(
                model_variant_factory=self,
                id=id,
                catalogue_entry=catalogue_entry,
            )
            # CABBAGE - CRUDE SHIM TO INCREMENT NUMERIC ID - INSTEAD USE catalogue_entry WHICH HAS THE IDS
            self.model_def.base_numeric_id = self.model_def.base_numeric_id + len(
                self.model_def.unit_defs
            )

        else:
            model_variant = self.model_type_cls(
                model_variant_factory=self,
                id=self.model_type_id,
                catalogue_entry=None,
            )

        # print(model_variant.gestalt_graphics.__class__.__name__)

        if self.roster_id == "pony":
            if len(self.produced_model_variants) == 0:
                if (self.cabbage_liveries == None) and (
                    model_variant.gestalt_graphics.__class__.__name__
                    != "GestaltGraphicsFormationDependent"
                ):
                    print(
                        "No liveries in model_def or class attrs for:", model_variant.id
                    )

        """
        for counter, livery in enumerate(["example", "cabbage_livery"]):
            increment = counter * self.model_def.produced_unit_total
            print(self.model_def.kwargs.get("id", self.model_type_id), self.model_def.kwargs["base_numeric_id"] + increment)
        """

        """
        if hasattr(model_type_cls, "liveries"):
            print(model_type_cls, len(model_type_cls.liveries))
        if self.kwargs.get("additional_liveries", None) != None:
            print(model_type_cls, self.kwargs["additional_liveries"])
        """

        # orchestrate addition of units
        for unit_def in self.model_def.unit_defs:
            try:
                unit_cls = getattr(unit_module, unit_def.class_name)
            except:
                raise Exception(
                    "class_name not found for "
                    + self.model_def.model_type_id
                    + ", "
                    + unit_def.class_name
                )
            # CABBAGE - this is delegating to model_variant currently, by passing unit classes, we want to pass actual units from here, model variant knows too much
            # print(unit_cls, unit)
            model_variant.add_unit(unit_cls, unit_def)

        if dry_run == False:
            self.produced_model_variants.append(model_variant)
        return model_variant

    @property
    def model_type_cls(self):
        # get the class for the model type, uninstantiated
        return getattr(model_type_module, self.class_name)

    @property
    def cabbage_liveries(self):
        # UNFINISHED - NEEDS TO HANDLE cls attr liveries on wagons
        if self.model_def.liveries is not None:
            return self.model_def.liveries
        elif hasattr(self.model_type_cls, "liveries"):
            return self.model_type_cls.liveries
        else:
            return None

    @property
    def cabbage_new_livery_system(self):
        if self.model_def.cabbage_new_livery_system:
            return True
        if getattr(self.model_type_cls, "cabbage_new_livery_system", False):
            return True
        return False

    def cabbage_new_livery_system_livery_index(self, model_variant):
        # THIS IS FOR REVERSE LOOK UP OF LIVERY FROM VARIANT?  IS THIS JUST A MIGRATION SHIM?
        result = self.produced_model_variants.index(model_variant)
        return result

    def cabbage_model_variant_is_default(self, model_variant):
        if getattr(model_variant, "catalogue_entry", None) is None:
            # CABBAGE - shim conditional handles possibility of catalogue entry being None whilst refactoring, remove this later
            return model_variant == self.produced_model_variants[0]
        else:
            return model_variant.catalogue_entry == self.catalogue[0]

    @property
    def model_type_id(self):
        # figures out where a model variant is getting a base id from
        # must be either defined on model_def or in the model variant class attrs
        if self.model_def.model_type_id is not None:
            return self.model_def.model_type_id
        else:
            # we assume it's a wagon id
            return self.get_wagon_id(
                self.model_type_cls.model_type_id_root, self.model_def
            )

    def get_wagon_id(self, model_type_id_root, model_def):
        # auto id creator, used for wagons not engines
        # handled by model variant factory not model variant, better this way
        # special case NG - extend this for other track_types as needed
        # 'normal' rail and 'elrail' doesn't require an id modifier
        if model_def.base_track_type_name == "NG":
            base_id = model_type_id_root + "_ng"
        elif model_def.base_track_type_name == "METRO":
            base_id = model_type_id_root + "_metro"
        else:
            base_id = model_type_id_root

        substrings = []
        # prepend cab_id if present, used for e.g. railcar trailers, HST coaches etc where the wagon matches a specific 'cab' engine
        if model_def.cab_id is not None:
            substrings.append(model_def.cab_id)
        substrings.append(base_id)
        substrings.append(self.roster_id)
        substrings.append("gen")
        substrings.append(str(model_def.gen) + str(model_def.subtype))
        result = "_".join(substrings)
        return result

    @property
    def input_spritesheet_name_stem(self):
        # the input spritesheet name is the same for all variants of the model type
        # optional support for delegating to a spritesheet belonging to a different vehicle type (e.g. when recolouring same base pixels for different wagon types)
        if (
            getattr(self.model_type_cls, "input_spritesheet_delegate_id_root", None)
            is not None
        ):
            input_spritesheet_name_stem = self.get_wagon_id(
                self.model_type_cls.input_spritesheet_delegate_id_root, self.model_def
            )
        else:
            # handle cloned cases by referring to the original consist factory for the path
            if self.model_def.cloned_from_model_def is not None:
                # this will get a default consist from the source factory, mapping this consist to the source spritesheet
                input_spritesheet_name_stem = (
                    self.model_def.cloned_from_model_def.model_type_id
                )
            else:
                input_spritesheet_name_stem = self.model_type_id

        # the consist id might have the consist's roster_id baked into it, if so replace it with the roster_id of the module providing the graphics file
        # this will have a null effect (which is fine) if the roster_id consist is the same as the module providing the graphics gile
        input_spritesheet_name_stem = input_spritesheet_name_stem.replace(
            self.roster_id, self.roster_id_providing_module
        )
        return input_spritesheet_name_stem
