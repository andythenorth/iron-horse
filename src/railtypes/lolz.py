from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="lolz",
        label="LOLZ",
        construction_cost=5,
        maintenance_cost=7,
        railtype_flags=["RAILTYPE_FLAG_CATENARY"],
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
        use_custom_sprites=False,
        alternative_railtype_list=[],
    )
    railtype.register(disabled=disabled)
