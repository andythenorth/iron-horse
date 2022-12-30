from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="merrylegs",
        base_numeric_id=9540,
        name="2-6-2 Merrylegs",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 650,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=2,
        caboose_family="gwr_1",
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=49, vehicle_length=6, spriterow_num=0)

    consist.description = (
        """Larks were getting a bit past it.  These are right well balanced."""
    )
    consist.foamer_facts = """GWR 4500 Class <i>Prairie Tank</i>"""

    return consist
