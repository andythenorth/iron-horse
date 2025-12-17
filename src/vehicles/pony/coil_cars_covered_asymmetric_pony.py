from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    model_def = ModelDef(
        schema_name="CoilCarCoveredAsymmetric",
        base_numeric_id=23320,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="CoilCarAsymmetricUnit", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarCoveredAsymmetric",
        base_numeric_id=29850,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="CoilCarAsymmetricUnit", chassis="4_axle_filled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarCoveredAsymmetric",
        base_numeric_id=23340,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="CoilCarAsymmetricUnit", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarCoveredAsymmetric",
        base_numeric_id=34820,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="CoilCarAsymmetricUnit", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
