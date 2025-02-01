from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="pegasus",
        base_numeric_id=300,
        name="2-8-2 Pegasus",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.25,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=110,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=4, spriterow_num=1
    )

    consist_factory.add_description(
        """A right big'un from Mr. Gresley. Put these in your pipe and smoke it."""
    )
    consist_factory.add_foamer_facts("""LNER P1, P2""")

    return consist_factory
