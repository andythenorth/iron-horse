from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="proper_job",
        base_numeric_id=21280,
        name="2-6-2 Proper Job",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 800,
        },
        gen=3,
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        caboose_family="gwr_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SteamEngineUnit", weight=57, vehicle_length=6, spriterow_num=0)

    consist_factory.description = (
        """For when you need proper engine at proper price. Proper Job."""
    )
    consist_factory.foamer_facts = """BR Standard Class 3, LMS Ivatt Class 2 and GWR 5101/6100 Class <i>Prairie Tanks</i>"""

    return consist_factory
