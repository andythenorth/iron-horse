from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="defiant",
        base_numeric_id=21830,
        name="Defiant",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 4150,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.355,
        random_reverse=True,
        gen=6,
        intro_year_offset=-4,  # let's be a little bit earlier for this one
        fixed_run_cost_points=200,  # run cost nerf as light weight throws the cost too cheap
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=95,  # notably low weight
        vehicle_length=8,
        spriterow_num=0,
    )

    consist_factory.add_description("""Amazing what they can do these days isn't it?""")
    consist_factory.add_foamer_facts("""Vossloh Eurolight (DRS Class 68)""")

    return consist_factory
