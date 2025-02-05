from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    # Pony NG uses railbus trailers, not railcar

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 3 could be added but needs the engine grilles replacing with pax car pixels

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=17130,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="slammer",
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=26060,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="geronimo",
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=27170,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="tin_rocket",
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=25140,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="breeze",
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=25580,
        gen=6,
        subtype="U",
        cab_id="happy_train",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="PassengerRailcarTrailerCarConsist",
        base_numeric_id=25400,
        gen=6,
        subtype="U",
        cab_id="zeus",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_type_factory)

    return result
