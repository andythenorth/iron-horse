from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="kelpie",
        base_numeric_id=21130,
        name="Kelpie",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        gen=4,
        caboose_family="railfreight_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        decor_spriterow_num=3,
        show_decor_in_purchase_for_variants=[2],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description("""Neat these are, to my mind.""")
    consist_factory.add_foamer_facts("""BR Class 26/27/33""")

    consist_factory.add_clone(base_numeric_id=450, clone_units=[2])

    return consist_factory
