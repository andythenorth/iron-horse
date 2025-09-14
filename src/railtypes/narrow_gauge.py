from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="narrow_gauge",
        vehicle_track_type_name="NG",
        label="NAAN",
        base_label_in_standardised_scheme="NAAN",  # CABBAGE
        # just use the standardised label, no legacy railtype support
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=[],
        curve_speed_multiplier=1,  # small buff for narrow gauge (default value for RAIL is 0)
        sort_order=38,
        # as of May 2025, all extended labels for speed and axle load are removed, in the interests of "those are neither fun nor useful"
        # keep it simple
        compatible_railtype_list=[
            "NAAE",
        ],
        powered_railtype_list=[
            "NAAE",
        ],
        alternative_railtype_list=[],
        use_custom_sprites=True,
    )
