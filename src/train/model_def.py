import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import copy
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class ModelDef:
    # Required fields (lexically sorted)
    schema_name: str
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

    unit_cls_name: str
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
