from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="dragon",
        base_numeric_id=21070,
        name="Dragon",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_YELLOW"),
        ],
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=99,
        vehicle_length=8,
        effect_offsets=[(-1, 0), (1, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist_factory.description = """A right big fast diesel hydraulic this one is."""
    consist_factory.foamer_facts = """BR Class 52 <i>Western</i>"""

    return consist_factory
