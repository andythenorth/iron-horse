from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="rail",
        vehicle_track_type_name="RAIL",
        label="RAIL",
        base_label_in_standardised_scheme="RAIL",  # CABBAGE - just don't bother with standardised scheme here?
        non_standardised_rtt_fallback_labels=["RAIL"],
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
