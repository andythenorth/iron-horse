from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=34610,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=34550,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_type_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=36610,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=16390,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=16400,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=16410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BoxCarConsistType2",
        base_numeric_id=16420,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_type_factory)

    return result
