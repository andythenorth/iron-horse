from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="pegasus",
        base_numeric_id=300,
        name="2-8-2 Pegasus",
        role="super_heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.25,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=110,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=4, spriterow_num=1
    )

    consist.description = (
        """A right big'un from Mr. Gresley. Put these in your pipe and smoke it."""
    )
    consist.foamer_facts = """LNER P1, P2"""

    return consist
