from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=36220,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_spine_16px"
    )

    result.append(model_type_factory)

    # no gen 2 for NG, straight to gen 3

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=36230,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_spine_16px"
    )

    result.append(model_type_factory)

    """ # restore in next version

    model_type_factory =ModelTypeFactory(
        class_name="LogCarConsist",
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=36240,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_spine_16px")

    result.append(model_type_factory)
    """
    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=31780,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=31770,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=31790,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=30750,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=31800,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=30970,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=31810,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="LogCarConsist",
        base_numeric_id=26050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_type_factory)

    return result
