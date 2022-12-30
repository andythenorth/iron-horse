from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tencendur",
        base_numeric_id=890,
        name="4-4-0 Tencendur",
        role="express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1400,
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=70, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=3, spriterow_num=1
    )

    consist.description = """Tidy, fast, nowt wrong with these."""
    consist.foamer_facts = """SR V <i>Schools</i> class"""

    return consist
