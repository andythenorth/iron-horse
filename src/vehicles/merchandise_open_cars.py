from train import OpenCarMerchandiseConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7210,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7220,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7230,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7240,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7250,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7260,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7270,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_16px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7280,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7290,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
    # no gen 6 as of March 2022, keep gen 5 around for appearance reasons
    """
    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7300,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=7310,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
    """
