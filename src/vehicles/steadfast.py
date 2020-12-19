from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="steadfast",
        base_numeric_id=4870,
        name="0-8-0 Steadfast",
        role="freight",
        role_child_branch_num=-1,
        power=1250,
        tractive_effort_coefficient=0.25,
        gen=2,
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=69, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    return consist
