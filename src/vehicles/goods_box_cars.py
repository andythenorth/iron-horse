from train import BoxCarGoodsConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    """
    # only type A for gen 1

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7300,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7310,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7320,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7330,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7340,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")
    """
    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7400,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7410,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,

        chassis="4_axle_filled_32px",
    )

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7420,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,

        chassis="2_axle_filled_24px",
    )

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7430,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,

        chassis="4_axle_filled_32px",
    )
