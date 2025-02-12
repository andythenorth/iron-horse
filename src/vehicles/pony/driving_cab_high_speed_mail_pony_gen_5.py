from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineCabbageDVTConsist",
        base_id="driving_cab_high_speed_mail_pony_gen_5",
        base_numeric_id=18090,
        name="High Speed Driving Van Trailer",
        subrole_child_branch_num=-2,  # driving cab cars are probably jokers?
        gen=5,
        lgv_capable=True,  # for lolz
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="CabbageDVTUnit", weight=32, chassis="railcar_32px"
    )

    model_def.define_description(
        """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    )
    model_def.define_foamer_facts(
        """BR MK3 Driving Van Trailer (DVT) with added generator"""
    )

    result.append(model_def)

    return result
