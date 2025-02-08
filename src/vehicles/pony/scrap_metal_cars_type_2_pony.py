from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32120,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32160,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_gapped_greebled_32px")

    result.append(model_def)

    return result
