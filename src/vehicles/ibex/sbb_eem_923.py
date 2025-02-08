from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="sbb_eem_923",
        base_numeric_id=34770,
        name="SBB Eem 923",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 750,
            "AC": 2000,
        },  # IRL 400 HP at rail for diesel modes, but gets a bump for gameplay
        random_reverse=True,
        gen=5,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    model_def.add_unit(
        class_name="ElectroDieselEngineUnit",
        weight=105,
        vehicle_length=6,
        spriterow_num=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""DR E 21 51""")

    result.append(model_def)

    return result
