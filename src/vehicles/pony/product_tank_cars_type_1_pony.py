from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=23970,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=22380,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=26280,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="3_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=25760,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=17960,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=23490,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=17370,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=27240,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_sparse_greebled_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=16950,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=17060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarProductConsistType1",
        base_numeric_id=28220,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_sparse_greebled_32px")

    result.append(model_def)

    return result
