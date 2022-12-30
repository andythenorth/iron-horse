from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lark",
        base_numeric_id=9150,
        name="4-4-2 Lark",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 500,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=35, vehicle_length=6, spriterow_num=0)

    consist.description = """These'll do right nicely for small lines.  I stole the design from Mr. Adams, but I won't tell him if you won't."""
    consist.foamer_facts = """LSWR 415 Class <i>Radial Tank</i>"""

    return consist
