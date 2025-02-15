from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="doineann",
        base_numeric_id=21110,
        name="Doineann",
        # Marauder??
        # Prevails??
        subrole="heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2750,  # within range of Resilient
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=-4,  # let's be a little earlier for this one
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "SWOOSH", "SWOOSH"],
        default_livery_extra_docs_examples=[
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=110,
        vehicle_length=8,
    )

    model_def.define_description("""Let there be some more test made of my metal.""")
    model_def.define_foamer_facts("""Northern Ireland Railways Class 111""")

    result.append(model_def)

    return result
