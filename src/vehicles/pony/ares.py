from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcarConsist",
        base_id="ares",
        base_numeric_id=20810,
        name="Ares",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 400,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        # use_3_unit_sets=True, # Ares only 2 unit sets, varies from other Pony mail railcars
        gen=3,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="ElectricRailcarMailUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_def.define_description("""A handy parcels car.""")
    model_def.define_foamer_facts("""LNER <i>Tyneside Electrics</i>""")

    result.append(model_def)

    return result
