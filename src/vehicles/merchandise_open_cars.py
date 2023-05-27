from train import OpenCarMerchandiseConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16290,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16300,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16310,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_16px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
