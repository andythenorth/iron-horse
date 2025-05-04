from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=26600,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_chute_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=26660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=19990,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=17190,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=25010,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodProductsHopperCarType2",
        base_numeric_id=26580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
