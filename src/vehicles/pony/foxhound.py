from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="foxhound",
        base_numeric_id=27160,
        name="Foxhound",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = """This one gets after it, no doubts at all."""
    consist_factory.foamer_facts = """BR Class 21/22/29"""

    consist_factory.add_clone(base_numeric_id=810, clone_units=[2])

    return consist_factory
