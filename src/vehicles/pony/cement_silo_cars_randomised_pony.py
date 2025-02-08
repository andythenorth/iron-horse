from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17590,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17560,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17540,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17520,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17500,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarCementRandomisedConsist",
        base_numeric_id=17480,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
