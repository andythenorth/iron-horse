from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="MailEngineRailcarConsist",
        id="pylon",
        base_numeric_id=20800,
        name="Pylon",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={"DIESEL": 700, "AC": 820},
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        use_3_unit_sets=True,
        gen=6,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    model_type_factory.define_unit(
        class_name="ElectroDieselRailcarMailUnit",
        weight=36,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_type_factory.define_description("""The last word in mail-by-rail.""")
    model_type_factory.define_foamer_facts("""Orion Class 769 <i>FLEX</i>""")

    result.append(model_type_factory)

    return result
