from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType1",
        base_numeric_id=33400,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_ng_8px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType1",
        base_numeric_id=29150,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType1",
        base_numeric_id=29330,
        gen=1,
        subtype="aA",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType1",
        base_numeric_id=23270,
        gen=1,
        subtype="aB",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType1",
        base_numeric_id=29170,
        gen=1,
        subtype="aC",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
