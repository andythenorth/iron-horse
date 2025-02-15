from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    model_def = ModelDef(
        class_name="CoilCarCovered",
        base_numeric_id=30190,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarCovered",
        base_numeric_id=30200,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarCovered",
        base_numeric_id=30210,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarCovered",
        base_numeric_id=30220,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_1cc_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarCovered",
        base_numeric_id=30230,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_1cc_filled_32px")

    result.append(model_def)

    return result
