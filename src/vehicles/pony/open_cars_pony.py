from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- metro -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=980,
        gen=1,
        subtype="U",
        base_track_type_name="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_metro_16px", repeat=2
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=20370,
        gen=2,
        subtype="U",
        base_track_type_name="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_metro_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=20270,
        gen=3,
        subtype="U",
        base_track_type_name="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_metro_32px")

    result.append(model_def)

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=29890,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26090,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26100,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=29860,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=29870,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=29880,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26110,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26130,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26140,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_filled_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26150,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarConsist",
        base_numeric_id=26170,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(model_def)

    return result
