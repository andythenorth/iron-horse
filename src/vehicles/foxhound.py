from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="foxhound",
        base_numeric_id=15480,
        name="Foxhound",
        role="branch_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        gen=4,
        # additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """This one gets after it, no doubts at all."""
    consist.foamer_facts = """BR Class 21/22/29"""

    return consist
