from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=26650,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="OreDumpCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=26670,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="OreDumpCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=35550,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="OreDumpCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=32260,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="OreDumpCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    # no gen 5A or 6A

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=35570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="OreDumpCarUnit", chassis="4_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarTipplerRotaryType1",
        base_numeric_id=32280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="OreDumpCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
