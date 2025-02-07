from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- pony NG -------------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26420,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26430,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26440,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26460,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26470,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26480,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26490,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26500,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26510,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarCoveredRandomisedConsist",
        base_numeric_id=26520,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
