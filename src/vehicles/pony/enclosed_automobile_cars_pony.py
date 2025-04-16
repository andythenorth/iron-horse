from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=20820,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=18000,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=34420,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=18010,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=34430,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileEnclosedCar",
        base_numeric_id=18060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
