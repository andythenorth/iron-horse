from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="lolz",
        label="LOLZ",
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        map_colour=0x25,
        compatible_railtype_list=[
            "RAIL",
            "ELRL",
            "CATZ",
        ],
        powered_railtype_list=[
            "ELRL",
            "CATZ",
        ],
        use_custom_sprites=False,
        alternative_railtype_list=["CATZ"],
    )
    railtype.register(disabled=disabled)
