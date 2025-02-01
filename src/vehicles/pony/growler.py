from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="growler",
        base_numeric_id=20940,
        name="Growler",
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        fixed_run_cost_points=40,  # give a huge bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=4,
        caboose_family="railfreight_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "LARGE_LOGO", "RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        decor_spriterow_num=4,
        show_decor_in_purchase_for_variants=[2],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=100, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description("""Sounds like a tractor, pulls like a train.""")
    consist_factory.add_foamer_facts("""BR Class 37, original TTD UU '37'""")

    return consist_factory
