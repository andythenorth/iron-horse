from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalRandomised",
        base_numeric_id=32180,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalRandomised",
        base_numeric_id=32200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarScrapMetalRandomised",
        base_numeric_id=32220,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
