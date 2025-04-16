from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=22500,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=22520,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=31450,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="3_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=31790,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=29950,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="3_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=29930,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=32020,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarSideDoor",
        base_numeric_id=30090,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_sparse_32px")

    result.append(model_def)

    return result
