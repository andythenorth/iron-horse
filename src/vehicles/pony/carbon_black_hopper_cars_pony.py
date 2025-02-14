from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="CarbonBlackHopperCarConsist",
        base_numeric_id=21870,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CarbonBlackHopperCarConsist",
        base_numeric_id=21880,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CarbonBlackHopperCarConsist",
        base_numeric_id=21890,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CarbonBlackHopperCarConsist",
        base_numeric_id=21900,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="CarbonBlackHopperCarConsist",
        base_numeric_id=21910,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
