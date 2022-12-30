# deprecated
from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="stag",
        base_numeric_id=15790,
        name="0-6-4 Stag",
        role="branch_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 800,
        },
        gen=3,
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=60, vehicle_length=6, spriterow_num=0)

    consist.description = """Not the biggest, but quite a beast all the same."""
    consist.foamer_facts = (
        """Metropolitan Railway G Class (LNER M2), GCR Class D (LNER M1)"""
    )

    return consist
