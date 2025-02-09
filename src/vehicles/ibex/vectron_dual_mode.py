from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="vectron_dual_mode",
        base_numeric_id=30810,
        name="Vectron Dual-Mode",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2400,
            "AC": 3200,
        },  # IRL 2600 HP at rail for both modes, but for gameplay what's the point of electric if not more powerful?
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        intro_year_offset=9,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=105,
        vehicle_length=8,
        spriterow_num=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""Siemens Vectron Dual-Mode""")

    result.append(model_def)

    return result
