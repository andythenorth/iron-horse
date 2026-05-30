from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalType3",
        base_numeric_id=29010,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalType3",
        base_numeric_id=29160,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalType3",
        base_numeric_id=30440,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
