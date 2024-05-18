from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="yak",
        base_numeric_id=21260,
        name="0-8-2 Yak",
        role="branch_freight",
        role_child_branch_num=-2,
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

    consist.add_unit(type=SteamEngineUnit, weight=70, vehicle_length=6, spriterow_num=0)

    consist.description = """We ought to do good to others as simply as a horse runs."""
    consist.foamer_facts = """LNER Thompson Q1 Class tank engine"""

    return consist
