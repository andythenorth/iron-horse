# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import (
    GestaltGraphicsIntermodalContainerTransporters,
)

from spritelayer_cargo import SpritelayerCargo, CargoSetBase


class IntermodalContainersSpritelayerCargo(SpritelayerCargo):
    """Base class for the containers spritelayer cargo"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_id = "intermodal_containers"
        self.gestalt_graphics = GestaltGraphicsIntermodalContainerTransporters(liveries=None)
        self.provide_container_shadows = True

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        return {
            "default": 0,
            "low_floor": 1,
            "cargo_sprinter": 0,
        }


class DefaultAndLowFloorIntermodalContainersCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default", "low_floor"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class CargoSprinterIntermodalContainersCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["cargo_sprinter"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "cargo_sprinter"


class FlatCar16pxStandardIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [[container_30_foot]]


class FlatCar24pxStandardIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_20_foot, container_20_foot], [container_40_foot]]


class FlatCar24px40FootOnlyIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    # because some cargos / container types don't look right at 20 foot (too short)

    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_40_foot]]


class FlatCar32pxStandardIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
            [container_40_foot, container_20_foot],
            [container_20_foot, container_40_foot],
        ]


class FlatCar32pxNo40FootIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
        ]


class FlatCar32px30FootOnlyIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_30_foot, container_30_foot],
        ]


class FlatCar16pxBoxIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        self.variants = [
            ["box_DFLT_30_foot_1CC"],
            ["box_DFLT_30_foot_2CC"],
            ["box_DFLT_30_foot_red"],
        ]


class FlatCar24pxBoxIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
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


class FlatCar32pxBoxIntermodalContainersCargoSet(
    DefaultAndLowFloorIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
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


class CargoSprinter32pxStandardIntermodalContainersCargoSet(
    CargoSprinterIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
            [container_40_foot],
        ]


class CargoSprinter32px20FootOnlyIntermodalContainersCargoSet(
    CargoSprinterIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
        ]


class CargoSprinter32px40FootOnlyIntermodalContainersCargoSet(
    CargoSprinterIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_40_foot],
        ]


class CargoSprinter32pxBoxIntermodalContainersCargoSet(
    CargoSprinterIntermodalContainersCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_2CC"],
            ["box_DFLT_20_foot_1CC", "box_DFLT_20_foot_red"],
            ["box_DFLT_20_foot_red", "box_DFLT_20_foot_1CC"],
            ["box_DFLT_40_foot_1CC"],
            ["box_DFLT_40_foot_red"],
        ]


subtype_to_cargo_set_mapping = {
    "box": [
        FlatCar16pxBoxIntermodalContainersCargoSet,
        FlatCar24pxBoxIntermodalContainersCargoSet,
        FlatCar32pxBoxIntermodalContainersCargoSet,
        CargoSprinter32pxBoxIntermodalContainersCargoSet,
    ],
    "bulk": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxNo40FootIntermodalContainersCargoSet,  # note special case for 32px
        CargoSprinter32px20FootOnlyIntermodalContainersCargoSet,  # special case
    ],
    "chemicals_tank": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "cryo_tank": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "curtain_side": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24px40FootOnlyIntermodalContainersCargoSet,  # special case
        FlatCar32px30FootOnlyIntermodalContainersCargoSet,  # special case
        CargoSprinter32px40FootOnlyIntermodalContainersCargoSet,  # special case
    ],
    "edibles_tank": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "stake_flatrack": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24px40FootOnlyIntermodalContainersCargoSet,  # special case
        FlatCar32px30FootOnlyIntermodalContainersCargoSet,  # special case
        CargoSprinter32px40FootOnlyIntermodalContainersCargoSet,  # special case
    ],
    "livestock": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "reefer": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "tank": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24pxStandardIntermodalContainersCargoSet,
        FlatCar32pxStandardIntermodalContainersCargoSet,
        CargoSprinter32pxStandardIntermodalContainersCargoSet,
    ],
    "wood": [
        FlatCar16pxStandardIntermodalContainersCargoSet,
        FlatCar24px40FootOnlyIntermodalContainersCargoSet,  # special case
        FlatCar32px30FootOnlyIntermodalContainersCargoSet,  # special case
        CargoSprinter32px40FootOnlyIntermodalContainersCargoSet,  # special case
    ],
}


def main():
    # first register containers with DFLT in their filename, which will be used for:
    # - for known cargos with only one visual variant
    # - specific known classes (as default, or fallback where the class might still have further cargo specific sprites)
    # - all other cargos / classes not handled explicitly, which will fall back to box
    for subtype in subtype_to_cargo_set_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if subtype not in [
            "bulk",
            "stake_flatrack",
        ]:
            subtype_suffix = "DFLT"
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=IntermodalContainersSpritelayerCargo,
                )
    # then register containers with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    # cargo label mapping returns "cargo_label: (subtype, subtype_suffix)"
    for subtype, subtype_suffix in set(
        GestaltGraphicsIntermodalContainerTransporters(liveries=None).cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=IntermodalContainersSpritelayerCargo,
                )
