from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="lgv_electrified_ohle",
        vehicle_track_type_name="LGV_ELECTRIFIED_OHLE",
        # H is not a type in in the standardised scheme as of Sept 2025, but we're using it anyway, yolo
        label="HAAE",
        base_label_in_standardised_scheme="HAAE",  # CABBAGE - just don't bother with standardised scheme here?
        # we don't fallback to RAIL or ELRL for LGV, because
        # (1) LGV is a specific type, if it's not in the game, these trains don't appear
        # (2) it causes the speed switch to return the higher value on RAIL or ELRL due to fallback, which is confusing and unwanted
        # there's no practical way to support a corner case where player has both disabled IH railtypes and not loaded an appropriate railtype grf
        # whilst railtype_available can handle the behaviour, the buy menu text is way too complicated to make more conditional
        non_standardised_rtt_fallback_labels=[],
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        railtype_flags=["RAILTYPE_FLAG_CATENARY", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=26,
        is_lgv_railtype=True,
        # TGVs can go on ELRL etc, but this won't allow RAIL / ELRL onto the TGV tracks
        compatible_railtype_list=[
            "HAAN",
            "IHA_", # legacy Horse - needed for railtype grfs that supported Horse?
            "IHB_", # legacy Horse - needed for railtype grfs that supported Horse?
            "RAIL",
            "ELRL",
        ],
        # templates for generating variations of standard railtype labels
        extend_compatible_railtype_list=["S*AN", "S*AE"],
        powered_railtype_list=[
            "IHB_", # legacy Horse - needed for railtype grfs that supported Horse?
            "ELRL",
        ],
        # templates for generating variations of standard railtype labels
        extend_powered_railtype_list=["S*AE"],
        use_custom_sprites=True,
        alternative_railtype_list=[],
    )
