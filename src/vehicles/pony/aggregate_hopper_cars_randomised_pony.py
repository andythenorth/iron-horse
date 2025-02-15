from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=35230,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=35050,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34480,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34810,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34460,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34440,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34250,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar",
        chassis="empty_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=34230,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=20350,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarAggregateRandomised",
        base_numeric_id=21970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
