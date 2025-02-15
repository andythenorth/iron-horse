from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # intro gen 4

    model_def = ModelDef(
        class_name="AutomobileLowFloorCar",
        base_numeric_id=26720,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetricUnit", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileLowFloorCar",
        base_numeric_id=26730,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetricUnit", chassis="4_axle_running_gear_only_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileLowFloorCar",
        base_numeric_id=26740,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetricUnit", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileLowFloorCar",
        base_numeric_id=26750,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetricUnit", chassis="4_axle_running_gear_only_32px"
    )

    result.append(model_def)

    return result
