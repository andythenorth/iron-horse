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
    base_id: Optional[str] = None
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
    replacement_model_base_id: Optional[str] = None
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
                +self.base_id,
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
        cloned_model_def.base_id = self.base_id + "_clone_" + str(len(self.clones))
        cloned_model_def.buyable_variant_group_id = self.base_id
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


class ModelVariantFactory(object):
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

    def __init__(self, model_def):
        self.class_name = model_def.class_name
        self.model_def = model_def
        # used for book-keeping related model_variants
        self.produced_model_variants = []
        self.produced_units = []

    def set_roster_ids(self, roster_id, roster_id_providing_module):
        # rosters can optionally init model variants from other rosters
        # store the roster that inited the model variant, and the roster that the model variant module is in the filesystem path for
        # we don't store the roster object directly as it can fail to pickle with multiprocessing
        self.roster_id = roster_id
        self.roster_id_providing_module = roster_id_providing_module

    def produce(self, livery=None, dry_run=False):
        if livery == None:
            # just do the default livery, this means that calling ModelVariantFactory.produce() without params will always just return a default model variant, which is useful
            # ASSIGN LIVERY HERE
            pass

        model_type_cls = getattr(model_type_module, self.class_name)

        # this needs to be in roster probably, not the factory - produce should produce only one model variant at once
        if self.model_def.cabbage_new_livery_system:
            if len(self.produced_model_variants) == 0:
                id=self.base_id_resolver(model_type_cls)
            else:
                id=self.base_id_resolver(model_type_cls) + "_variant_" + str(len(self.produced_model_variants))
            # HAX
            self.model_def.base_numeric_id = self.model_def.base_numeric_id + (len(self.produced_model_variants) * self.model_def.produced_unit_total)
            model_variant = model_type_cls(
                model_variant_factory=self,
                id=id,
                cabbage_livery = livery
            )

        else:
            model_variant = model_type_cls(
                model_variant_factory=self,
                id=self.base_id_resolver(model_type_cls),
            )

        #print(model_variant.gestalt_graphics.__class__.__name__)

        """
        for counter, livery in enumerate(["example", "cabbage_livery"]):
            increment = counter * self.model_def.produced_unit_total
            print(self.model_def.kwargs.get("id", model_variant.base_id), self.model_def.kwargs["base_numeric_id"] + increment)
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
                    + self.model_def.base_id
                    + ", "
                    + unit_def.class_name
                )
            # CABBAGE - this is delegating to model_variant currently, by passing unit classes, we want to pass actual units from here, model variant knows too much
            # print(unit_cls, unit)
            model_variant.add_unit(unit_cls, unit_def)

        if dry_run == False:
            self.produced_model_variants.append(model_variant)
        return model_variant

    def base_id_resolver(self, model_type_cls):
        # figures out where a model variant is getting a base id from
        # must be either defined on model_def or in the model variant class attrs
        if self.model_def.base_id is not None:
            return self.model_def.base_id
        else:
            # we assume it's a wagon id
            return self.get_wagon_id(model_type_cls.model_type_id_stem, self.model_def)

    def get_wagon_id(self, model_type_id_stem, model_def):
        # auto id creator, used for wagons not locos
        # handled by model variant factory not model variant, better this way
        base_id = model_type_id_stem
        # special case NG - extend this for other track_types as needed
        # 'normal' rail and 'elrail' doesn't require an id modifier
        if model_def.base_track_type_name == "NG":
            base_id = base_id + "_ng"
        elif model_def.base_track_type_name == "METRO":
            base_id = base_id + "_metro"

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
