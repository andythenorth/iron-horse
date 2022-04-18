from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="lolz",
        introduction_date="1999,06,22",
        label="LOLZ",
        construction_cost=16,
        maintenance_cost=16,
        railtype_flags=["RAILTYPE_FLAG_CATENARY", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        map_colour=0x25,
        # TGVs can go on ELRL etc, but this won't allow RAIL / ELRL onto the TGV tracks
        compatible_railtype_list=[
            "RAIL",
            "ELRL",
            "CATZ",
        ],
        powered_railtype_list=[
            "ELRL",
            "CATZ",
        ],
        extends_RAIL=True,
        extends_ELRL=True,
        use_custom_sprites=True,
        alternative_railtype_list=[],
    )
    railtype.register(disabled=disabled)
