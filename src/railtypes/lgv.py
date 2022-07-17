from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="lgv",
        introduction_date="1989,06,22",
        label="IHAA",
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        railtype_flags=["RAILTYPE_FLAG_HIDDEN", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        map_colour=0x25,
        sort_order=25,
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
