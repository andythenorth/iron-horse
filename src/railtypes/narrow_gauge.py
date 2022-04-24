from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="narrow_gauge",
        label="IHD_",
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        map_colour=0x25,
        # assumes compatible with all axle weights and speeds for narrow gauge rail in standardised scheme
        compatible_railtype_list=[
            "NABN",
            "NACN",
            "NADN",
            "NAEN",
            "NAAE",
            "NABE",
            "NACE",
            "NADE",
            "NAEE",
        ],
        powered_railtype_list=[
            "NABN",
            "NACN",
            "NADN",
            "NAEN",
        ],
        use_custom_sprites=True,
        alternative_railtype_list=["NABN", "NACN", "NADN", "NAEN"],
    )
    railtype.register(disabled=disabled)
