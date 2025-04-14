from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="little_bear",
        base_numeric_id=21220,
        name="Little Bear",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        intro_year_offset=-6,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=68,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """I want no epitaphs of profound history and all that type of thing. I contributed - I would hope they would say that, and I would hope somebody liked me."""
    )
    # IRL the quote is Brian Clough
    model_def.define_foamer_facts("""BR Class 14, Clayton DHP1 prototype""")

    result.append(model_def)

    return result
