from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="ae_3_5",
        base_numeric_id=30780,
        name="Ae 3/5",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            # "AC": 1100,
            "AC": 10,
        },
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Ae 3/5""")

    result.append(model_def)

    return result
