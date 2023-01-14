from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doister",
        base_numeric_id=280,
        name="2-6-0 Doister",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1500,  # slightly less than the Swift (and lighter engine)
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=10,  # introduce later than gen epoch by design
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=82, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    consist.description = """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    consist.foamer_facts = """"""

    return consist
