# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsIntermodal

from spritelayer_cargo import CargoBase


class IntermodalCargo(CargoBase):
    """ Base class for container cargos """

    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    def __init__(self, **kwargs):
        self.base_id = "intermodal_containers"
        super().__init__(**kwargs)
        self.container_subtype = kwargs.get("container_subtype", None)

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        return {"default": 0, "low_floor": 1, "cargo_sprinter": 0}

    @property
    def all_platform_types(self):
        return self.all_platform_types_with_floor_heights.keys()

    @property
    def floor_height_for_platform_type(self):
        # crude resolution of floor height for each platform type
        return self.all_platform_types_with_floor_heights[self.platform_type]

    @property
    def cargos_by_platform_type_and_length(self):
        # structure optimised for rendering into nml switch stack
        # just walking over all the cargos into a flat set of spritesets triggers the nfo / nml 255 limit for switch results, so the switches are interleaved in a specific way to avoid that
        result = {}
        for platform_type in self.all_platform_types:
            result[platform_type] = {}
            platform_lengths = [16, 24, 32]
            for platform_length in platform_lengths:
                if (platform_type, platform_length) not in suppression_list:
                    result[platform_type][platform_length] = get_cargos_matching_platform_type_and_length(platform_type, platform_length)
        return result

    @property
    def id(self):
        return (
            "intermodal_"
            + self.platform_type
            + "_"
            + self.container_subtype
            + "_"
            + str(self.length)
            + "px"
        )


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
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        self.variants = [[container_30_foot]]


class IntermodalFlatCar24pxStandardCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [[container_20_foot, container_20_foot], [container_40_foot]]


class IntermodalFlatCar24px40FootOnlyCargo(IntermodalDefaultAndLowFloorCargoBase):
    # because some cargos / container types don't look right at 20 foot (too short)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [[container_40_foot]]


class IntermodalFlatCar32pxStandardCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
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
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar32px30FootOnlyCargo(IntermodalDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
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
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
            [container_40_foot],
        ]


class IntermodalCargoSprinter32px20FootOnlyCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
        ]


class IntermodalCargoSprinter32px40FootOnlyCargo(IntermodalCargoSprinterCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
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


container_type_cargo_mapping = {
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


# this is simply manually maintained, and is to prevent nml warnings about unused switches
suppression_list = [("cargo_sprinter", 16), ("cargo_sprinter", 24)]

registered_container_cargos = []


def register_container_cargo(container_type, container_subtype):
    for cargo_type in container_type_cargo_mapping[container_type]:
        for platform_type in cargo_type.compatible_platform_types:
            cargo = cargo_type(
                container_subtype=container_subtype,
                platform_type=platform_type,
            )
            # suppression of unused cargos to prevent nml warnings further down the chain
            if (platform_type, cargo.length) not in suppression_list:
                registered_container_cargos.append(cargo)


def get_cargos_matching_platform_type_and_length(
    platform_type, platform_length
):
    result = []
    for cargo in registered_container_cargos:
        if (cargo.platform_type == platform_type) and (
            cargo.length == platform_length
        ):
            result.append(cargo)
    return result


def cargo_has_random_variants_for_cargo_label(
    platform_type, platform_length, container_subtype
):
    result = False
    for cargo in get_cargos_matching_platform_type_and_length(
        platform_type, platform_length
    ):
        if cargo.container_subtype == container_subtype:
            if len(cargo.variants) > 1:
                result = True
    return result


def get_next_cargo_switch(platform_type, platform_length, container_subtype):
    # this is solely to optimise out pointless random switches, which nml could do for us but eh, why not shave the yak :P
    if cargo_has_random_variants_for_cargo_label(
        platform_type, platform_length, container_subtype
    ):
        return (
            "switch_spritelayer_cargos_intermodal_containers_random_"
            + platform_type
            + "_"
            + str(platform_length)
            + "px_"
            + container_subtype
        )
    else:
        return (
            "switch_spritelayer_cargos_intermodal_containers_"
            + platform_type
            + "_"
            + str(platform_length)
            + "px_"
            + container_subtype
            + "_0"
        )


def main():
    # first register containers with DFLT in their filename, which will be used for:
    # - for known cargos with only one visual variant
    # - specific known classes (as default, or fallback where the class might still have further cargo specific sprites)
    # - all other cargos / classes not handled explicitly, which will fall back to box
    for container_type in container_type_cargo_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if container_type not in [
            "bulk",
            "stake_flatrack",
        ]:
            container_subtype = container_type + "_DFLT"
            register_container_cargo(container_type, container_subtype)

    # then register containers with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    for container_subtype in set(
        GestaltGraphicsIntermodal().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if "DFLT" not in container_subtype:
            container_type = container_subtype[0:-5]
            register_container_cargo(container_type, container_subtype)

    """
    # for knowing how many containers combinations we have in total
    total = 0
    for cargo in registered_container_cargos:
        total += len(cargo.variants)
    print('total variants', total)
    """
