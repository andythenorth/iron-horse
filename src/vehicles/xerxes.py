from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="xerxes",
        base_numeric_id=6760,
        name="0-6-0+0-6-0 Xerxes",
        role="heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "STEAM": 1450,
        },
        random_reverse=True,
        gen=1,
        intro_year_offset=20,  # introduce much later than gen epoch by design
        fixed_run_cost_points=140,  # minor run cost bonus as default algorithm makes run cost too high
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=49,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    consist.description = """Not much to say about these two."""
    consist.foamer_facts = """GWR pannier tanks, original TTD Kirby 'Paul'"""

    return consist
