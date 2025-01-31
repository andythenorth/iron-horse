from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="yillen",
        base_numeric_id=6370,
        name="Yillen",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a little earlier for this one
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    # 2 separate units so that buy menu has reversed cabs
    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=67, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=67, vehicle_length=5, spriterow_num=1
    )

    consist_factory.description = """The universe is asymmetric. And so are these."""
    consist_factory.foamer_facts = """BR Class 15, BR Class 16"""

    return consist_factory
