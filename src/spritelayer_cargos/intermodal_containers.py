# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from spritelayer_cargo import SpritelayerCargo, CargoSetBase
import polar_fox

class IntermodalContainersSpritelayerCargo(SpritelayerCargo):
    """Base class for the containers spritelayer cargo"""

    base_id = "intermodal_containers"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # we need both reversed states for asymmetric cargo sprinter cab units; due to existing implementation it's easier to provide that for all intermodal cargos
        self.supported_reverse_states = ["unreversed", "reversed"]
        self.provide_container_shadows = True

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        return {
            "default": 0,
            "low_floor": 1,
            "cargo_sprinter_cab_unreversed": 0,
            "cargo_sprinter_cab_reversed": 0,
        }

    @classmethod
    def allow_adding_cargo_label(cls, cargo_label, container_type, result):
        # don't ship DFLT as actual cargo label, it's not a valid cargo and will cause nml to barf
        # the generation of the DFLT container sprites is handled separately without using cargo_label_mapping
        if cargo_label == "DFLT":
            return False
        # explicit control over contested cargo_labels, by specifying which container type should be used (there can only be one type for label based support)
        if cargo_label in polar_fox.constants.container_contested_cargo_labels.keys():
            if (
                container_type
                == polar_fox.constants.container_contested_cargo_labels[cargo_label]
            ):
                return True
            else:
                return False
        # print a note if an unhandled contested cargo is found, so the contested cargos can be updated to handle the cargo label
        if cargo_label in result:
            print(
                "IntermodalContainersSpritelayerCargo.cargo_label_mapping: cargo_label",
                cargo_label,
                "already exists, being over-written by",
                container_type,
                "label; update polar_fox.constants.container_contested_cargo_labels",
            )
        # default to allowing, most cargos aren't contested
        return True

    @classmethod
    def get_cargo_label_mapping(cls):
        # class method so we can call it when we don't have an instance of the class in scope
        # the base class also has an @property accessor for this for consistency with other uses
        result = {}
        for (
            container_type,
            cargo_maps,
        ) in polar_fox.constants.container_recolour_cargo_maps:
            # first handle the cargos as explicitly refittable
            # lists of explicitly refittable cargos are by no means *all* the cargos refittable to for a type
            # nor does explicitly refittable cargos have 1:1 mapping with cargo-specific graphics
            # the mapping expected by spritelayer cargos is cargo_label: (subtype, subtype_suffix)
            # these will all map cargo_label: (container_type, DFLT)
            for cargo_label in cargo_maps[0]:
                if cls.allow_adding_cargo_label(cargo_label, container_type, result):
                    result[cargo_label] = (container_type, "DFLT")

            # then insert or override entries with cargo_label: (container_type, [CARGO_LABEL]) where there are explicit graphics for a cargo
            for cargo_label, recolour_map in cargo_maps[1]:
                if cls.allow_adding_cargo_label(cargo_label, container_type, result):
                    result[cargo_label] = (container_type, cargo_label)
        # special handling of flatracks with visible cargo sprites
        for cargo_list in polar_fox.constants.container_piece_cargo_maps.values():
            for cargo_label in cargo_list:
                if cls.allow_adding_cargo_label(cargo_label, "stake_flatrack", result):
                    result[cargo_label] = ("stake_flatrack", cargo_label)
        return result

class DefaultAndLowFloorIntermodalContainersCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default", "low_floor"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class CargoSprinterIntermodalContainersCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = [
            "cargo_sprinter_cab_unreversed",
            "cargo_sprinter_cab_reversed",
        ]
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
        IntermodalContainersSpritelayerCargo.get_cargo_label_mapping().values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=IntermodalContainersSpritelayerCargo,
                )
