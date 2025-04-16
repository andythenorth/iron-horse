from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony --------------------------------------------------------------------------

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=35450,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=35460,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=25980,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26050,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26150,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26190,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26220,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsBoxCarType2",
        base_numeric_id=26340,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
