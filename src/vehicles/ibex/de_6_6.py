from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="de_6_6",
        base_numeric_id=34760,
        name="De 6/6 Seetal Krokodil",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 1200,
        },
        speed=60,  # spans 2 generations
        random_reverse=True,
        gen=2,
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
        class_name="ElectricEngineUnit", weight=105, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB De 6/6 <i>Seetal Krokodil</i>""")

    result.append(model_def)

    return result
