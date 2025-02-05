from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="PassengerEngineRailcarConsist",
        id="emu_ibex_3",
        base_numeric_id=35320,
        name="SBB Ce 2/4",  # see also https://de.wikipedia.org/wiki/SOB_CFZe_4/4
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=3,
        sprites_complete=False,
        # intro_year_offset=-3,
    )

    model_type_factory.define_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_type_factory.define_description(""" """)
    model_type_factory.define_foamer_facts("""SBB Ce 2/4""")

    result.append(model_type_factory)

    return result
