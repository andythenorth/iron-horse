from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="MailEngineRailcar",
        model_id="jupiter",
        base_numeric_id=21840,
        name="Jupiter",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "OHLE": 680,
        },
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        formation_ruleset="railcars_3_unit_sets",
        gen=5,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_5_electric_railcar_mail_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricRailcarMailUnit",
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_def.define_description(
        """A new generation of mail and express freight haulage."""
    )
    model_def.define_foamer_facts("""BR Class 302, BR Class 325""")

    result.append(model_def)

    return result
