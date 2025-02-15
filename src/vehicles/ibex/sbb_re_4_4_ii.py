from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="sbb_re_4_4_ii",
        base_numeric_id=35010,
        name="SBB Re 4/4ii",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 6000,
        },
        random_reverse=True,
        gen=4,
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

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Re 4/4<sup>ii</sup>""")

    result.append(model_def)

    return result
