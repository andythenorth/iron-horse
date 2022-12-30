from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="swift",
        base_numeric_id=230,
        name="4-4-2 Swift",
        role="heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1550,
        },
        tractive_effort_coefficient=0.18,
        gen=2,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=80, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=35, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Eh it's the right big engine I said they needed. Mr. Raven helped me out a treat with this one."""
    consist.foamer_facts = """GNR Class C1, Class C2 <i>Klondike</i>"""

    return consist
