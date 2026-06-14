from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    """
    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=17530,
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
        base_numeric_id=17550,
        gen=3,
        subtype="A",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=17750,
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
        base_numeric_id=17910,
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
        base_numeric_id=17930,
        gen=4,
        subtype="A",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="2_axle_solid_pax_mail_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=17950,
        gen=4,
        subtype="B",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=31800,
        gen=4,
        subtype="C",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_32px"
    )

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=18050,
        gen=5,
        subtype="A",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="2_axle_solid_pax_mail_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=18110,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarRandomised",
        base_numeric_id=31620,
        gen=5,
        subtype="C",
        #livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="empty_32px"
    )

    result.append(model_def)
    """
    return result
