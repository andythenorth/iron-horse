from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="rail_electrified_dc",
        label="IHF_",
        rosters=["ibex"],
        construction_cost=12,
        maintenance_cost=12,
        railtype_flags=["RAILTYPE_FLAG_CATENARY"],
        sort_order=19,
        compatible_railtype_list=[
            "IHA_",
            "IHB_",
            "RAIL",
            "ELRL",
        ],
        powered_railtype_list=[],
        alternative_railtype_list=[],
        extends_RAIL=True,
    )
