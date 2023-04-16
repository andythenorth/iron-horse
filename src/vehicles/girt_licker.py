from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="girt_licker",
        base_numeric_id=70,
        name="0-10-0 Girt Licker",
        role="super_heavy_freight",
        role_child_branch_num=-1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 1850,  # match to Vigilant
        },
        tractive_effort_coefficient=0.33,
        fixed_run_cost_points=250,  # cost malus, early heavy freight engines are too cheap to run relative to smaller engines
        gen=2,
        intro_year_offset=6,  # introduce a bit later
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit, weight=100, vehicle_length=6, spriterow_num=0
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=45, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Big ugly thing. Power in spades though."""
    consist.foamer_facts = """Midland Railway 2290 'Big Bertha' Lickey Banker"""

    return consist
