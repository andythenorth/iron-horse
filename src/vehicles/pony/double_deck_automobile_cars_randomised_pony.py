from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="AutomobileCarDoubleDeckRandomised",
        base_numeric_id=63780,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarRandomisedUnit", chassis="empty_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileCarDoubleDeckRandomised",
        base_numeric_id=63790,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarRandomisedUnit", chassis="empty_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileCarDoubleDeckRandomised",
        base_numeric_id=4980,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarRandomisedUnit",
        chassis="empty_20px",
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarRandomisedUnit",
        chassis="empty_20px",
        rel_spriterow_index=1,
    )

    result.append(model_def)

    return result
