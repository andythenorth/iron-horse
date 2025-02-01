from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="sob_re_446",
        base_numeric_id=31830,
        name="SOB Re 446",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 6700,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce earler than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description(""" """)
    consist_factory.add_foamer_facts("""SOB Re 446 / SBB Re 4/4<sup>iv</sup>""")

    return consist_factory
