from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=16440,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=24530,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=26450,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=24490,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=24500,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=21200,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=30450,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=22150,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=30620,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarHopperCombos",
        base_numeric_id=27280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
