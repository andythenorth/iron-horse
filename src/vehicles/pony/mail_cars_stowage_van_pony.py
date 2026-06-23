from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MailCarVanStowage",
        base_numeric_id=29030,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=32320,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=31720,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=27840,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=27890,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=28100,
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
        schema_name="MailCarVanStowage",
        base_numeric_id=28160,
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
