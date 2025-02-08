from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="fs_e646",
        base_numeric_id=160,
        name="FS E.646",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={"DC": 4800},
        random_reverse=True,
        gen=4,
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
    model_def.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=0
    )
    model_def.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=1
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""FS E.646""")

    result.append(model_def)

    return result
