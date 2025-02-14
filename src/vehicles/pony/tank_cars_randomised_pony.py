from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=37020,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=32900,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=32940,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35900,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35920,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35940,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)
    """

    model_def = ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35960,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarStandardRandomisedConsist",
        base_numeric_id=35280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
