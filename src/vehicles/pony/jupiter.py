from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcarConsist",
        base_id="jupiter",
        base_numeric_id=21840,
        name="Jupiter",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 680,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        consist_ruleset="railcars_3_unit_sets",
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="ElectricRailcarMailUnit",
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
