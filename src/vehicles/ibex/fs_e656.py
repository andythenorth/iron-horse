from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="fs_e656",
        base_numeric_id=170,
        name="FS E.656",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={"DC": 5400},
        random_reverse=True,
        gen=5,
        # pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    # !!! these are only 60 foot long IRL so 2x 4/8 units
    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=0
    )
    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=1
    )

    consist_factory.add_description(""" """)
    consist_factory.add_foamer_facts("""FS E.656""")

    result.append(consist_factory)

    return result
