from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="proper_job",
        base_numeric_id=10340,
        name="2-6-2 Proper Job",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 800,
        },
        gen=3,
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        caboose_family="gwr_1",
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL"],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=57, vehicle_length=6, spriterow_num=0)

    consist.description = (
        """For when you need proper engine at proper price. Proper Job."""
    )
    consist.foamer_facts = """BR Standard Class 3, LMS Ivatt Class 2 and GWR 5101/6100 Class <i>Prairie Tanks</i>"""

    return consist
