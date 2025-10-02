from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=19120,
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
        base_numeric_id=19140,
        gen=3,
        subtype="A",
        base_track_type="NG",
        livery_group_name="gen_3_ng_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=19160,
        gen=3,
        subtype="B",
        base_track_type="NG",
        livery_group_name="gen_3_ng_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=19180,
        gen=4,
        subtype="A",
        base_track_type="NG",
        livery_group_name="gen_4_ng_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17450,
        gen=4,
        subtype="B",
        base_track_type="NG",
        livery_group_name="gen_4_ng_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=21170,
        gen=4,
        subtype="C",
        base_track_type="NG",
        livery_group_name="gen_4_ng_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="4_axle_ng_32px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17470,
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
        base_numeric_id=17490,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17510,
        gen=2,
        subtype="A",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17530,
        gen=2,
        subtype="B",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17550,
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
        base_numeric_id=17750,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17910,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17930,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="2_axle_solid_pax_mail_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=17950,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=18030,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=18050,
        gen=5,
        subtype="A",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="2_axle_solid_pax_mail_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=18110,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailCar",
        base_numeric_id=18130,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    return result
