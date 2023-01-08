from train import FlatCarPlateConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10520,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no gen 2A, gen 1A continues in pony

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10530,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10540,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10580,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10630,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10590,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10510,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10880,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10840,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FlatCarPlateConsist(
        roster_id="pony",
        base_numeric_id=10910,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
