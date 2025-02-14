from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="TankCarStandardConsistType2",
        base_numeric_id=35100,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_sparse_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarStandardConsistType2",
        base_numeric_id=33050,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarStandardConsistType2",
        base_numeric_id=37000,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
