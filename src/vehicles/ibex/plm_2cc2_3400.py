from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="EngineConsist",
        id="plm_2cc2_3400",
        base_numeric_id=150,
        name="PLM 2CC2 3400",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={"DC": 4600},
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce much later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    model_def.define_unit(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=8,
        spriterow_num=0,
        repeat=2,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""PLM 2CC2 3400""")

    result.append(model_def)

    return result
