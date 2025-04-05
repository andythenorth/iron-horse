import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import random
import copy
from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional
from functools import cached_property

from train import model_type as model_type_module
from train import unit as unit_module

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
    base_track_type_name: Optional[str] = None
    variant_group_id: Optional[str] = None
    cab_id: Optional[str] = None
    decor_spriterow_num: Optional[int] = None
    default_livery_extra_docs_examples: List[Any] = None # CABBAGE - DOES THIS DO ANYTHNG CURRENTLY? - *SHOULD* BE USED BY vehicle_details_engine
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
    replacement_model_id: Optional[str] = None
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
    quacks_like_a_clone: bool = False
    requires_high_clearance: bool = False
    show_decor_in_purchase_for_variants: List[Any] = None
    spriterow_labels: Optional[Any] = None
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

    # CABBAGE DOCUMENT
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
    It aggregates properties derived from model_def and computed by the factory, ensuring
    consumers can access necessary data without referencing the factory directly.
    """

    catalogue: "Catalogue"
    model_id: str
    model_variant_id: str
    unit_variant_ids: List[str]
    unit_numeric_ids: List[int]
    livery_def: "LiveryDef"
    variant_group_id: str
    input_spritesheet_name_stem: str

    @property
    def index(self):
        # convenience function
        return self.catalogue.index(self)


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
        if len(self.catalogue) == 0:
            raise Exception(
                f"{self.model_id}\n" f"ModelVariantFactory catalogue is empty"
            )

    def produce(self, catalogue_entry=None):

        if catalogue_entry == None:
            raise BaseException(
                "no catalogue_index passed for ModelVariantFactory; model_def is "
                + str(self.model_type_cls)
            )

        # CABBAGE FAILS WITH CLONES - HAX TO RESOLVE, THIS SHOULD ALREADY BE FIGURED OUT BY THE CLONE THOUGH
        # CHECK if variant_group_id is already set?  If it is, leave it alone?
        # can this not be done when cloning?
        if self.model_def.cloned_from_model_def is not None:
            self.model_def.variant_group_id = (
                self.model_def.cloned_from_model_def.model_id
            )

        model_variant = self.model_type_cls(
            factory=self,
            catalogue_entry=catalogue_entry,
        )

        # orchestrate addition of units
        for counter, unit_def in enumerate(self.model_def.unit_defs):
            try:
                unit_cls = getattr(unit_module, unit_def.class_name)
            except:
                raise Exception(
                    "class_name not found for "
                    + self.model_def.model_id
                    + ", "
                    + unit_def.class_name
                )
            # CABBAGE - this is delegating to model_variant currently, by passing unit classes, we want to pass actual units from here, model variant knows too much
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
        return getattr(model_type_module, self.class_name)

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
        # handled by model variant factory not model variant, better this way
        # special case NG - extend this for other track_types as needed
        # 'normal' rail and 'elrail' doesn't require an id modifier
        if model_def.base_track_type_name == "NG":
            base_id = model_id_root + "_ng"
        elif model_def.base_track_type_name == "METRO":
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
    def cab_factory(self):
        # convenience way to get cab factory
        if self.model_def.cab_id is not None:
            return self.roster.model_variants_by_catalogue[self.model_def.cab_id]['catalogue'].factory
        else:
            return None

    def get_variant_group_id(self, livery_def, base_track_type_name):
        # cascade of sources for variant group ID

        # group trailers with their cabs
        if self.cab_factory is not None:
            return self.cab_factory.model_id

        # force a variant group via model def
        if self.model_def.variant_group_id is not None:
            return self.model_def.variant_group_id

        # primarily used for explcitly selected wagon groups (from a class property on the model type)
        if self.model_type_cls.group_as_wagon:
            if getattr(self.model_type_cls, "variant_group_id_root", None) is not None:
                variant_group_id_root = self.model_type_cls.variant_group_id_root
            else:
                variant_group_id_root = self.model_id
            # we split groups for random and static liveries (group nesting will then be determined by roster)
            livery_selection = "random" if len(livery_def.colour_set_names or []) > 1 else "static"
            return (
                f"{variant_group_id_root}_"
                f"{base_track_type_name.lower()}_"
                f"gen_{self.model_def.gen}{self.model_def.subtype}_"
                f"{livery_selection}"
            )

        # default is to group all variants from this catalogue together
        return self.model_id


    @cached_property
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
            # handle cloned cases by referring to the original factory for the path
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


class Catalogue(list):
    """
    CABBAGE - METADATA ABOUT ALL AVAILABLE MODEL VARIANTS
        # all available model variants, with ids, numeric ids etc
        # ordered by livery index
    """

    def __init__(self, factory):
        self.factory = factory

    # to avoid having a very complicated __init__ we faff around with this class method, GPT reports that it's idiomatic, I _mostly_ agree
    @classmethod
    def create(cls, factory):
        instance = cls(factory)
        for livery_counter, livery_def in enumerate(instance.livery_defs):
            model_variant_id = f"{instance.factory.model_id}_mv_{livery_counter}"
            unit_variant_ids = [
                f"{model_variant_id}_unit_{i}"
                for i, _ in enumerate(instance.factory.model_def.unit_defs)
            ]
            # pre-calculated numeric IDs provided for every unit
            numeric_id_offset = instance.factory.model_def.base_numeric_id + (
                livery_counter * len(instance.factory.model_def.unit_defs)
            )
            # note that this is the list of *unique* numeric ids - it doesn't repeat ids for repeated units
            unit_numeric_ids = [
                numeric_id_offset + i
                for i, _ in enumerate(instance.factory.model_def.unit_defs)
            ]

            variant_group_id = factory.get_variant_group_id(livery_def, instance.base_track_type_name)

            # certain static properties are copied into the catalogue_entry from the factory
            # this is for convenience of access as
            # - we prefer not to access factory directly from templates or graphics generation
            # - model_def is considered mostly immutable after init, and we don't want the factory extensively writing properties into model_def instances
            catalogue_entry = CatalogueEntry(
                catalogue=instance,
                model_id=factory.model_id,
                model_variant_id=model_variant_id,
                unit_variant_ids=unit_variant_ids,
                unit_numeric_ids=unit_numeric_ids,
                livery_def=livery_def,
                variant_group_id=variant_group_id,
                input_spritesheet_name_stem=factory.input_spritesheet_name_stem,
            )
            instance.append(catalogue_entry)
        return instance

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

        if self.factory.cab_factory is not None:
            # if there's a valid cab factory, we want the liveries from that
            target_factory = self.factory.cab_factory
        else:
            target_factory = self.factory

        # liveries as group from per-vehicle override
        if target_factory.model_def.livery_group_name is not None:
            result = []
            for (
                livery_name,
                index,
            ) in target_factory.roster_providing_module.pax_mail_livery_groups[
                target_factory.model_def.livery_group_name
            ]:
                result.append(
                    iron_horse.livery_supplier.deliver(
                        livery_name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.factory.model_id}")
            return result

        # liveries as group from class livery_group_name (default)
        if hasattr(target_factory.model_type_cls, "livery_group_name"):
            result = []
            for (
                livery_name,
                index,
            ) in target_factory.roster_providing_module.pax_mail_livery_groups[
                target_factory.model_type_cls.livery_group_name
            ]:
                result.append(
                    iron_horse.livery_supplier.deliver(
                        livery_name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.factory.model_id}")
            return result

        # liveries directly from model_def (simple list)
        if target_factory.model_def.liveries is not None:
            result = []
            for index, name in enumerate(target_factory.model_def.liveries):
                result.append(
                    iron_horse.livery_supplier.deliver(
                        name, relative_spriterow_num=index
                    )
                )
            if len(result) == 0:
                raise ValueError(f"no liveries found for {self.factory.model_id}")
            return result

        # liveries directly from model_type_cls
        if hasattr(target_factory.model_type_cls, "liveries"):
            result = []
            for index, name in enumerate(target_factory.model_type_cls.liveries):
                if target_factory.model_type_cls.is_wagon_for_docs:
                    # all default wagon liveries are recolour-only, so force relative_spriterow_num to 0
                    # slight abuse of is_wagon_for_docs to force this - add another cls attr to wagon model type if needed
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
                raise ValueError(f"no liveries found for {self.factory.model_id}")
            return result

        # If no valid source is found, raise an error.
        raise ValueError(
            f"Unable to determine valid livery names for "
            f"{self.factory.model_id}\n"
            f"{self.factory.model_def}"
            f"{self.factory.cab_factory}"
        )

    @property
    def id(self):
        return self.factory.model_id

    @property
    def default_entry(self):
        # provide default entry as an explicit option for consumers, not implicit
        return self[0]

    def is_default_model_variant(self, model_variant):
        return model_variant.catalogue_entry == self.default_entry

    @cached_property
    def default_model_variant_from_roster(self):
        # requires that the factory produce() method has been called
        model_variants = self.factory.roster.model_variants_by_catalogue[self.id]['model_variants']
        for model_variant in model_variants:
            if model_variant.is_default_model_variant:
                return model_variant

    @cached_property
    def dedicated_trailer_catalogue_model_variant_mappings(self):
        # fetch dedicated trailer vehicles for this cab engine (if any)
        result = []
        for catalogue_id, catalogue_model_variant_mapping in self.factory.roster.model_variants_by_catalogue.items():
            catalogue = catalogue_model_variant_mapping['catalogue']
            if catalogue.factory.model_def.cab_id == self.id:
                result.append(catalogue_model_variant_mapping)
        return result

    @cached_property
    def intro_year(self):
        # automatic intro_year, but can override via model_def
        assert self.factory.model_def.gen != None, (
            "%s has no gen value set, which is incorrect" % self.factory.model_id
        )
        result = self.factory.roster.intro_years[self.base_track_type_name][
            self.factory.model_def.gen - 1
        ]
        if self.factory.model_def.intro_year_offset is not None:
            result = result + self.factory.model_def.intro_year_offset
        return result

    @cached_property
    def base_track_type_name(self):
        if self.factory.model_def.base_track_type_name is not None:
            return self.factory.model_def.base_track_type_name
        else:
            return "RAIL"

    @property
    def cite(self):
        # this assumes that NG and Metro always return the same, irrespective of model type cite
        # that makes sense for Pony roster, but might not work in other rosters, deal with that if it comes up eh?
        # don't like how much content (text) is in code here, but eh
        if self.factory.model_def.base_track_type_name == "NG":
            cite_name = "Roberto Flange"
            cite_titles = [
                "Narrow Gauge Superintendent",
                "Works Manager (Narrow Gauge)",
                "Traction Controller, Narrow Gauge Lines",
            ]
        elif self.factory.model_def.base_track_type_name == "METRO":
            cite_name = "JJ Transit"
            cite_titles = [
                "Superintendent (Metro Division)",
                "Chief Engineer, Mass Mobility Systems",
            ]
        else:
            if getattr(self.factory.model_type_cls, "cite", None) == "Arabella Unit":
                cite_name = self.factory.model_type_cls.cite
                cite_titles = [
                    "General Manager (Railcars)",
                    "Senior Engineer, Self-Propelled Traction",
                    "Director, Suburban and Rural Lines",
                ]
            elif getattr(self.factory.model_type_cls, "cite", None) == "Dr Constance Speed":
                cite_name = self.factory.model_type_cls.cite
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
        cloned_model_def.variant_group_id = model_def.model_id
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
