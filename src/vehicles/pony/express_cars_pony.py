from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # no NG express cars in pony, use mail car

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=17900,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=18100,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=30360,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=17920,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=18120,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=34710,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=30600,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="2_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=17940,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=30660,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=24290,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="2_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=18020,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressCarConsist",
        base_numeric_id=18040,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ExpressCar", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    return result
