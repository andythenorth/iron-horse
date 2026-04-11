from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=24820,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=26260,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=25790,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=26310,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=25810,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=24820,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_32px",
    )

    result.append(model_def)
    """

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=32040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=32050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
