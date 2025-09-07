from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="lgv",
        vehicle_track_type_name="LGV",
        introduction_date="1989,06,22",
        label="IHAA",
        base_label_in_standardised_scheme="HAAN", # CABBAGE - just don't bother with standardised scheme here?
        # we don't fallback to RAIL or ELRL for LGV, because
        # (1) LGV is a specific type, if it's not in the game, these trains don't appear
        # (2) it causes the speed switch to return the higher value on RAIL or ELRL due to fallback, which is confusing and unwanted
        # there's no practical way to support a corner case where player has both disabled IH railtypes and not loaded an appropriate railtype grf
        # whilst railtype_available can handle the behaviour, the buy menu text is way too complicated to make more conditional
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        # this is a hidden railtype for vehicle cross-compatibility
        railtype_flags=["RAILTYPE_FLAG_HIDDEN", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=25,
        is_lgv_railtype=True,
        # TGVs can go on ELRL etc, but this won't allow RAIL / ELRL onto the TGV tracks
        # !! might wanna automate extending these with compatible types, via resolving the global constants table or something for all compatibility?
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
