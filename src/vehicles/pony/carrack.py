from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="carrack",
        base_numeric_id=1040,
        name="4-4-0 Carrack",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1200,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=60, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=30, vehicle_length=3, spriterow_num=1
    )

    consist_factory.description = (
        """It's not the biggest, but there's nowt wrong wi this one."""
    )
    consist_factory.foamer_facts = """Midland Railway 483 Class, GWR <i>City</i> 3700 Class, generic 4-4-0 locomotives"""

    return consist_factory
