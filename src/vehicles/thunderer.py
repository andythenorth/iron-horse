from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="thunderer",
        base_numeric_id=4830,
        name="4-6-0 Thunderer",  # shorter 2-6-0 version was tried, but doesn't fit a power band gap in the mixed traffic roster
        role="heavy_express",
        role_child_branch_num=-1,
        replacement_consist_id="tenacious",  # this Joker ends with Tenacious, long-lived
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

    consist.description = """Bit of an odd beast this one.  It's quite happy on passengers and mail or you can put it on freight.  Right long-lived too."""
    consist.foamer_facts = """GWR 2900 <i>Saint</i> Class, GWR 4000 <i>Star</i> Class"""

    return consist
