from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="f40ph",
        base_numeric_id=22010,
        name="F40PH",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1800,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=110, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = """"""
    consist_factory.foamer_facts = """"""

    return consist_factory
