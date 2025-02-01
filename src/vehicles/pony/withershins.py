from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        decor_spriterow_num=3,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=82, vehicle_length=6, repeat=2
    )

    consist_factory.add_description("""It's a rat pack. What more do you want?""")
    consist_factory.add_foamer_facts("""BR Class 24, BR Class 25""")

    consist_factory.add_clone(base_numeric_id=34910, clone_units=[1, 0])

    result.append(consist_factory)

    consist_factory = consist_factory.clone(base_numeric_id=34910)

    result.append(consist_factory)

    return result
