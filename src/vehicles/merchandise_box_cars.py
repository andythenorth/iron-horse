from train import BoxCarMerchandiseConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16380,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16390,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16400,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=16420,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
