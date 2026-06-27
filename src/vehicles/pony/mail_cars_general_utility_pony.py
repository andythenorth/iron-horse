from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """
    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31620,
        gen=1,
        subtype="A",
        livery_group_name="gen_1_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)
    """
    """
    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31700,
        gen=1,
        subtype="B",
        livery_group_name="gen_1_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)
    """
    """
    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=29180,
        gen=2,
        subtype="A",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=30540,
        gen=2,
        subtype="B",
        livery_group_name="gen_2_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="3_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31660,
        gen=3,
        subtype="A",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="3_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31800,
        gen=3,
        subtype="B",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=32030,
        gen=3,
        subtype="C",
        livery_group_name="gen_3_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31540,
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
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=28020,
        gen=4,
        subtype="B",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=28060,
        gen=4,
        subtype="C",
        livery_group_name="gen_4_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=31420,
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
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=28330,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailCarVanGeneralUtility",
        base_numeric_id=25740,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_greebled_32px"
    )

    result.append(model_def)

    return result
