from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="general_endeavour",
        base_numeric_id=20980,
        name="General Endeavour",
        role="branch_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1650,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """I can make a General in five minutes, but a good horse is hard to replace."""
    )
    consist.foamer_facts = (
        """Upgraded Alco S1, EMD switchers, Brush Bagnall steelworks locos"""
    )

    return consist
