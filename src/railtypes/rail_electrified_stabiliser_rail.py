from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)

def main(disabled=False):
    return Railtype(
        id="rail_electrified_stabiliser_rail",
        label="IHH_",
        rosters=["horse"],
        construction_cost=12,
        maintenance_cost=12,
        # this is a hidden railtype for vehicle cross-compatibility
        railtype_flags=["RAILTYPE_FLAG_HIDDEN"],
        sort_order=19,
        compatible_railtype_list=[
            "IHA_",
            "RAIL",
        ],
        powered_railtype_list=[
            "SAA3"
        ],
        alternative_railtype_list=[],
        extends_RAIL=True,
    )
