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
        gen=3,
        additional_liveries=[],
        sprites_complete=False,
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
    consist.foamer_facts = """LNER P2"""

    return consist
