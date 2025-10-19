import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import random
import copy
from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional
from functools import cached_property

from train import model_types as model_types
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


@dataclass
class CatalogueEntry:
    """
    The catalogue is composed of multiple CatalogueEntry instances.

    Each CatalogueEntry provides instantiation-time configuration for a model variant instance.
    It aggregates properties derived from model_def and computed by the producer, ensuring
    consumers can access necessary data without referencing the producer directly.
    """

    catalogue: "Catalogue"
    model_id: str
    model_variant_id: str
    unit_variant_ids: List[str]
    unit_numeric_ids: List[int]
    livery_def: "LiveryDef"
    variant_group_id: str
    vehicle_family_id: str
    input_spritesheet_name_stem: str

    @property
    def index(self):
        # convenience function
        return self.catalogue.index(self)


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
                f"{self.model_id}\n" f"ModelVariantProducer catalogue is empty"
            )

    def produce(self, catalogue_entry=None):

        if catalogue_entry == None:
            raise BaseException(
                "no catalogue_index passed for ModelVariantProducer; model_def is "
                + str(self.model_type_cls)
            )

        model_variant = self.model_type_cls(
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
    def model_type_cls(self):
        # get the class for the model type, uninstantiated
        return getattr(model_types, self.class_name)

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

    @cached_property
    def model_id(self):
        # figures out where a model variant is getting a base id from
        # must be either defined on model_def or in the model variant class attrs
        if self.model_def.model_id is not None:
            return self.model_def.model_id
        else:
            # we assume it's a wagon id
            return self.get_wagon_id(self.model_type_cls.model_id_root, self.model_def)

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
            if getattr(self.model_type_cls, "vehicle_family_id", None) is not None:
                return self.model_type_cls.vehicle_family_id
            # wagons otherwise fall through to just model_id
            return self.model_type_cls.model_id_root

        # otherwise fall through to just model_id
        return self.model_id

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
                    f"ih_pantograph_display/requires_cab_present/{self.model_id}"
                )
        # now find out if we're a cab, and if we need pans
        if self.catalogue.engine_quacker.is_cab_with_dedicated_trailers:
            if self.model_def.pantograph_type is not None:
                result.append(f"ih_pantograph_display/is_cab/{self.model_id}")
        # strictly we should never need both results and could return early, but eh, this also works
        return result

    @property
    def variant_group_id_root(self):
        # we keep this distinct from vehicle_family_id, to support flexibility in variant grouping
        if getattr(self.model_type_cls, "variant_group_id_root", None) is not None:
            return self.model_type_cls.variant_group_id_root
        elif getattr(self.model_type_cls, "model_id_root", None) is not None:
            return f"NAME_SUFFIX_{self.model_type_cls.model_id_root}"
        else:
            return self.model_id

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
                livery_suffix = "secondary_" + str(self.catalogue.livery_defs.index(livery_def))

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
        raise ValueError(f"variant_group_id not found for {self.model_id}")

    @cached_property
    def input_spritesheet_name_stem(self):
        # the input spritesheet name is the same for all variants of the model type
        # optional support for delegating to a spritesheet belonging to a different vehicle type (e.g. when recolouring same base pixels for different wagon types)
        if (
            getattr(self.model_type_cls, "input_spritesheet_delegate_id_root", None)
            is not None
        ):
            # CABBAGE - THIS MAY BE UNUSED
            input_spritesheet_name_stem = self.get_wagon_id(
                self.model_type_cls.input_spritesheet_delegate_id_root, self.model_def
            )
        else:
            # handle cloned cases by referring to the original producer for the path
            if self.model_def.cloned_from_model_def is not None:
                input_spritesheet_name_stem = (
                    self.model_def.cloned_from_model_def.model_id
                )
            else:
                input_spritesheet_name_stem = self.model_id

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
                utils.echo_message(self.model_id + " has no description")
            if len(self.model_def.foamer_facts) == 0:
                utils.echo_message(self.model_id + " has no foamer_facts")
            if "." in self.model_def.foamer_facts:
                utils.echo_message(self.model_id + " foamer_facts has a '.' in it.")


