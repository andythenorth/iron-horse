# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from spritelayer_cargo import SpritelayerCargo, CargoSetBase
import polar_fox


class DropCentreSpritelayerCargo(SpritelayerCargo):
    """
    Base class for drop centre spritelayer cargo - machinery, vehicles etc.
    Also includes 'normal' flatbed cargos.
    Uses spritelayers for:
    - cargo randomisation
    - asymmetry
    - positioning: 'long' cargos are full length of vehicle, 'tall' or 'heavy' cargos are centred in well
    """

    base_id = "drop_centre"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cargo_sprite_provider = "default"
        # these sprites can be asymmetric
        self.cargo_sprites_are_asymmetric = True

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        # the origin was set up for intermodal cars, at solebar height, so standard automobiles actually need shifted up 1px, hence -1
        return {
            "default": 0,
        }

    @classmethod
    def get_cargo_label_mapping(cls):
        # class method so we can call it when we don't have an instance of the class in scope
        # the base class also has an @property accessor for this for consistency with other uses
        result = {}
        # see intermodal for example of how this mapped containers
        # for vehicles this maybe just needs to switch e.g on cargo subtype or something - trucks, cars etc
        return result


class DropCentreCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class Tarps24pxCargoSet(DropCentreCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [
            [
                "tarps_grey_1_20_foot",
            ],
        ]


class Tarps32pxCargoSet(DropCentreCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            [
                "tarps_grey_1_24_foot",
            ],
        ]


subtype_to_cargo_set_mapping = {
    "tarps_grey": [
        Tarps24pxCargoSet,
        Tarps32pxCargoSet,
    ],
    # "trucks": [
    #    Trucks16pxCargoSet,
    #    Trucks20pxCargoSet,
    #    Trucks24pxCargoSet,
    #    Trucks32pxCargoSet,
    # ],
}


def main(spritelayer_cargo_manager):
    spritelayer_cargo_cls = DropCentreSpritelayerCargo
    # Pass 1: register default (DFLT) variants
    # - used when a cargo has no specific visual variant
    # - acts as fallback for partially-defined cargo types
    # - some subtypes are excluded because they are always cargo-specific
    for subtype in subtype_to_cargo_set_mapping.keys():
        subtype_suffix = "DFLT"
        for spritelayer_cargo_set_cls in subtype_to_cargo_set_mapping[subtype]:
            spritelayer_cargo_manager.add_cargo_set(
                spritelayer_cargo_set_cls,
                spritelayer_cargo_cls,
                subtype,
                subtype_suffix,
            )

    # Pass 2: register cargo-specific variants (e.g. cars_VEHI, trucks_ENSP)
    # mapping returns (subtype, subtype_suffix) pairs
    # DFLT entries are skipped here as they are handled above
    for subtype, subtype_suffix in set(
        spritelayer_cargo_cls.get_cargo_label_mapping().values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_cls in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_manager.add_cargo_set(
                    spritelayer_cargo_set_cls,
                    spritelayer_cargo_cls,
                    subtype,
                    subtype_suffix,
                )
