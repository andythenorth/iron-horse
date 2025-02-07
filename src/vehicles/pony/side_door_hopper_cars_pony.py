from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=22500,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_sparse_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=22520,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_ng_sparse_24px"
    )

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=31450,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="3_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=35250,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=35350,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="3_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=35880,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=32020,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarSideDoorConsist",
        base_numeric_id=35390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_sparse_32px"
    )

    result.append(model_def)

    return result
