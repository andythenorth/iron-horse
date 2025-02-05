from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="bb_7200",
        base_numeric_id=31000,
        name="BB 7200",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={"DC": 6000},
        random_reverse=True,
        gen=4,
        # pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
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
    model_type_factory.define_foamer_facts("""SNCF BB 7200""")

    result.append(model_type_factory)

    return result