class Catalogue(list):
    """
    Entry point for information about a model, including
    - liveries (variants) as catalogue entries
    - some properties that aren't otherwise delegated to model_variant or model_def
    - accessors for producer, tech tree etc
    """

    def __init__(self, producer):
        self.producer = producer
        self.engine_quacker = EngineQuacker(catalogue=self)
        self.wagon_quacker = WagonQuacker(catalogue=self)
        self.clone_quacker = CloneQuacker(catalogue=self)
        self.tgv_hst_quacker = TGVHSTQuacker(catalogue=self)

    # to avoid having a very complicated __init__ we faff around with this class method, GPT reports that it's idiomatic, I _mostly_ agree
    @classmethod
    def create(cls, producer):
        instance = cls(producer)
        return instance

    def add_entries(self):
        # entry adding separated from create() as it depends on the catalogue being available to producer
        for livery_counter, livery_def in enumerate(self.livery_defs):
            model_variant_id = f"{self.producer.model_id}_mv_{livery_counter}"
            unit_variant_ids = [
                f"{model_variant_id}_unit_{i}"
                for i, _ in enumerate(self.producer.model_def.unit_defs)
            ]
            # pre-calculated numeric IDs provided for every unit
            numeric_id_offset = self.producer.model_def.base_numeric_id + (
                livery_counter * len(self.producer.model_def.unit_defs)
            )
            # note that this is the list of *unique* numeric ids - it doesn't repeat ids for repeated units
            unit_numeric_ids = [
                numeric_id_offset + i
                for i, _ in enumerate(self.producer.model_def.unit_defs)
            ]

            vehicle_family_id = self.producer.vehicle_family_id

            variant_group_id = self.producer.get_variant_group_id(
                livery_def, self.base_track_type
            )

            # certain static properties are copied into the catalogue_entry from the producer
            # this is for convenience of access as
            # - we prefer not to access producer directly from templates or graphics generation
            # - model_def is considered mostly immutable after init, and we don't want the producer extensively writing properties into model_def instances
            catalogue_entry = CatalogueEntry(
                catalogue=self,
                model_id=self.producer.model_id,
                model_variant_id=model_variant_id,
                unit_variant_ids=unit_variant_ids,
                unit_numeric_ids=unit_numeric_ids,
                livery_def=livery_def,
                vehicle_family_id=vehicle_family_id,
                variant_group_id=variant_group_id,
                input_spritesheet_name_stem=self.producer.input_spritesheet_name_stem,
            )
            self.append(catalogue_entry)

    @property
    def livery_defs(self):
        # Retrieve a list of livery definitions from various sources.
        # Liveries may be specified in either model_def or model_type_cls,
        # and can be provided in two formats:
        #
        # 1. Livery group format (2-tuples: (livery_name, index)):
        #    - Supports reordering liveries in the buy menu without reordering the spritesheet.
        #    - Used for cases such as pax and mail car liveries, common across multiple vehicle models.
        #
        #    Priority:
        #      a. model_def.livery_group_name (per-vehicle override)
        #      b. model_type_cls.livery_group_name (default)
        #
        # 2. Direct liveries (simple list):
        #    - Assumes liveries in the spritesheet are in the same order as in the buy menu.
        #    - Used for cases like engine liveries, which are unique to the vehicle model.
        #
        #    Priority:
        #      a. model_def.liveries (per-vehicle override)
        #      b. model_type_cls.liveries (default)

        if self.producer.cab_producer is not None:
            # if there's a valid cab producer, we want the liveries from that
            target_producer = self.producer.cab_producer
        else:
            target_producer = self.producer

        # liveries as group from per-vehicle override
        if target_producer.model_def.livery_group_name is not None:
            result = []
            for (
                livery_name,
                index,
            ) in target_producer.roster_providing_module.pax_mail_livery_groups[
                target_producer.model_def.livery_group_name
            ]:
                result.append(
                    iron_horse.livery_supplier.deliver(
                        livery_name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.model_id}")
            return result

        # liveries as group from class livery_group_name (default)
        if hasattr(target_producer.model_type_cls, "livery_group_name"):
            result = []
            for (
                livery_name,
                index,
            ) in target_producer.roster_providing_module.pax_mail_livery_groups[
                target_producer.model_type_cls.livery_group_name
            ]:
                result.append(
                    iron_horse.livery_supplier.deliver(
                        livery_name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.model_id}")
            return result

        # liveries directly from model_def (simple list)
        if target_producer.model_def.liveries is not None:
            result = []
            for index, name in enumerate(target_producer.model_def.liveries):
                result.append(
                    iron_horse.livery_supplier.deliver(
                        name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.model_id}")
            return result

        # liveries directly from model_type_cls
        if hasattr(target_producer.model_type_cls, "liveries"):
            result = []
            for index, name in enumerate(target_producer.model_type_cls.liveries):
                if self.wagon_quacker.quack:
                    # all default wagon liveries are recolour-only, so force relative_spriterow_num to 0
                    relative_spriterow_num = 0
                else:
                    # assume that liveries map to spriterows (common case for engines)
                    relative_spriterow_num = index
                result.append(
                    iron_horse.livery_supplier.deliver(
                        name, relative_spriterow_num=relative_spriterow_num
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.model_id}")
            return result

        # If no valid source is found, raise an error.
        raise ValueError(
            f"Unable to determine valid livery names for "
            f"{self.model_id}\n"
            f"{self.model_def}"
            f"{self.producer.cab_producer}"
        )

    @property
    def model_id(self):
        # catalogue model_id is synonymous with catalogue id, and derived from producer
        return self.producer.model_id

    @property
    def model_id_root(self):
        # convenience method
        return self.producer.model_type_cls.model_id_root

    @property
    def model_def(self):
        # convenience method
        return self.producer.model_def

    @property
    def default_entry(self):
        # provide default entry as an explicit option for consumers, not implicit
        return self[0]

    def is_default_model_variant(self, model_variant):
        return model_variant.catalogue_entry == self.default_entry

    @cached_property
    def default_model_variant_from_roster(self):
        # requires that the producer produce() method has been called
        model_variants = self.producer.roster.model_variants_by_catalogue[self.model_id][
            "model_variants"
        ]
        for model_variant in model_variants:
            if model_variant.is_default_model_variant:
                return model_variant

    @property
    def example_model_variant(self):
        # more convenient when we just want an example model_variant for templates
        return self.default_model_variant_from_roster

    @cached_property
    def cab_engine_model(self):
        # fetch a model variant for the cab, if relevant
        # only applies if cab_id is set in model_def
        # considered moving to WagonQuacker, as it's only used for wagons as of April 2025, but not sure yet (EngineQuacker is supposed to be 'is?' not 'here are...')
        if self.producer.cab_producer is None:
            return None
        return self.producer.cab_producer.catalogue.example_model_variant

    @cached_property
    def dedicated_trailer_catalogue_model_variant_mappings(self):
        # fetch dedicated trailer vehicles for this cab engine (if any)
        # this is _expected_ to fail if called too early - there won't be any wagons
        # - there's no guard against that as of April 2025, just don't it
        # considered moving to EngineQuacker, as it's only used for engines as of April 2025, but not sure yet (WagonQuacker is supposed to be 'is?' not 'here are...')
        result = []
        for (
            catalogue_id,
            catalogue_model_variant_mapping,
        ) in self.producer.roster.model_variants_by_catalogue.items():
            catalogue = catalogue_model_variant_mapping["catalogue"]
            if catalogue.model_def.cab_id == self.model_id:
                result.append(catalogue_model_variant_mapping)
        return result

    @cached_property
    def next_gen_catalogue(self):
        # note that there's just one replacement catalogue in the next gen (has to be this way for model life calculations)
        if self.engine_quacker.quack:
            return self.producer.roster.engine_model_tech_tree.get_next_gen_catalogue(
                catalogue=self
            )
        return None

    @cached_property
    def previous_gen_catalogues(self):
        # note a catalogue can replace multiple catalogues in the previous gen (as tree branches can merge)
        if self.engine_quacker.quack:
            return (
                self.producer.roster.engine_model_tech_tree.get_previous_gen_catalogues(
                    catalogue=self
                )
            )
        # empty list if nothing found
        return []

    @cached_property
    def similar_model_catalogues(self):
        if self.engine_quacker.quack:
            return (
                self.producer.roster.engine_model_tech_tree.get_similar_model_catalogues(
                    catalogue=self
                )
            )
        # empty list if nothing found
        return []

    @cached_property
    def intro_year(self):
        if self.producer.cab_producer is not None:
            return self.producer.cab_producer.catalogue.intro_year

        # automatic intro_year, but can override via model_def
        assert self.model_def.gen != None, (
            "%s has no gen value set, which is incorrect" % self.model_id
        )
        result = self.producer.roster.intro_years[self.base_track_type][
            self.model_def.gen - 1
        ]
        if self.model_def.intro_year_offset is not None:
            result = result + self.model_def.intro_year_offset
        return result

    @cached_property
    def base_track_type(self):
        if self.model_def.base_track_type is not None:
            return self.model_def.base_track_type
        else:
            return "RAIL"

    @property
    def formation_reporting_labels(self):
        # these are used for the badges that the vehicle will report *to* alt var 41 predicates
        # the predicate to check *for* is handled elsewhere
        # !! there is some degree of JFDI in this as of April 2025
        result = []
        if self.tgv_hst_quacker.is_tgv_hst_middle_part:
            result.append(
                self.tgv_hst_quacker.formation_ruleset_middle_part_equivalence_flag
            )

        # !! attr lookup like this is a sign that this might need delegated to producer properly, but eh
        if (
            getattr(self.producer.model_type_cls, "formation_reporting_labels", None)
            is not None
        ):
            result.extend(self.producer.model_type_cls.formation_reporting_labels)
        # !! adding family might have unexpected results, it's a JFDI thing
        result.append(self.producer.vehicle_family_id)
        return result

    @property
    def vehicle_family_badge(self):
        # convenience method, catalogue method is public, producer is not
        return self.producer._vehicle_family_badge

    @property
    def vehicle_family_pantograph_display_badges(self):
        # convenience method, catalogue method is public, producer is not
        return self.producer._vehicle_family_pantograph_display_badges

    @property
    def cite(self):
        # this assumes that NG and Metro always return the same, irrespective of model type cite
        # that makes sense for Pony roster, but might not work in other rosters, deal with that if it comes up eh?
        # don't like how much content (text) is in code here, but eh
        if self.model_def.base_track_type == "NG":
            cite_name = "Roberto Flange"
            cite_titles = [
                "Narrow Gauge Superintendent",
                "Works Manager (Narrow Gauge)",
                "Traction Controller, Narrow Gauge Lines",
            ]
        elif self.model_def.base_track_type == "METRO":
            cite_name = "JJ Transit"
            cite_titles = [
                "Superintendent (Metro Division)",
                "Chief Engineer, Mass Mobility Systems",
            ]
        else:
            if getattr(self.producer.model_type_cls, "cite", None) == "Arabella Unit":
                cite_name = self.producer.model_type_cls.cite
                cite_titles = [
                    "General Manager (Railcars)",
                    "Senior Engineer, Self-Propelled Traction",
                    "Director, Suburban and Rural Lines",
                ]
            elif (
                getattr(self.producer.model_type_cls, "cite", None)
                == "Dr Constance Speed"
            ):
                cite_name = self.producer.model_type_cls.cite
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


class EngineQuacker:
    """
    Utility for detecting if models
    - are engines,
    - or behave like engines in some circumstances (e.g., for docs, grouping, etc).
    """

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.producer = self.catalogue.producer

    def _validate_inverse_quacker(self, test_result):
        # the engine and wagon quackers are used to handle engine-like and wagon-like behaviour in context
        # BUT the default .quack methods should be inverse for any given catalogue, as the base behaviours are mutually exclusive
        # doing it this way prevents conceptual blur enforceably
        assert (
            self.catalogue.wagon_quacker._quack() != test_result
        ), f"{self.catalogue.model_id} quacker conflict: engine and wagon quackers both return {test_result} for .quack, their return values should be mutually inverse"

    def _quack(self):
        # simple base class check, all models are derived from one of "EngineModelTypeBase" xor "CarModelTypeBase"
        # this could have been done with an attribute on the base class, but that tends to lead to subclass overrides, which work at first, then become unmanageable
        return any(
            base.__name__ == "EngineModelTypeBase"
            for base in self.catalogue.producer.model_type_cls.__mro__
        )

    @cached_property
    def quack(self):
        # wraps _quack so we can run _validate without recursion loop
        result = self._quack()
        self._validate_inverse_quacker(result)
        return result

    @cached_property
    def availability_controlled_by_engine_param(self):
        # predicate for engines whose availability is governed by the player setting for engines availability parameter
        # *all* engines are engines
        if self._quack():
            return True
        # otherwise delegate to inversion of wagon quacker availability params
        # anything that's not a wagon for availability params is treated as an engine
        return not self.catalogue.wagon_quacker.availability_controlled_by_wagon_param

    @cached_property
    def is_cab_with_dedicated_trailers(self):
        # predicate for engines which act as cabs for dedicated trailers
        if not self._quack():
            return False
        if len(self.catalogue.dedicated_trailer_catalogue_model_variant_mappings) > 0:
            return True
        # fall through
        return False


class WagonQuacker:
    """
    Utility for detecting if models
    - are wagons,
    - or behave like wagons in some circumstances (e.g., for docs, grouping, etc).
    """

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.producer = self.catalogue.producer

    def _validate_inverse_quacker(self, test_result):
        # the engine and wagon quackers are used to handle engine-like and wagon-like behaviour in context
        # BUT the default .quack methods should be inverse for any given catalogue, as the base behaviours are mutually exclusive
        assert (
            self.catalogue.engine_quacker._quack() != test_result
        ), f"{self.catalogue.model_id} quacker conflict: engine and wagon quackers both return {test_result} for .quack, their return values should be mutually inverse"

    def _quack(self):
        # simple base class check, all models are derived from one of "EngineModelTypeBase" xor "CarModelTypeBase"
        # this could have been done with an attribute on the base class, but that tends to lead to subclass overrides, which work at first, then become unmanageable
        # doing it this way prevents conceptual blur enforceably
        return any(
            base.__name__ == "CarModelTypeBase"
            for base in self.catalogue.producer.model_type_cls.__mro__
        )

    @cached_property
    def quack(self):
        # wraps _quack so we can run _validate without recursion loop
        result = self._quack()
        self._validate_inverse_quacker(result)
        return result

    @cached_property
    def availability_controlled_by_wagon_param(self):
        # predicate for wagons whose availability is governed by the player setting for wagons availability parameter
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # wagons that are trailers for railcars etc need to match availability to their cab, so they're handled as engines
        if self.producer.cab_producer is not None:
            return False
        # fall through
        return True

    @cached_property
    def is_randomised_wagon_type(self):
        # predicate for wagons which act as randomised types
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # depends on looking up class name, but should be ok
        return any(
            base.__name__ == "RandomisedCarMixinBase"
            for base in self.producer.model_type_cls.__mro__
        )

    @cached_property
    def is_caboose(self):
        # predicate for wagons which act as caboose (or similar)
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # depends on looking up class name, but should be ok
        return any(
            base.__name__ == "GestaltGraphicsCabooseLike"
            for base in self.catalogue.example_model_variant.gestalt_graphics.__class__.__mro__
        )

    @cached_property
    def is_randomised_caboose(self):
        # predicate for wagons which act as random choice of caboose (or similar)
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # depends on looking up class name, but should be ok
        return any(
            base.__name__ == "GestaltGraphicsCabooseLikeRandomised"
            for base in self.catalogue.example_model_variant.gestalt_graphics.__class__.__mro__
        )

    @cached_property
    def is_restaurant_car(self):
        # predicate for wagons which act as caboose
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # depends on looking up class name, but should be ok
        return any(
            base.__name__ == "PassengerRestaurantCar"
            for base in self.catalogue.producer.model_type_cls.__mro__
        )

    @cached_property
    def is_pax_or_mail_car(self):
        # predicate for wagons which are pax or mail
        # if it's not a wagon at all, return early
        if self._quack() == False:
            return False
        # depends on looking up class name, but should be ok
        return any(
            base.__name__ in ["PassengerCarBase", "MailCarBase"]
            for base in self.catalogue.producer.model_type_cls.__mro__
        )


class CloneQuacker:
    """
    Utility for affordances on models that either:
    - are clones,
    - or are treated like clones (e.g., for docs, grouping, etc).
    """

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.producer = self.catalogue.producer

    @property
    def quack(self):
        # convenience boolean for things that either are clones, or can be treated like clones for docs etc
        # public access via catalogue
        if self.producer.model_def.cloned_from_model_def is not None:
            return True
        if self.producer.model_def.quacks_like_a_clone:
            return True
        if getattr(self.producer.model_type_cls, "quacks_like_a_clone", False):
            return True
        # fall through to 'does not quack like a clone'
        return False

    def _get_upstream_catalogue(self, permissive):
        if not self.quack:
            raise ValueError(
                f"{self.catalogue.model_id} does not quack like a clone, don't call clone_quacker.get_upstream_catalogue on it."
            )
        if permissive == False and self.producer.model_def.cloned_from_model_def is None:
            raise ValueError(
                f"{self.catalogue.model_id} is not a true clone, don't call clone_quacker.get_upstream_catalogue on it with permissive={permissive}"
            )
        # if it's an actual clone get the producer for the model the clone was derived from
        # possibly expensive, but not often required
        # timed ok when tested, but if slow, put a structure on roster to handle it, or pre-build the clone references in catalogue when produced
        if self.producer.model_def.cloned_from_model_def is not None:
            for candidate_catalogue in self.producer.roster.catalogues:
                if (
                    candidate_catalogue.model_def
                    == self.producer.model_def.cloned_from_model_def
                ):
                    return candidate_catalogue
        # otherwise it's a fake clone, try the vehicle family, which may be unreliable but eh
        try:
            return self.producer.roster.model_variants_by_catalogue[
                self.producer.vehicle_family_id
            ]["catalogue"]
        except (KeyError, TypeError):
            raise LookupError(
                f"Upstream catalogue not found for {self.catalogue.model_id}; "
                f"vehicle_family_id={self.producer.vehicle_family_id}"
            )

    def resolve_catalogue(self, permissive):
        # does not act like a clone, early return
        if not self.quack:
            return self.catalogue
        # we handle trains with cab engines like clones, so get the cab catalogue
        if permissive and self.producer.cab_producer is not None:
            return self.producer.cab_producer.catalogue
        return self._get_upstream_catalogue(permissive)


class TGVHSTQuacker:
    """
    Utility for affordances on models that act like TGV or HST, with dual-head cab and dedicated middle vehicles
    *Not* used for generic railcars and trailers.
    """

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.producer = self.catalogue.producer

    def _validate(self):
        # specific name format is required for TGV and HST parts
        assert (
            self.is_tgv_hst_cab != self.is_tgv_hst_middle_part
        ), f"TGVHSTQuacker: {self.catalogue.model_id} is returning true for both is_tgv_hst_cab and is_tgv_hst_middle_part"
        if self.is_tgv_hst_cab:
            assert self.catalogue.model_id.endswith(
                "_cab"
            ), f"TGVHSTQuacker: {self.catalogue.model_id} cab part must end with '_cab'"
        if self.is_tgv_hst_middle_part:
            assert self.catalogue.model_id.endswith(
                ("_middle_passenger", "middle_mail")
            ), f"TGVHSTQuacker: {self.catalogue.model_id} middle part must end with '_middle_passenger' or '_middle_mail'"

    @property
    def quack(self):
        # convenience boolean for models that are HST or TGV (dual-head cab and dedicated middle vehicles)
        if getattr(
            self.catalogue.producer.model_type_cls, "dedicated_tgv_hst_formation", False
        ):
            return True
        # fall through
        return False

    @cached_property
    def is_tgv_hst_cab(self):
        # predicate to find cabs
        if not self.quack:
            return False
        # cab parts are created before middle parts, so we can't rely on detecting middle parts for cab
        # instead we have to rely on absence of cab_producer as that can be used at init time
        if self.producer.cab_producer is None:
            return True
        # fall through
        return False

    @cached_property
    def is_tgv_hst_middle_part(self):
        # predicate to find middle_parts
        if not self.quack:
            return False
        if self.producer.cab_producer is not None:
            return True
        # fall through
        return False

    @cached_property
    def vehicle_family_id(self):
        self._validate()
        for suffix in ("_cab", "_middle_passenger", "_middle_mail"):
            if self.catalogue.model_id.endswith(suffix):
                return self.catalogue.model_id.removesuffix(suffix)

    @cached_property
    def formation_ruleset_middle_part_equivalence_flag(self):
        if not self.quack:
            return None
        return f"{self.vehicle_family_id}_middle"
