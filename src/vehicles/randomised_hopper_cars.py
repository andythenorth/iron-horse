from train import HopperCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7820,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, vehicle_length=4)

    # no new type A for gen 2, gen 1 type A continues

    consist = HopperCarRandomisedConsist(
        roster_id="pony", base_numeric_id=7840, gen=3, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7850,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony", base_numeric_id=7860, gen=4, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7870,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7890,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7900,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7910,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = HopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7920,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
