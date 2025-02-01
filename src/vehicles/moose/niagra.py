from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="niagra",
        base_numeric_id=34880,
        name="Niagra",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1150,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description("""""")
    consist_factory.add_foamer_facts("""""")

    return consist_factory
