from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="metro",
        vehicle_track_type_name="METRO",
        label="IHC_",
        # power assumes generic metro is 3rd rail, should be fine, just a game
        base_label_in_standardised_scheme = "YAA3",
        non_standardised_rtt_fallback_labels = ["MTRO"],
        rosters=["ibex", "moose", "pony"],
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=["RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        sort_order=41,
        compatible_railtype_list=[
            "MTRO",
        ],
        powered_railtype_list=["MTRO"],
        alternative_railtype_list=[
            "MTRO",
        ],
        use_custom_sprites=True,
        use_custom_signals=True,
    )
