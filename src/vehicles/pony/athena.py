from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="PassengerEngineRailcarConsist",
        id="athena",
        base_numeric_id=20030,
        name="Athena",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=3,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    model_type_factory.define_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_type_factory.define_description("""World's Greatest Suburban Electric""")
    model_type_factory.define_foamer_facts("""LNER <i>Tyneside Electrics</i>""")

    result.append(model_type_factory)

    return result
