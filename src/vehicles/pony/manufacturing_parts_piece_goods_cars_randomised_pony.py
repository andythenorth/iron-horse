from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarManufacturingPartsRandomisedConsist",
        base_numeric_id=24540,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarManufacturingPartsRandomisedConsist",
        base_numeric_id=24550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarManufacturingPartsRandomisedConsist",
        base_numeric_id=24560,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarManufacturingPartsRandomisedConsist",
        base_numeric_id=24570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PieceGoodsCarManufacturingPartsRandomisedConsist",
        base_numeric_id=24580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
