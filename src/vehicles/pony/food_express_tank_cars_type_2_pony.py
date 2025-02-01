from train import ExpressFoodTankCarConsistType2, ExpressCar, FreightCar


def main(roster_id, **kwargs):
    result = []


    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1 for food tank cars - straight to gen 2
    """
    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17200,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17210,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17220,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17230,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28190,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28440,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16970,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28180,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")

    # gen 6A not included - could add?
    """

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=20380,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ExpressFoodTankCarConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=20390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    return result
