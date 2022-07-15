from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="niagra",
        base_numeric_id=9010,
        name="Niagra",
        role="branch_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1150,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """CABBAGE."""
    consist.foamer_facts = """CABBAGE, Alco S1, EMD switchers"""

    return consist
