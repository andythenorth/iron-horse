from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="metro",
        vehicle_track_type_name="METRO",
        label="IHC_",
        # MTRO used, not the SAA4 standardised label, for tragedy of the commons reasons (more likely MTRO is supported by large sets)
        base_label_in_standardised_scheme="MTRO",
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=["RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        sort_order=41,
        compatible_railtype_list=[
            "MTRO",
            "SAA4",
        ],
        powered_railtype_list=[
            "MTRO",
            "SAA4",
        ],
        alternative_railtype_list=[
            "MTRO",
        ],
        use_custom_sprites=True,
        use_custom_signals=True,
    )
