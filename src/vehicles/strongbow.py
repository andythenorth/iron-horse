from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="strongbow",
        base_numeric_id=4320,
        name="4-6-0 Strongbow",
        role="heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,  # not an exact linear progression in this tree
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=96, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=34, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Got this one off Mr. Stanier.  It'll go anywhere, do anything, for not too much brass."""
    consist.foamer_facts = """LMS Jubilee Class, original TTD Chaney 'Jubilee'"""

    return consist
