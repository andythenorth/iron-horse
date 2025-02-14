from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="po_2d2_5500",
        base_numeric_id=17290,
        name="PO 2D2 5500",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={"DC": 3700},
        speed=75,
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=-8,  # introduce much later than gen epoch by design
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
        vehicle_length=8,
        spriterow_num=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""PO 2D2 5500""")

    result.append(model_def)

    return result
