from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="bb_26000_upgraded",
        base_numeric_id=30950,
        name="BB 26000 Sybic (upgraded)",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-4,
        power_by_power_source={"AC": 9300, "DC": 9300},
        random_reverse=True,
        gen=6,
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
    model_def.define_foamer_facts(
        """SNCF BB 26000 <i>Sybic</i> !! multisystem !! upgraded"""
    )

    result.append(model_def)

    return result
