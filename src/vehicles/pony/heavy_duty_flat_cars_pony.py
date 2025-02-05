from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21920,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="HeavyDutyCar", chassis="4_axle_ng_16px")

    result.append(model_type_factory)

    # --------------- pony -------------------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21930,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="HeavyDutyCar", chassis="4_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21940,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="HeavyDutyCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21950,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="HeavyDutyCar", chassis="4_axle_filled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FlatCarHeavyDutyConsist",
        base_numeric_id=21960,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="HeavyDutyCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    return result
