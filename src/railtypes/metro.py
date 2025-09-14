from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="metro",
        vehicle_track_type_name="METRO",
        # MTRO used, because metro is not equivalent to either SAA3 or SAA4 standardised labels - it's a specific type unrepresented in the standardised scheme
        label="MTRO",
        base_label_in_standardised_scheme="MTRO",
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=["RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        sort_order=41,
        # compatible and powered are minimal following https://github.com/OpenTTD/OpenTTD/pull/14357
        compatible_railtype_list=[],
        powered_railtype_list=[],
        alternative_railtype_list=[],
        use_custom_sprites=True,
        use_custom_signals=True,
    )
