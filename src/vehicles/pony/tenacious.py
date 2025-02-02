from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="tenacious",
        base_numeric_id=17180,
        name="Tenacious",
        subrole="heavy_express",
        subrole_child_branch_num=-2,  # -ve because Joker
        power_by_power_source={
            "DIESEL": 2150,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=150,  # give a small bonus so this can be a genuine mixed-traffic engine
        default_livery_extra_docs_examples=[
            ("COLOUR_GREEN", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="DieselEngineUnit",
        weight=80,  # significant bonus over other of same power band
        vehicle_length=8,
        spriterow_num=0,
    )

    consist_factory.define_description(
        """It's rapid, sprightly, and formidable all at once."""
    )
    consist_factory.define_foamer_facts("""BR Class 42/43 <i>Warship</i>""")

    result.append(consist_factory)

    return result
