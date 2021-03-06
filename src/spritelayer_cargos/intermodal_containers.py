# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into gestalt graphics, global constants, train.py etc

from gestalt_graphics.pipelines import GenerateCompositedIntermodalContainers
from gestalt_graphics.gestalt_graphics import GestaltGraphicsIntermodal


class IntermodalContainerGestalt(object):
    """ Base class for container gestalts """

    # a gestalt is a set of containers of specific length and appearance
    # each set corresponds to a spritesheet which will be generated by the graphics processor
    # each set is used for a specific group of cargo labels or classes
    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    # ====== #
    # each container set may have one or more spriterows
    # spriterows are chosen randomly when vehicles load new cargo
    # rows are composed by the graphics processor, and may include variations for
    # - combinations of container lengths
    # - combinations of container types
    # - container colours
    # !!! containers are going to need 'base sets' to allow double stack, cropped for well cars etc
    # !!! the consist needs to encode the set type to fetch the right spritesets
    # !!! base sets will also have to be encoded in gestalts here, unless they're done by (sets * gestalts) combinatorially?
    def __init__(self, **kwargs):
        self.pipeline = GenerateCompositedIntermodalContainers()
        self.container_subtype = kwargs.get("container_subtype", None)
        self.platform_type = kwargs.get("platform_type", None)

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


class IntermodalBaseDefaultAndLowFloor(IntermodalContainerGestalt):
    """ Sparse base class to set compatible platform types and sprite placement template """

    # class properties, we want them available without __init__ for...reasons
    compatible_platform_types = ["default", "low_floor"]
    template_type_name = "default"


class IntermodalBaseCargoSprinter(IntermodalContainerGestalt):
    """ Sparse base class to set compatible platform types and sprite placement template """

    # class properties, we want them available without __init__ for...reasons
    compatible_platform_types = ["cargo_sprinter"]
    template_type_name = "cargo_sprinter"


