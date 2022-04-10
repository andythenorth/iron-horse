from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="catz",
        label="CATZ",
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        map_colour=0x25,
        compatible_railtype_list=[
            "RAIL",
            "ELRL",
        ],
        powered_railtype_list=[
            "ELRL",
        ],
        use_custom_sprites=False,
        alternative_railtype_list=[],
    )
    railtype.register(disabled=disabled)
