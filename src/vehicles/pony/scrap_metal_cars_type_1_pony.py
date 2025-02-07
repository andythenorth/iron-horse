from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    # gen 2 start eh?

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19070,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19090,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19110,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19130,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19150,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19170,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19190,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19210,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarScrapMetalConsistType1",
        base_numeric_id=19250,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
