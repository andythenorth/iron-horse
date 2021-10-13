from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bulleid",
        base_numeric_id=6410,
        name="4-8-2 [bulleid]",
        role="heavy_express",
        role_child_branch_num=-4,
        power=2250,
        tractive_effort_coefficient=0.25,
        gen=3,
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=120,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=32, vehicle_length=4, spriterow_num=1
    )

    consist.description = (
        """A right big'un from Mr. Gresley. Put these in your pipe and smoke it."""
    )
    consist.foamer_facts = """LNER P2"""

    return consist
