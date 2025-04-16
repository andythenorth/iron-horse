from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="TorpedoCarUnit",
        base_numeric_id=490,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarUnit",
        base_numeric_id=90,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarUnit",
        base_numeric_id=15190,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TorpedoCarUnit",
        base_numeric_id=15230,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=6)

    model_def.add_unit_def(class_name="TorpedoCarUnit", vehicle_length=3)

    result.append(model_def)

    return result
