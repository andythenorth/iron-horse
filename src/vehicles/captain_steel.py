from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="captain_steel",
        base_numeric_id=14030,
        name="Captain Steel",
        role="branch_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1150,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Imported job. No fuss, no bother."""
    consist.foamer_facts = """Alco S1, EMD switchers, Brush Bagnall steelworks locos"""

    return consist
