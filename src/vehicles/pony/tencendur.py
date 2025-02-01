from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="tencendur",
        base_numeric_id=890,
        name="4-4-0 Tencendur",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1450,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=3, spriterow_num=1
    )

    consist_factory.description = """Tidy, fast, nowt wrong with these."""
    consist_factory.foamer_facts = """SR V <i>Schools</i> Class"""

    return consist_factory
