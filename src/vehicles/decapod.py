# deprecated
from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="decapod",
        base_numeric_id=15810,
        name="0-10-0 Decapod",
        role="branch_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 650,
        },
        gen=2,
        intro_year_offset=7,  # let's be a little bit later for this one
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=54, vehicle_length=6, spriterow_num=0)

    consist.description = """Don't know what they were thinking, but they asked me to build it. Well, it's done."""
    consist.foamer_facts = """GER Class A55 <i>Decapod</i>"""

    return consist
