from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="rapid",
        base_numeric_id=21440,
        name="Rapid",
        subrole="heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2800,  # significant jump from previous gen
        },
        # dibble, assume super-slip control, intent is to give higher TE as a non-significant variation from Resilient
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # let's not have everything turn up in 1990
        fixed_run_cost_points=45,  # give a bonus so this can be a genuine mixed-traffic engine
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RES"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description(
        """They said they wanted these for a freight engine.  No I said.  We need a general purpose engine I said.  We talked about it for twenty minutes then we decided I was right."""
    )
    consist_factory.add_foamer_facts("""proposed BR Class 41/48, NIR 201 Class""")

    return consist_factory
