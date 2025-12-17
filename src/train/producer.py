import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import copy
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from functools import cached_property

from train.catalogue import Catalogue
from train import schemas as schemas
from train import unit_types as unit_types
import utils
from utils import timing

import iron_horse


@dataclass
class ModelDef:
    # Required fields (lexically sorted)
    class_name: str
    gen: int
    sprites_complete: bool

    # Optional common fields (lexically sorted)
    additional_liveries: List[Any] = None
    liveries: List[Any] = None
    model_id: Optional[str] = None
    base_numeric_id: Optional[int] = None
    base_track_type: Optional[str] = None
    vehicle_family_id: Optional[str] = None
    cab_id: Optional[str] = None
    decor_spriterow_num: Optional[int] = None
    receives_easter_egg_haulage_speed_bonus: bool = False
    extended_vehicle_life: bool = False
    fixed_run_cost_points: Optional[int] = None
    intro_year_offset: Optional[int] = None
    lgv_capable: bool = False
    name: Optional[str] = None
    pax_car_capacity_type: Optional[str] = None
    pantograph_type: Optional[str] = None
    power_by_power_source: Optional[Dict[Any, Any]] = None
    random_reverse: bool = False
    replacement_model_id: Optional[str] = None
    speed: Optional[int] = None
    subrole: Optional[str] = None
    subrole_child_branch_num: Optional[int] = None
    subtype: Optional[str] = None
    tractive_effort_coefficient: Optional[float] = None

    # Optional esoteric fields (lexically sorted)
    formation_ruleset: Optional[str] = None
    docs_image_spriterow: Optional[int] = None
    livery_group_name: Optional[Any] = None
    quacks_like_a_clone: bool = False
    show_decor_in_purchase_for_variants: List[Any] = None
    tilt_bonus: bool = False

    # Internal attributes (not provided via __init__) (lexically sorted)
    cloned_from_model_def: Optional["ModelDef"] = field(default=None, init=False)
    clones: List[Any] = field(default_factory=list, init=False)
    clone_stats_adjustment_factor: Optional[float] = None
    unit_defs: List[Any] = field(default_factory=list, init=False)

    def add_unit_def(self, **kwargs):
        self.unit_defs.append(UnitDef(**kwargs))

    def define_description(self, description):
        self.description = description

    def define_foamer_facts(self, foamer_facts):
        self.foamer_facts = foamer_facts

    def begin_clone(self, base_numeric_id, unit_repeats):
        return ModelDefCloner.begin_clone(self, base_numeric_id, unit_repeats)

    def complete_clone(self):
        return ModelDefCloner.complete_clone(self)

    @property
    def produced_unit_total(self):
        # convenience way to find out how many units in total this model def will produce
        return sum(unit_def.repeat for unit_def in self.unit_defs)


@dataclass
class UnitDef:
    """Simple wrapper obj to unpack/default required kwargs (the rest are arbitrary)"""

    class_name: str
    repeat: int = 1
    capacity: Optional[int] = None
    weight: Optional[int] = None
    vehicle_length: Optional[int] = None
    rel_spriterow_index: Optional[int] = 0
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


