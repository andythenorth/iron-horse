from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG -------------------------------------------------------------------

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=25850,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=25820,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=23710,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27080,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27090,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27100,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27110,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27130,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27180,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PieceGoodsCombosMixedRandomised",
        base_numeric_id=27150,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
