from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # just type gen 4 and 5

    model_def = ModelDef(
        class_name="HopperCarMGRTopHood",
        base_numeric_id=20230,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarMGRTopHood",
        base_numeric_id=36280,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarMGRTopHood",
        base_numeric_id=20250,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="HopperCarMGRTopHood",
        base_numeric_id=36300,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    return result
