from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="emu_ibex_6",
        base_numeric_id=34500,
        name="FLIRT",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=6,
        sprites_complete=False,
        # intro_year_offset=-3,
    )

    consist_factory.add_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist_factory.add_description(""" """)
    consist_factory.add_foamer_facts("""Stadler FLIRT""")

    result.append(consist_factory)

    return result
