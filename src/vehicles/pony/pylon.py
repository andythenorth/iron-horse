from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcar",
        model_id="pylon",
        base_numeric_id=20800,
        name="Pylon",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={"DIESEL": 700, "OHLE": 820},
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        formation_ruleset="railcars_3_unit_sets",
        gen=6,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_6_electric_railcar_mail_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselRailcarMailUnit",
        weight=36,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description("""The last word in mail-by-rail.""")
    model_def.define_foamer_facts("""Orion Class 769 <i>FLEX</i>""")

    result.append(model_def)

    return result
