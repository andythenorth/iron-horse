from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="lamia",
        base_numeric_id=21730,
        name="0-6-0 Lamia",  # the name is the Basque mythical creature, not the Greek https://en.wikipedia.org/wiki/Lamia_(Basque_mythology)
        subrole="gronk",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 350,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=101,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=35, vehicle_length=4, spriterow_num=0
    )

    consist_factory.add_description("""Nice little engine this one.""")
    consist_factory.add_foamer_facts("""Bagnall saddle tanks""")

    return consist_factory
