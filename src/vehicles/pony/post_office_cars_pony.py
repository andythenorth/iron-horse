from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MailPostOfficeCar",
        base_numeric_id=30380,
        gen=1,
        subtype="U",
        livery_group_name="gen_1_pax_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        # CABBAGE CLASSNAMES
        unit_cls_name="ExpressMailCarUnit", chassis="6_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailPostOfficeCar",
        base_numeric_id=31080,
        gen=2,
        subtype="U",
        livery_group_name="gen_2_pax_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="6_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailPostOfficeCar",
        base_numeric_id=31310,
        gen=3,
        subtype="U",
        livery_group_name="gen_3_pax_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="6_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailPostOfficeCar",
        base_numeric_id=31420,
        gen=4,
        subtype="U",
        livery_group_name="gen_4_pax_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailPostOfficeCar",
        base_numeric_id=31540,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressMailCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    return result
