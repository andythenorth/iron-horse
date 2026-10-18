from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63670,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63660,
        gen=2,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63650,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63640,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63620,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63610,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MachineryCarRandomised",
        base_numeric_id=63600,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="MachineryCarAsymmetricUnit", chassis="empty_32px")

    result.append(model_def)

    return result
