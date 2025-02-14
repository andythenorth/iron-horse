from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18160,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18180,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18200,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18220,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18140,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="3_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18240,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18670,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="3_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18260,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=30710,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=18280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="LivestockCarConsist",
        base_numeric_id=7160,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    model_def.add_unit_def(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=2,
    )

    result.append(model_def)

    return result
