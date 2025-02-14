from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineCabbageDVTConsist",
        base_id="driving_cab_high_speed_mail_pony_gen_6",
        base_numeric_id=17320,
        name="High Speed Driving Van Trailer",
        subrole_child_branch_num=-3,  # driving cab cars are probably jokers?
        gen=6,
        lgv_capable=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="CabbageDVTUnit", weight=34, chassis="railcar_32px"
    )

    model_def.define_description(
        """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Seems to work, so here's a new version."""
    )
    model_def.define_foamer_facts(
        """CAF MK5A Driving Van Trailer (DVT) with added generator"""
    )

    result.append(model_def)

    return result
