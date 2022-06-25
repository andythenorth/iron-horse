from train import KaolinHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=16150,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=16160,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15970,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15980,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    # --------------- ibex ----------------------------------------------------------------------

    consist = KaolinHopperCarConsist(
        roster_id="ibex",
        base_numeric_id=8750,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="ibex",
        base_numeric_id=8780,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = KaolinHopperCarConsist(
        roster_id="ibex",
        base_numeric_id=8790,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="ibex",
        base_numeric_id=8800,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
