from railtype import Railtype

# it's known that diagonal rails are broken for compatible railtypes in OpenTTD - https://github.com/OpenTTD/OpenTTD/issues/9850
# using this anyway, in the hope that 9850 gets fixed (works fine in JGRPP)


def main(disabled=False):
    return Railtype(
        id="lgv_electrified_ac",
        label="IHBA",
        base_label_in_standardised_scheme = "HAAA",
        rosters=["ibex", "moose", "pony"],
        construction_cost=16,
        maintenance_cost=16,
        railtype_flags=["RAILTYPE_FLAG_CATENARY", "RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        curve_speed_multiplier=1.66,  # decimal value seems to work?  I expected int would be required, but eh.
        sort_order=26,
        # TGVs can go on ELRL etc, but this won't allow RAIL / ELRL onto the TGV tracks
        compatible_railtype_list=[
            "IHA_",
            "IHB_",
            "RAIL",
            "ELRL",
        ],
        powered_railtype_list=[
            "IHB_",
            "ELRL",
        ],
        use_custom_sprites=True,
        # fallback for unelectrified LGV which is hidden in-game and allows non-electric TGV-style trains onto LGV routes
        alternative_railtype_list=["IHAA"],
    )
