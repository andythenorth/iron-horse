from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="general_endeavour",
        base_numeric_id=20980,
        name="General Endeavour",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
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

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = (
        """I can make a General in five minutes, but a good horse is hard to replace."""
    )
    consist_factory.foamer_facts = (
        """Upgraded Alco S1, EMD switchers, Brush Bagnall steelworks locos"""
    )

    return consist_factory
