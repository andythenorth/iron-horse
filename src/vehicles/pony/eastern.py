from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="eastern",
        base_numeric_id=280,
        name="0-8-0 Eastern",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.27,
        gen=2,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=30, vehicle_length=3, spriterow_num=1
    )

    consist_factory.add_description(
        """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    )
    consist_factory.add_foamer_facts("""LNER Q2 Class""")

    return consist_factory
