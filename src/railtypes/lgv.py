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
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        # this is a hidden railtype for vehicle cross-compatibility
        railtype_flags=["RAILTYPE_FLAG_HIDDEN"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=25,
        is_lgv_railtype=True,
        # compatible and powered are minimal following https://github.com/OpenTTD/OpenTTD/pull/14357
        compatible_railtype_list=[
            "HAAE",
            "IHA_",  # legacy Horse - needed for railtype grfs that supported Horse?
            "IHB_",  # legacy Horse - needed for railtype grfs that supported Horse?
            "IHBA",  # legacy Horse - needed for railtype grfs that supported Horse?
        ],
        powered_railtype_list=[
            "HAAE",
            "IHA_",  # legacy Horse - needed for railtype grfs that supported Horse?
            "IHB_",  # legacy Horse - needed for railtype grfs that supported Horse?
            "IHBA",  # legacy Horse - needed for railtype grfs that supported Horse?
        ],
        alternative_railtype_list=[],
        use_custom_sprites=False,
    )
