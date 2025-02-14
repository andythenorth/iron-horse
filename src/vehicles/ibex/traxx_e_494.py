from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="traxx_e_494",
        base_numeric_id=34700,
        name="Captrain Italia E.494 Traxx 3 LM",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
        # !! maybe add last mile diesel?  tends to not be useful on high HP electrics, but eh...?
        power_by_power_source={"DC": 7400, "DIESEL": 2000},
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
        """Captrain Italia E.494 Traxx 3 FS 140 DC Last Mile"""
    )

    result.append(model_def)

    return result
