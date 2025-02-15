from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineExpressRailcar",
        base_id="chronos",
        base_numeric_id=950,
        name="Chronos",
        subrole="express_mail_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={"AC": 2800},
        pantograph_type="z-shaped-single-with-base",
        gen=5,
        intro_year_offset=1,  # introduce later by design
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricRailcarMailUnit",
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_def.define_description(
        """Time's courier swift. Chronos weaves through night and day. Posts haste, never late."""
    )
    model_def.define_foamer_facts("""BR Class 325 mail/parcels EMU""")

    result.append(model_def)

    return result
