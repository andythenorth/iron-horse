from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64380,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64390,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64400,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64410,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64420,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarCryoType3",
        base_numeric_id=64430,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
