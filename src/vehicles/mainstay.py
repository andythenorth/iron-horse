from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="mainstay",
        base_numeric_id=6360,
        name="2-8-0 Mainstay",
        role="heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,
        },
        speed=60,
        tractive_effort_coefficient=0.23,
        gen=3,
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=96, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=50, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Bombproof."""
    consist.foamer_facts = """WD Austerity 2-8-0, USRA S160 Class 2-8-0"""

    return consist
