from train import BoxCarGoodsConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16480,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16490,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16500,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16440,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16450,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_filled_32px",
    )

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16460,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16470,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16460,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,

        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarGoodsConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16470,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_1cc_filled_32px",
    )
    """
