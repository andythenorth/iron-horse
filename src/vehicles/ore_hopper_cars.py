from train import HopperCarOreConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=14960,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=14970,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=14980,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    # also just type A for gen 1, 2 and 3

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=14740,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1 also covers gen 2

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13150,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13430,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13160,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13170,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13420,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13180,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=13190,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
