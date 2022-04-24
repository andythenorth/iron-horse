from train import BoxCarGoodsConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7440,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7450,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7460,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7400,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7410,
        gen=4,
        subtype="C",
        sprites_complete=True,
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
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7430,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_1cc_filled_32px",
    )
    """
    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7420,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,

        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarGoodsConsist(
        roster_id="pony",
        base_numeric_id=7430,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_1cc_filled_32px",
    )
    """
