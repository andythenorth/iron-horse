from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="merlion",
        base_numeric_id=17150,
        name="Merlion",
        subrole="express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1750,
        },
        tractive_effort_coefficient=0.25,  # effectively a nerf because realism eh? (A1A-A1A wheel arrangement)
        fixed_run_cost_points=42,  # give a huge bonus so this can be a genuine mixed-traffic engine, and because of 'balancing' the nerfed weight and TE
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a littler earlier for this one
        caboose_family="railfreight_1",
        # add railfreight triple grey
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "BANGER_BLUE",
            "WHITE_STRIPE",
            "RAILFREIGHT_RED_STRIPE",
            "DUTCH_1986",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        decor_spriterow_num=5,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=97,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist_factory.description = (
        """I don't like the looks of it right much, but I suppose it will do."""
    )
    consist_factory.foamer_facts = """BR Class 31, uprated EE 12CSVT prime mover"""

    return consist_factory
