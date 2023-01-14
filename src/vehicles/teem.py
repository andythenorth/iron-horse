from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="teem",
        base_numeric_id=470,
        name="0-6-0+0-6-0 Teem",
        role="heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1750,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=-13,  # introduce much earlier than gen epoch by design
        fixed_run_cost_points=140,  # minor run cost bonus as default algorithm makes run cost too high
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=55,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
