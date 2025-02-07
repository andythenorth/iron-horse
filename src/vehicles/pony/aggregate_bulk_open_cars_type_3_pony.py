from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarAggregateConsistType3",
        base_numeric_id=32060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarAggregateConsistType3",
        base_numeric_id=32070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_32px"
    )

    result.append(model_def)

    return result
