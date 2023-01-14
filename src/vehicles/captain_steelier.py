from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="captain_steelier",
        base_numeric_id=8320,
        name="Captain Steelier",
        role="branch_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1300,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """I can make a General in five minutes, but a good horse is hard to replace."""
    consist.foamer_facts = """Upgraded Alco S1, EMD switchers, Brush Bagnall steelworks locos"""

    return consist
