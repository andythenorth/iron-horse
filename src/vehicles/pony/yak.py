from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="yak",
        base_numeric_id=21260,
        name="0-8-2 Yak",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 1000,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=3,
        intro_year_offset=0,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description(
        """We ought to do good to others as simply as a horse runs."""
    )
    consist_factory.add_foamer_facts("""LNER Thompson Q1 Class tank engine""")

    return consist_factory
