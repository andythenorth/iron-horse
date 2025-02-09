from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21920,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- pony -------------------------------------------------------------------------

    model_def = ModelDef(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21930,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCar", chassis="4_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21940,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCar", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21950,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCar", chassis="4_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21960,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="HeavyDutyCar", chassis="4_axle_filled_24px")

    result.append(model_def)

    return result
