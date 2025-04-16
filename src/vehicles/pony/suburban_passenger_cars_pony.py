from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    # no NG suburban cars in pony

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1, the capacity difference is negligible compared to standard pax

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19200,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19220,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19240,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19260,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19930,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="6_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=19950,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=20240,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=20370,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=20830,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=20850,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerSuburbanCar",
        base_numeric_id=20870,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_solid_express_32px")

    result.append(model_def)

    return result
