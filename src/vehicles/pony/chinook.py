from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="chinook",
        base_numeric_id=120,
        name="Chinook",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        caboose_family="railfreight_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE", "SWOOSH"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=80, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=80, vehicle_length=6, spriterow_num=1
    )

    consist_factory.description = """I send these out in twos."""
    consist_factory.foamer_facts = """BR Class 20, uprated EE 8CSVT prime mover"""

    consist_factory.add_clone(base_numeric_id=34900, clone_units=[1, 0])
    print("cabbage 939", consist_factory.kwargs["id"])
    """
    # also JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    consist_factory.clones[0].random_reverse = True
    """
    return consist_factory
