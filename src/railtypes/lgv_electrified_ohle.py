from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="lgv_electrified_ohle",
        vehicle_track_type_name="LGV_ELECTRIFIED_OHLE",
        # H is not a type in in the standardised scheme as of Sept 2025, but we're using it anyway, yolo
        label="LGVE",
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        railtype_flags=["RAILTYPE_FLAG_CATENARY", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=26,
        is_lgv_railtype=True,
        # compatible and powered are minimal following https://github.com/OpenTTD/OpenTTD/pull/14357
        # TGVs can go on ELRL etc, but this is via the vehicle track_type
        compatible_railtype_list=[
            "LGVN",
            "IHA_",  # legacy Horse - needed for railtype grfs that supported Horse?
            "IHB_",  # legacy Horse - needed for railtype grfs that supported Horse?
        ],
        powered_railtype_list=[
            "IHB_",  # legacy Horse - needed for railtype grfs that supported Horse?
        ],
        alternative_railtype_list=[],
        use_custom_sprites=True,
    )
