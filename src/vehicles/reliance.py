from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="reliance",
        base_numeric_id=4890,
        name="2-4-0 Reliance",
        role="express",
        role_child_branch_num=-1,
        replacement_consist_id="carrack",  # this Joker ends with Carrack
        power_by_power_source={
            "STEAM": 950,
        },
        tractive_effort_coefficient=0.12,
        fixed_run_cost_points=140,  # minor cost bonus so it can make money
        gen=1,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=56, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = """Lots of these about, but ours are best uns."""
    consist.foamer_facts = """GWR 3201 <i>Stella</i> Class, generic 2-4-0 locomotives"""

    return consist
