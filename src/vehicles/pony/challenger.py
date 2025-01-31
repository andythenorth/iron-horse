from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="challenger",
        base_numeric_id=14020,
        name="4-6-6-4 Challenger",
        subrole="heavy_freight",
        subrole_child_branch_num=-3,
        power=6000,
        tractive_effort_coefficient=0.4,
        gen=4,
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name="SteamEngineUnit", weight=60, vehicle_length=6, spriterow_num=0)

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit",
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=1,
    )

    consist_factory.add_unit(class_name="SteamEngineUnit", weight=60, vehicle_length=6, spriterow_num=2)

    consist_factory.description = """ """
    consist_factory.foamer_facts = """ """

    return consist_factory
