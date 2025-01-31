from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="haar",
        base_numeric_id=1880,
        name="0-8-0 Haar",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0)

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=3, spriterow_num=1
    )

    consist_factory.description = (
        """This is right ugly, but the shed likes them. Easy to maintain. They'll do."""
    )
    consist_factory.foamer_facts = """SR Q1 Class, LMS Class 7F"""

    return consist_factory
