from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="high_power_railcar_5",
        base_numeric_id=35200,
        name="SBB RBDe 560",
        subrole="high_power_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 3400,
        },
        random_reverse=True,
        gen=5,
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

    model_type_factory.define_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    model_type_factory.define_description(""" """)
    model_type_factory.define_foamer_facts("""SBB RBDe 560""")

    result.append(model_type_factory)

    return result
