from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcar",
        model_id="ares",
        base_numeric_id=20810,
        name="Ares",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "OHLE": 400,
        },
        pantograph_type="diamond-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=3,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_3_electric_railcar_mail_liveries",
        sprites_complete=True,
    )

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
