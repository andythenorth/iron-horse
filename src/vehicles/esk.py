from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="esk",
        base_numeric_id=4050,
        name="2-6-0+0-6-2 Esk",
        role="super_heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 2400,
        },
        tractive_effort_coefficient=0.4,
        gen=3,
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=60, vehicle_length=3, spriterow_num=0
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0)],
        spriterow_num=1,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=60, vehicle_length=3, spriterow_num=2
    )

    consist.description = """Well it's a big bugger isn't it."""
    consist.foamer_facts = """LMS Garratt"""

    return consist
