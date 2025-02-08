from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20730,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20740,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20750,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_sparse_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20760,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_sparse_greebled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="GasTankCarCryoConsist",
        base_numeric_id=20780,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_alt_32px"
    )

    result.append(model_def)

    return result
