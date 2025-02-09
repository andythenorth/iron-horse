from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="TorpedoCarConsist",
        base_numeric_id=4140,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarConsist",
        base_numeric_id=4060,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarConsist",
        base_numeric_id=4170,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarConsist",
        base_numeric_id=4090,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_def)

    return result
