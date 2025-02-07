from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=25700,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=25720,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31300,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31160,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31180,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31200,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31220,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31240,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31020,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31040,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TankCarAcidRandomisedConsist",
        base_numeric_id=31280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
