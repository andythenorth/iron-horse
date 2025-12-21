from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType4",
        base_numeric_id=29370,
        gen=1,
        subtype="aA",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType4",
        base_numeric_id=29130,
        gen=1,
        subtype="aB",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType4",
        base_numeric_id=29290,
        gen=1,
        subtype="aC",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
