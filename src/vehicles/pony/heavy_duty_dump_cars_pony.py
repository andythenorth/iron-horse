from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarHeavyDuty",
        base_numeric_id=17110,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- pony -------------------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarHeavyDuty",
        base_numeric_id=17120,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCarUnit", chassis="4_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarHeavyDuty",
        base_numeric_id=16630,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarHeavyDuty",
        base_numeric_id=16530,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCarUnit", chassis="4_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarHeavyDuty",
        base_numeric_id=30640,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    return result
