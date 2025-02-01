from train import GasTankCarPressureConsist, FreightCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25410,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25420,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_ng_sparse_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25430,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_ng_sparse_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25440,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25450,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25460,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25470,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25480,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25490,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25500,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25510,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    result.append(consist_factory)

    consist_factory = GasTankCarPressureConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25520,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    result.append(consist_factory)

    return result
