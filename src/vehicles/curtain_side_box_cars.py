from train import BoxCarCurtainSideConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # gen 4 start, only B and C lengths
    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=9580,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=9550,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=9750,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=10020,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=10480,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=10500,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
