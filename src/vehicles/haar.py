from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="haar",
        base_numeric_id=1880,
        name="0-8-0 Haar",
        role="freight",
        role_child_branch_num=2,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        gen=3,
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=70, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=3, spriterow_num=1
    )

    consist.description = (
        """This is right ugly, but the shed likes them. Easy to maintain. They'll do."""
    )
    consist.foamer_facts = """SR Q1 Class, LMS Class 7F"""

    return consist
