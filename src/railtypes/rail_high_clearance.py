from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="rail_high_clearance",
        label="IHAB",
        rosters=["ibex", "moose", "pony"],
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=[],
        sort_order=8,
        compatible_railtype_list=[],
        powered_railtype_list=[],
        alternative_railtype_list=[],
        extends_RAIL=True,
    )
