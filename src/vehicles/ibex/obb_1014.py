from train import ConsistFactory

# multi-system !!


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="obb_1014",
        base_numeric_id=35000,
        name="OBB 1014",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 4800,
        },
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
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
    consist_factory.add_foamer_facts("""OBB 1014""")

    result.append(consist_factory)

    return result
