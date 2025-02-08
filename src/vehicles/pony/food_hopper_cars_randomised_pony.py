from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=19870,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=30320,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=16980,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=30290,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=17280,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=17360,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)
    """

    model_def = ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=33000,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FoodHopperCarRandomisedConsist",
        base_numeric_id=32980,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
