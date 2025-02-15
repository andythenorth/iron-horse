from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22170,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22180,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22190,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22200,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22210,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_1cc_filled_hopppers_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementType3",
        base_numeric_id=22220,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_def)

    return result
