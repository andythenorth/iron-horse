from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)

# unelectrifed LGV is a *hidden* compatibility railtype to ensure LGV capable but unelectrified HSTs etc can travel on LGV

def main(disabled=False):
    return Railtype(
        id="lgv",
        vehicle_track_type_name="LGV",
        introduction_date="1989,06,22",
        label="HAAN",
        base_label_in_standardised_scheme="HAAN", # CABBAGE - just don't bother with standardised scheme here?
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        # this is a hidden railtype for vehicle cross-compatibility
        railtype_flags=["RAILTYPE_FLAG_HIDDEN"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=25,
        is_lgv_railtype=True,
        compatible_railtype_list=[
            "IHA_",
            "IHB_",
            "IHBA",
            "RAIL",
            "ELRL",
        ],
        powered_railtype_list=[
            "IHA_",
            "IHB_",
            "IHBA",
            "RAIL",
            "ELRL",
        ],
        use_custom_sprites=False,
        alternative_railtype_list=[],
    )