class IntermodalFlatCar16pxStandard(IntermodalBaseDefaultAndLowFloor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 16
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        self.variants = [[container_30_foot]]


class IntermodalFlatCar24pxStandard(IntermodalBaseDefaultAndLowFloor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [[container_20_foot, container_20_foot], [container_40_foot]]


class IntermodalFlatCar24px40FootOnly(IntermodalBaseDefaultAndLowFloor):
    # because some cargos / container types don't look right at 20 foot (too short)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [[container_40_foot]]


class IntermodalFlatCar32pxStandard(IntermodalBaseDefaultAndLowFloor):
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


class IntermodalFlatCar32pxNo40Foot(IntermodalBaseDefaultAndLowFloor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        self.variants = [
            [container_20_foot, container_20_foot, container_20_foot],
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar32px30FootOnly(IntermodalBaseDefaultAndLowFloor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_30_foot = kwargs.get("container_subtype") + "_30_foot"
        self.variants = [
            [container_30_foot, container_30_foot],
        ]


class IntermodalFlatCar16pxBox(IntermodalBaseDefaultAndLowFloor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 16
        self.variants = [
            ["box_DFLT_30_foot_1CC"],
            ["box_DFLT_30_foot_2CC"],
            ["box_DFLT_30_foot_red"],
        ]


class IntermodalFlatCar24pxBox(IntermodalBaseDefaultAndLowFloor):
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


class IntermodalFlatCar32pxBox(IntermodalBaseDefaultAndLowFloor):
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


class IntermodalCargoSprinter32pxStandard(IntermodalBaseCargoSprinter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
            [container_40_foot],
        ]


class IntermodalCargoSprinter32px20FootOnly(IntermodalBaseCargoSprinter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_20_foot = kwargs.get("container_subtype") + "_20_foot"
        self.variants = [
            [container_20_foot, container_20_foot],
        ]


class IntermodalCargoSprinter32px40FootOnly(IntermodalBaseCargoSprinter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        container_40_foot = kwargs.get("container_subtype") + "_40_foot"
        self.variants = [
            [container_40_foot],
        ]


class IntermodalCargoSprinter32pxBox(IntermodalBaseCargoSprinter):
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


def get_container_gestalts_by_length(vehicle_length):
    result = []
    for container_gestalt in registered_container_gestalts:
        if container_gestalt.length == 4 * vehicle_length:
            result.append(container_gestalt)
    return result


container_type_gestalt_mapping = {
    "box": [
        IntermodalFlatCar16pxBox,
        IntermodalFlatCar24pxBox,
        IntermodalFlatCar32pxBox,
        IntermodalCargoSprinter32pxBox,
    ],
    "bulk": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxNo40Foot,  # note special case for 32px
        IntermodalCargoSprinter32px20FootOnly,
    ],
    "chemicals_tank": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "cryo_tank": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "curtain_side": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24px40FootOnly,  # note special case for 24px
        IntermodalFlatCar32px30FootOnly,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnly,
    ],
    "edibles_tank": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "stake_flatrack": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24px40FootOnly,  # note special case for 24px
        IntermodalFlatCar32px30FootOnly,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnly,
    ],
    "livestock": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "reefer": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "tank": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24pxStandard,
        IntermodalFlatCar32pxStandard,
        IntermodalCargoSprinter32pxStandard,
    ],
    "wood": [
        IntermodalFlatCar16pxStandard,
        IntermodalFlatCar24px40FootOnly,  # note special case for 24px
        IntermodalFlatCar32px30FootOnly,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnly,
    ],
}


# this is simply manually maintained, and is to prevent nml warnings about unused switches
suppression_list = [("cargo_sprinter", 16), ("cargo_sprinter", 24)]

registered_container_gestalts = []


def register_container_gestalt(container_type, container_subtype):
    for gestalt_type in container_type_gestalt_mapping[container_type]:
        for platform_type in gestalt_type.compatible_platform_types:
            gestalt = gestalt_type(
                container_subtype=container_subtype,
                platform_type=platform_type,
            )
            # suppression of unused gestalts to prevent nml warnings further down the chain
            if (platform_type, gestalt.length) not in suppression_list:
                registered_container_gestalts.append(gestalt)


def get_container_gestalts_matching_platform_type_and_length(
    platform_type, platform_length
):
    result = []
    for gestalt in registered_container_gestalts:
        if (gestalt.platform_type == platform_type) and (
            gestalt.length == platform_length
        ):
            result.append(gestalt)
    return result


def gestalt_has_random_variants_for_cargo_label(
    platform_type, platform_length, container_subtype
):
    result = False
    for gestalt in get_container_gestalts_matching_platform_type_and_length(
        platform_type, platform_length
    ):
        if gestalt.container_subtype == container_subtype:
            if len(gestalt.variants) > 1:
                result = True
    return result


def get_next_cargo_switch(platform_type, platform_length, container_subtype):
    # this is solely to optimise out pointless random switches, which nml could do for us but eh, why not shave the yak :P
    if gestalt_has_random_variants_for_cargo_label(
        platform_type, platform_length, container_subtype
    ):
        return (
            "switch_spritelayer_cargos_intermodal_cars_random_"
            + platform_type
            + "_"
            + str(platform_length)
            + "px_"
            + container_subtype
        )
    else:
        return (
            "switch_spritelayer_cargos_intermodal_cars_"
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
    for container_type in container_type_gestalt_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if container_type not in [
            "bulk",
            "stake_flatrack",
        ]:
            container_subtype = container_type + "_DFLT"
            register_container_gestalt(container_type, container_subtype)

    # then register containers with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    for container_subtype in set(
        GestaltGraphicsIntermodal().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if "DFLT" not in container_subtype:
            container_type = container_subtype[0:-5]
            register_container_gestalt(container_type, container_subtype)

    """
    # for knowing how many containers combinations we have in total
    total = 0
    for gestalt in registered_container_gestalts:
        total += len(gestalt.variants)
    print('total variants', total)
    """
