from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
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

    consist_factory.define_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist_factory.define_description("""World's Greatest Suburban Electric""")
    consist_factory.define_foamer_facts("""LNER <i>Tyneside Electrics</i>""")

    result.append(consist_factory)

    return result
