from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # no NG express cars in pony, use mail car

    # --------------- standard gauge ---------------------------------------------------------------

    #     model_def = ModelDef(
    #         schema_name="ExpressCarType2",
    #         base_numeric_id=18800,
    #         gen=1,
    #         subtype="A",
    #         sprites_complete=True,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="ExpressCarUnit",
    #         suppress_roof_sprite=True,  # non-standard roof for this wagon
    #         chassis="3_axle_solid_express_16px",
    #     )
    #
    #     result.append(model_def)
    #
    #     model_def = ModelDef(
    #         schema_name="ExpressCarType2",
    #         base_numeric_id=19620,
    #         gen=2,
    #         subtype="A",
    #         sprites_complete=True,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="ExpressCarUnit",
    #         suppress_roof_sprite=True,  # non-standard roof for this wagon
    #         chassis="3_axle_solid_express_16px",
    #     )
    #
    #     result.append(model_def)
    #
    #     model_def = ModelDef(
    #         schema_name="ExpressCarType2",
    #         base_numeric_id=19660,
    #         gen=2,
    #         subtype="B",
    #         sprites_complete=True,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="ExpressCarUnit",
    #         suppress_roof_sprite=True,  # non-standard roof for this wagon
    #         chassis="4_axle_solid_express_24px",
    #     )
    #
    #     result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=22760,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=22800,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_24px",
    )

    result.append(model_def)

    #     model_def = ModelDef(
    #         schema_name="ExpressCarType2",
    #         base_numeric_id=25870,
    #         gen=3,
    #         subtype="C",
    #         sprites_complete=True,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="ExpressCarUnit",
    #         suppress_roof_sprite=True,  # non-standard roof for this wagon
    #         chassis="4_axle_solid_express_32px",
    #     )
    #
    #     result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=26210,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=26290,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=33060,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=18720,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_greebled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressCarType2",
        base_numeric_id=17330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_32px",
    )

    result.append(model_def)

    return result
