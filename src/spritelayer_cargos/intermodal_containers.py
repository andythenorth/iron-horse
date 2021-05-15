# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsIntermodal

from spritelayer_cargo import SpritelayerCargo, CargoSetBase


class IntermodalSpritelayerCargo(SpritelayerCargo):
    """ Base class for the containers spritelayer cargo """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_id = "intermodal_containers"
        self.gestalt_graphics = GestaltGraphicsIntermodal()

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        return {
            "default": 0,
            "low_floor": 1,
            "cargo_sprinter": 0,
        }


class IntermodalCargoSet(CargoSetBase):
    """ Base class for container cargo sets """

    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gestalt_graphics = GestaltGraphicsIntermodal()


class IntermodalDefaultAndLowFloorCargoSetBase(IntermodalCargoSet):
    """ Sparse base class to set compatible platform types and sprite placement template """

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default", "low_floor"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class IntermodalCargoSprinterCargoSetBase(IntermodalCargoSet):
    """ Sparse base class to set compatible platform types and sprite placement template """

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["cargo_sprinter"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "cargo_sprinter"


class IntermodalFlatCar16pxStandardCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [[container_30_foot]]


class IntermodalFlatCar24pxStandardCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_20_foot, container_20_foot], [container_40_foot]]


class IntermodalFlatCar24px40FootOnlyCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    # because some cargos / container types don't look right at 20 foot (too short)

    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [[container_40_foot]]


class IntermodalFlatCar32pxStandardCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
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


class IntermodalFlatCar32pxNo40FootCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar32px30FootOnlyCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_30_foot = self.subtype + "_" + self.subtype_suffix + "_30_foot"
        self.variants = [
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar16pxBoxCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        self.variants = [
            ["box_DFLT_30_foot_1CC"],
            ["box_DFLT_30_foot_2CC"],
            ["box_DFLT_30_foot_red"],
        ]


class IntermodalFlatCar24pxBoxCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
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


class IntermodalFlatCar32pxBoxCargoSet(IntermodalDefaultAndLowFloorCargoSetBase):
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


class IntermodalCargoSprinter32pxStandardCargoSet(IntermodalCargoSprinterCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
            [container_40_foot],
        ]


class IntermodalCargoSprinter32px20FootOnlyCargoSet(
    IntermodalCargoSprinterCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_20_foot = self.subtype + "_" + self.subtype_suffix + "_20_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
        ]


class IntermodalCargoSprinter32px40FootOnlyCargoSet(
    IntermodalCargoSprinterCargoSetBase
):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        container_40_foot = self.subtype + "_" + self.subtype_suffix + "_40_foot"
        self.variants = [
            [container_40_foot],
        ]


class IntermodalCargoSprinter32pxBoxCargoSet(IntermodalCargoSprinterCargoSetBase):
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
        IntermodalFlatCar16pxBoxCargoSet,
        IntermodalFlatCar24pxBoxCargoSet,
        IntermodalFlatCar32pxBoxCargoSet,
        IntermodalCargoSprinter32pxBoxCargoSet,
    ],
    "bulk": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxNo40FootCargoSet,  # note special case for 32px
        IntermodalCargoSprinter32px20FootOnlyCargoSet,  # special case
    ],
    "chemicals_tank": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "cryo_tank": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "curtain_side": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24px40FootOnlyCargoSet,  # special case
        IntermodalFlatCar32px30FootOnlyCargoSet,  # special case
        IntermodalCargoSprinter32px40FootOnlyCargoSet,  # special case
    ],
    "edibles_tank": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "stake_flatrack": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24px40FootOnlyCargoSet,  # special case
        IntermodalFlatCar32px30FootOnlyCargoSet,  # special case
        IntermodalCargoSprinter32px40FootOnlyCargoSet,  # special case
    ],
    "livestock": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "reefer": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "tank": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24pxStandardCargoSet,
        IntermodalFlatCar32pxStandardCargoSet,
        IntermodalCargoSprinter32pxStandardCargoSet,
    ],
    "wood": [
        IntermodalFlatCar16pxStandardCargoSet,
        IntermodalFlatCar24px40FootOnlyCargoSet,  # special case
        IntermodalFlatCar32px30FootOnlyCargoSet,  # special case
        IntermodalCargoSprinter32px40FootOnlyCargoSet,  # special case
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
                    spritelayer_cargo_type=IntermodalSpritelayerCargo,
                )
    # then register containers with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    # cargo label mapping returns "cargo_label: (subtype, subtype_suffix)"
    for subtype, subtype_suffix in set(
        GestaltGraphicsIntermodal().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=IntermodalSpritelayerCargo,
                )
