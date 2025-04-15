from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30000,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30010,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30020,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30030,
        gen=4,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30260,
        gen=4,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30040,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30050,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30060,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30070,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30080,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30090,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30100,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30110,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="2_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30140,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30150,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30160,
        gen=5,
        subtype="A",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="2_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30170,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=30180,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    return result
