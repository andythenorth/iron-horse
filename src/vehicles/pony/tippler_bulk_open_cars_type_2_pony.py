from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=35900,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_sparse_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=35920,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_sparse_24px"
    )

    result.append(model_type_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27290,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27310,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27330,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27350,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_type_factory)

    # no gen 5A or 6A

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27370,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_greebled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="BulkOpenCarTipplerConsistType2",
        base_numeric_id=27390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_type_factory)

    return result
