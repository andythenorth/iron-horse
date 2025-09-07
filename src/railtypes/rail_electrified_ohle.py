from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="rail_electrified_ohle",
        vehicle_track_type_name="RAIL_ELECTRIFIED_OHLE",
        label="ELRL",
        base_label_in_standardised_scheme="ELRL", # CABBAGE - just don't bother with standardised scheme here?
        non_standardised_rtt_fallback_labels=["ELRL"],
        rosters=["pony", "ibex", "moose"],
        suppress_for_nml=True,
        construction_cost=None,
        maintenance_cost=None,
        railtype_flags=[],
        sort_order=None,
        compatible_railtype_list=[],
        powered_railtype_list=[],
        alternative_railtype_list=[],
    )
