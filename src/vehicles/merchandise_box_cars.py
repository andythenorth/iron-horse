from train import BoxCarMerchandiseConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7300,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7310,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7320,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7330,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7340,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7350,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7360,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7370,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7380,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
    """
    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7390,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7400,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
    """
