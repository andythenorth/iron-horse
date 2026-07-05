from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28940,
        gen=1,
        subtype="A",
        livery_group_name="gen_1_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=29580,
        gen=1,
        subtype="B",
        livery_group_name="gen_1_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28930,
        gen=2,
        subtype="A",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28900,
        gen=2,
        subtype="B",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28920,
        gen=3,
        subtype="A",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=29050,
        gen=3,
        subtype="B",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28910,
        gen=3,
        subtype="C",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=27780,
        gen=4,
        subtype="A",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=29320,
        gen=4,
        subtype="B",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28210,
        gen=4,
        subtype="C",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=24510,
        gen=5,
        subtype="A",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=28360,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=24520,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_32px"
    )

    result.append(model_def)

    return result
