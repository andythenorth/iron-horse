from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="narrow_gauge",
        label="IHD_",
        rosters=["ibex", "moose", "pony"],
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        curve_speed_multiplier=1, # small bufff for narrow gauge (default value for RAIL is 0)
        sort_order=38,
        # assumes compatible with all axle weights and speeds for narrow gauge rail in standardised scheme
        compatible_railtype_list=[
            "NAAN",
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
            "NAAN",
            "NABN",
            "NACN",
            "NADN",
            "NAEN",
        ],
        use_custom_sprites=True,
        alternative_railtype_list=["NAAN", "NABN", "NACN", "NADN", "NAEN"],
    )
