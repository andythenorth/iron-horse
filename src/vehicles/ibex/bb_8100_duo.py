from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="bb_8100_duo",
        base_numeric_id=190,
        name="BB 8100 / 9200 (duo)",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={"DC": 8700},
        speed=75,  # for lolz
        random_reverse=True,
        gen=3,  # spans gen 4 as well
        pantograph_type="diamond-double",
        intro_year_offset=8,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SNCF BB 8100 / 9200 (duo)""")

    result.append(model_def)

    return result
