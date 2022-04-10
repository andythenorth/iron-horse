from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="narrow_gauge",
        label="NAAN",
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        map_colour=0x25,
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
            "NAAE",
            "NABE",
            "NACE",
            "NADE",
            "NAEE",
        ],
        use_custom_sprites=True,
        alternative_railtype_list=["NABN", "NACN", "NADN", "NAEN"],
    )
    railtype.register(disabled=disabled)
