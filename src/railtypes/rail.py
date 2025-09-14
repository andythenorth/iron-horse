from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="rail",
        vehicle_track_type_name="RAIL",
        label="RAIL",
        non_standardised_rtt_fallback_labels=["RAIL"],
        rosters=["pony", "ibex", "moose"],
        construction_cost=None,
        maintenance_cost=None,
        railtype_flags=[],
        sort_order=None,
        # compatible and powered not set, this railtype is just for setting vehicle track_type in compile
        compatible_railtype_list=[],
        powered_railtype_list=[],
        alternative_railtype_list=[],
        suppress_for_nml=True,
    )
