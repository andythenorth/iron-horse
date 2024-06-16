from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="captain_steel",
        base_numeric_id=21650,
        name="Captain Steel",
        role="branch_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1450,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Imported job. No fuss, no bother."""
    consist.foamer_facts = """Alco S1, EMD switchers, Brush Bagnall steelworks locos"""

    return consist
