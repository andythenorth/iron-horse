from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="challenger",
        base_numeric_id=14020,
        name="4-6-6-4 Challenger",
        role="heavy_freight",
        subrole_child_branch_num=-3,
        power=6000,
        tractive_effort_coefficient=0.4,
        gen=4,
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=60, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit,
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=1,
    )

    consist.add_unit(type=SteamEngineUnit, weight=60, vehicle_length=6, spriterow_num=2)

    consist.description = """ """
    consist.foamer_facts = """ """

    return consist
