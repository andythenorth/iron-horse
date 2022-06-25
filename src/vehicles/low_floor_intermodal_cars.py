from train import IntermodalLowFloorCarConsist, IntermodalCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14450,
        gen=5,
        subtype="A",
        sprites_complete=True,
        consist_ruleset="1_unit_sets",  # special case for single unit low-floor intermodals (they're PFAs eh)
    )

    consist.add_unit(type=IntermodalCar, chassis="2_axle_1cc_low_floor_16px")

    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14460,
        gen=5,
        subtype="B",
        sprites_complete=True,
        consist_ruleset="2_unit_sets",  # special case for 2 unit low-floor intermodals (they're FLAs eh)
    )
    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_low_floor_24px")

    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14470,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_low_floor_32px")

    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14480,
        gen=6,
        subtype="A",
        sprites_complete=True,
        consist_ruleset="1_unit_sets",  # special case for single unit low-floor intermodals (they're PFAs eh)
    )

    consist.add_unit(type=IntermodalCar, chassis="2_axle_1cc_low_floor_16px")

    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14490,
        gen=6,
        subtype="B",
        sprites_complete=True,
        consist_ruleset="2_unit_sets",  # special case for 2 unit low-floor intermodals (they're FLAs eh)
    )
    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_low_floor_24px")

    consist = IntermodalLowFloorCarConsist(
        roster_id="pony",
        base_numeric_id=14500,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_low_floor_32px")