class ModelVariantProducer:
    """
    ModelVariantProducer instances:
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
    - model_id = "ford_transit"
        - model_variant = "ford_transit_blue"
            - model_variant.units = [<FreightRoadVehicleUnitType>]
        - model_variant = "ford_transit_red"
            - model_variant.units = [<FreightRoadVehicleUnitType>]

    - class_name = class Engine(ModelType)
    - model_id = "challenger"
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
        self.catalogue = Catalogue.create(self)
        self.catalogue.add_entries()
        if len(self.catalogue) == 0:
            raise Exception(
                f"{self.catalogue.model_id}\n"
                f"ModelVariantProducer catalogue is empty"
            )

    def produce(self, catalogue_entry=None):

        if catalogue_entry == None:
            raise BaseException(
                "no catalogue_index passed for ModelVariantProducer; model_def is "
                + str(self.schema_cls)
            )

        model_variant = self.schema_cls(
            producer=self,
            catalogue_entry=catalogue_entry,
        )

        # orchestrate addition of units
        for counter, unit_def in enumerate(self.model_def.unit_defs):
            try:
                unit_cls = getattr(unit_types, unit_def.class_name)
            except:
                raise Exception(
                    "class_name not found for "
                    + self.model_def.model_id
                    + ", "
                    + unit_def.class_name
                )
            # print(unit_cls, unit)
            # now add the units
            unit = unit_cls(
                model_variant=model_variant,
                unit_def=unit_def,
                id=catalogue_entry.unit_variant_ids[counter],
                numeric_id=catalogue_entry.unit_numeric_ids[counter],
            )
            for repeat_num in range(unit_def.repeat):
                model_variant.units.append(unit)

        return model_variant

    @cached_property
    def schema_cls(self):
        # get the schema_cls class for the model, uninstantiated
        return getattr(schemas, self.class_name)

    @property
    def roster(self):
        # convenience method, we can't store roster instances directly as they fail to pickle in multiprocessing; instead look up as needed using the string id
        return iron_horse.roster_manager.get_roster_by_id(self.roster_id)

    @property
    def roster_providing_module(self):
        # convenience method, we can't store roster instances directly as they fail to pickle in multiprocessing; instead look up as needed using the string id
        return iron_horse.roster_manager.get_roster_by_id(
            self.roster_id_providing_module
        )

    def get_wagon_id(self, model_id_root, model_def):
        # auto id creator, used for wagons not engines
        # handled by model variant producer not model variant, better this way
        # special case NG - extend this for other track_types as needed
        # 'normal' rail and 'elrail' doesn't require an id modifier
        if model_def.base_track_type == "NG":
            base_id = model_id_root + "_ng"
        elif model_def.base_track_type == "METRO":
            base_id = model_id_root + "_metro"
        else:
            base_id = model_id_root

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
    def cab_producer(self):
        # convenience way to get cab producer
        if self.model_def.cab_id is not None:
            return self.roster.model_variants_by_catalogue[self.model_def.cab_id][
                "catalogue"
            ].producer
        else:
            return None

    @property
    def vehicle_family_id(self):
        # vehicle families can transcend multiple model types, and can be used for purposes such as
        # - fetching common model type names
        # - variant grouping (other methods exist)
        # - badges for behaviour such as formation-dependent sprites
        # - other badges

        # cascade of sources for vehicle family ID
        if self.model_def.vehicle_family_id is not None:
            return self.model_def.vehicle_family_id

        # tgv and hst model types have specific handling
        if self.catalogue.tgv_hst_quacker.quack:
            return self.catalogue.tgv_hst_quacker.vehicle_family_id

        # general methods for wagons
        if self.catalogue.wagon_quacker.quack:
            # trailers can delegate to cab_id if prsent
            if self.model_def.cab_id is not None:
                return self.model_def.cab_id
            # wagon can optionally set vehicle_family_id as class property
            if getattr(self.schema_cls, "vehicle_family_id", None) is not None:
                return self.schema_cls.vehicle_family_id
            # wagons otherwise fall through to just model_id
            return self.schema_cls.model_id_root

        # otherwise fall through to just model_id
        return self.catalogue.model_id

    @property
    def _vehicle_family_badge(self):
        # accessed via catalogue
        # over-ride in subclasses as appropriate
        return f"ih_vehicle_family/{self.vehicle_family_id}"

    @property
    def _vehicle_family_pantograph_display_badges(self):
        # accessed via catalogue
        result = []
        # first find out if we're a trailer, and if we need pans
        if (self.cab_producer is not None) and (
            not self.catalogue.example_model_variant.is_distributed_power_wagon
        ):
            if self.cab_producer.model_def.pantograph_type is not None:
                result.append(
                    f"ih_pantograph_display/requires_cab_present/{self.catalogue.model_id}"
                )
        # now find out if we're a cab, and if we need pans
        if self.catalogue.engine_quacker.is_cab_with_dedicated_trailers:
            if self.model_def.pantograph_type is not None:
                result.append(f"ih_pantograph_display/is_cab/{self.catalogue.model_id}")
        # strictly we should never need both results and could return early, but eh, this also works
        return result

    @property
    def variant_group_id_root(self):
        # we keep this distinct from vehicle_family_id, to support flexibility in variant grouping
        if getattr(self.schema_cls, "variant_group_id_root", None) is not None:
            return self.schema_cls.variant_group_id_root
        elif getattr(self.schema_cls, "model_id_root", None) is not None:
            return f"NAME_SUFFIX_{self.schema_cls.model_id_root}"
        else:
            return self.catalogue.model_id

    def get_variant_group_id(self, livery_def, base_track_type):
        # cascade of sources for variant group ID

        # group trailers with their cabs - needs to be done before generic wagon handling
        # there are a few ways this could be done, doesn't matter which as of Apr 2025
        if self.cab_producer is not None:
            return self.cab_producer.vehicle_family_id

        # default grouping for wagons not otherwise handled above
        if self.catalogue.wagon_quacker.quack:
            if self.catalogue.livery_defs[0] == livery_def:
                livery_suffix = "primary"
            else:
                livery_suffix = "secondary_" + str(
                    self.catalogue.livery_defs.index(livery_def)
                )

            return (
                f"{self.variant_group_id_root}_"
                f"{base_track_type.lower()}_"
                f"gen_{self.model_def.gen}{self.model_def.subtype}_"
                f"{livery_suffix}"
            )

        # delegate to vehicle family
        if self.vehicle_family_id is not None:
            return self.vehicle_family_id

        # should never be reached
        raise ValueError(f"variant_group_id not found for {self.catalogue.model_id}")

    @cached_property
    def input_spritesheet_name_stem(self):
        # the input spritesheet name is the same for all variants of the model type
        # optional support for delegating to a spritesheet belonging to a different vehicle type (e.g. when recolouring same base pixels for different wagon types)
        if (
            getattr(self.schema_cls, "input_spritesheet_delegate_id_root", None)
            is not None
        ):
            # CABBAGE - THIS MAY BE UNUSED
            input_spritesheet_name_stem = self.get_wagon_id(
                self.schema_cls.input_spritesheet_delegate_id_root, self.model_def
            )
        else:
            # handle cloned cases by referring to the original producer for the path
            if self.model_def.cloned_from_model_def is not None:
                input_spritesheet_name_stem = (
                    self.model_def.cloned_from_model_def.model_id
                )
            else:
                input_spritesheet_name_stem = self.catalogue.model_id

        # the id might have a roster_id baked into it, if so replace it with the roster_id of the module providing the graphics file
        # this will have a null effect (which is fine) if the roster_id is the same as the module providing the graphics gile
        input_spritesheet_name_stem = input_spritesheet_name_stem.replace(
            self.roster_id, self.roster_id_providing_module
        )
        return input_spritesheet_name_stem

    @cached_property
    def numeric_id_blocks_consumed(self):
        """
        Returns a sorted list of unique numeric ID blocks (multiple-of-10 bases)
        consumed by this vehicle.
        """
        all_ids = []
        for catalogue_entry in self.catalogue:
            all_ids.extend(catalogue_entry.unit_numeric_ids)

        blocks = {id_ - (id_ % 10) for id_ in all_ids}
        return sorted(blocks)

    def assert_description_foamer_facts(self):
        # if these are too noisy, comment out the caller
        if self.catalogue.engine_quacker.quack:
            if len(self.model_def.description) == 0:
                utils.echo_message(self.catalogue.model_id + " has no description")
            if len(self.model_def.foamer_facts) == 0:
                utils.echo_message(self.catalogue.model_id + " has no foamer_facts")
            if "." in self.model_def.foamer_facts:
                utils.echo_message(
                    self.catalogue.model_id + " foamer_facts has a '.' in it."
                )


class ModelDefCloner:
    """Utility to clone a model_def instance, this is just to keep clone logic out of the simple ModelDef dataclass"""

    @staticmethod
    def begin_clone(model_def, base_numeric_id, unit_repeats):
        if model_def.cloned_from_model_def is not None:
            # cloning clones isn't supported, it will cause issues resolving spritesheets etc, and makes it difficult to manage clone id suffixes
            raise Exception(
                "Don't clone a model def that is itself a clone, it won't work as expected. \nClone the original model def. \nModel def is: "
                + model_def.model_id,
            )
        cloned_model_def = copy.deepcopy(model_def)
        # clone may need to reference original source
        cloned_model_def.cloned_from_model_def = model_def
        # keep a reference locally for book-keeping
        model_def.clones.append(cloned_model_def)
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
        cloned_model_def.model_id = (
            model_def.model_id + "_clone_" + str(len(model_def.clones))
        )
        # this will cause the clone to group as a variant of the original source (unless influenced by other factors)
        cloned_model_def.vehicle_family_id = model_def.model_id
        return cloned_model_def

    @staticmethod
    def complete_clone(model_def):
        # book-keeping and adjustments after all changes are made to a clone

        # clones need to adjust some stats, e.g. power, running_cost etc, we do this by inferring a multiple by comparing number of units that will be produced
        # call on clone, not source, will except (correctly) if called on source
        try:
            source_unit_count = model_def.cloned_from_model_def.produced_unit_total
        except:
            raise Exception("source_unit_count failed" + str(model_def))
        clone_unit_count = model_def.produced_unit_total
        model_def.clone_stats_adjustment_factor = clone_unit_count / source_unit_count

        # recalculate power in a clone
        result = {}
        for (
            power_type,
            power_value,
        ) in model_def.power_by_power_source.items():
            result[power_type] = int(
                power_value * model_def.clone_stats_adjustment_factor
            )
        model_def.power_by_power_source = result

        # purchase menu variant decor isn't supported if the vehicle is articulated, so just forcibly clear this property
        if model_def.produced_unit_total > 1:
            model_def.show_decor_in_purchase_for_variants = None
        return model_def
