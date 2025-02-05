from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25930,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        intro_year_offset=20,  # these are pushed right back to line up with standard gauge versions
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25940,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25950,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_type_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25960,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25970,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=25980,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=26220,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=26930,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=34520,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=34210,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarMillConsistType2",
        base_numeric_id=30830,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_type_factory)

    return result
