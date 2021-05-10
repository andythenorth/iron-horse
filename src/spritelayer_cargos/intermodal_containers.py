# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsIntermodal

import spritelayer_cargo
from spritelayer_cargo import CargoBase

from spritelayer_cargos import registered_spritelayer_cargos


class IntermodalCargo(CargoBase):
    """ Base class for container cargos """

    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    def __init__(self, **kwargs):
        self.base_id = "intermodal_containers"
        super().__init__(**kwargs)
        self.gestalt_graphics = GestaltGraphicsIntermodal()
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        self.all_platform_types_with_floor_heights = {
            "default": 0,
            "low_floor": 1,
            "cargo_sprinter": 0,
        }


class IntermodalDefaultAndLowFloorCargoBase(IntermodalCargo):
    """ Sparse base class to set compatible platform types and sprite placement template """

    # class properties, we want them available without __init__ for...reasons
    compatible_platform_types = ["default", "low_floor"]
    template_type_name = "default"


class IntermodalCargoSprinterCargoBase(IntermodalCargo):
    """ Sparse base class to set compatible platform types and sprite placement template """

    # class properties, we want them available without __init__ for...reasons
    compatible_platform_types = ["cargo_sprinter"]
    template_type_name = "cargo_sprinter"


class IntermodalFlatCar16pxStandardCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 16
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [[container_30_foot]]


class IntermodalFlatCar24pxStandardCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_20_foot, container_20_foot], [container_40_foot]]


class IntermodalFlatCar24px40FootOnlyCargo(IntermodalDefaultAndLowFloorCargoBase):
    # because some cargos / container types don't look right at 20 foot (too short)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_40_foot]]


class IntermodalFlatCar32pxStandardCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
            [container_40_foot, container_20_foot],
            [container_20_foot, container_40_foot],
        ]


class IntermodalFlatCar32pxNo40FootCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar32px30FootOnlyCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar16pxBoxCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 16
        self.variants = [
            ["box_DFLT_30_foot_1CC"],
            ["box_DFLT_30_foot_2CC"],
            ["box_DFLT_30_foot_red"],
        ]


class IntermodalFlatCar24pxBoxCargo(IntermodalDefaultAndLowFloorCargoBase):
    compatible_platform_types = ["default", "low_floor"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        self.variants = [
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_red", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_2CC"],
            ["box_DFLT_20_foot_2CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_40_foot_1CC"],
            ["box_DFLT_40_foot_2CC"],
            ["box_DFLT_40_foot_red"],
        ]


class IntermodalFlatCar32pxBoxCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        self.variants = [
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_red", "box_DFLT_20_foot_red", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_2CC", "box_DFLT_20_foot_2CC", "box_DFLT_20_foot_2CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_2CC", "box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_2CC", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_40_foot_1CC"],
            ["box_DFLT_20_foot_2CC", "box_DFLT_40_foot_1CC"],
            ["box_DFLT_20_foot_red", "box_DFLT_40_foot_red"],
            ["box_DFLT_40_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_40_foot_2CC", "box_DFLT_20_foot_2CC"],
            ["box_DFLT_40_foot_2CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_30_foot_1CC", "box_DFLT_30_foot_1CC"],
        ]


class IntermodalCargoSprinter32pxStandardCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
            [container_40_foot],
        ]


class IntermodalCargoSprinter32px20FootOnlyCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
        ]


class IntermodalCargoSprinter32px40FootOnlyCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_40_foot],
        ]


class IntermodalCargoSprinter32pxBoxCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        self.variants = [
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_2CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_red", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_40_foot_1CC"],
            ["box_DFLT_40_foot_red"],
        ]


cargo_subtype_to_subclass_mapping = {
    "box": [
        IntermodalFlatCar16pxBoxCargo,
        IntermodalFlatCar24pxBoxCargo,
        IntermodalFlatCar32pxBoxCargo,
        IntermodalCargoSprinter32pxBoxCargo,
    ],
    "bulk": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxNo40FootCargo,  # note special case for 32px
        IntermodalCargoSprinter32px20FootOnlyCargo,
    ],
    "chemicals_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "cryo_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "curtain_side": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
    "edibles_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "stake_flatrack": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
    "livestock": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "reefer": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "wood": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
}


def main():
    # first register containers with DFLT in their filename, which will be used for:
    # - for known cargos with only one visual variant
    # - specific known classes (as default, or fallback where the class might still have further cargo specific sprites)
    # - all other cargos / classes not handled explicitly, which will fall back to box
    for subtype in cargo_subtype_to_subclass_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if subtype not in [
            "bulk",
            "stake_flatrack",
        ]:
            subtype_suffix = "DFLT"
            spritelayer_cargo.register_cargo(
                cargo_subtype_to_subclass_mapping, subtype, subtype_suffix
            )

    # then register containers with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    # cargo label mapping returns "cargo_label: (subtype, subtype_suffix)"
    for subtype, subtype_suffix in set(
        GestaltGraphicsIntermodal().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            spritelayer_cargo.register_cargo(
                cargo_subtype_to_subclass_mapping, subtype, subtype_suffix
            )

    """
    # for knowing how many containers combinations we have in total
    total = 0
    for cargo in registered_spritelayer_cargos:
        total += len(cargo.variants)
    print('total variants', total)
    """
