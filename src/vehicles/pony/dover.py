from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcar",
        model_id="dover",
        base_numeric_id=21150,
        name="Dover",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 540,
        },
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        formation_ruleset="railcars_3_unit_sets",
        gen=4,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="electric_railcar_mail_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricRailcarMailUnit",
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description("""A useful motor van for mail and express freight.""")
    model_def.define_foamer_facts("""BR Class 419 MLV, Class 489 GLV""")

    result.append(model_def)

    return result
