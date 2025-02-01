from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="cc_7100",
        base_numeric_id=31140,
        name="CC 7100",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={"DC": 5300},
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
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
    consist_factory.add_foamer_facts("""SNCF CC 7100""")

    result.append(consist_factory)

    return result
