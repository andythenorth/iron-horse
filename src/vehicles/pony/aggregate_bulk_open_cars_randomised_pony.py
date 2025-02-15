from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34810,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34460,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34440,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=34250,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        chassis="empty_32px",
    )

    result.append(model_def)
    """

    model_def = ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=32040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarAggregateRandomised",
        base_numeric_id=32050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
