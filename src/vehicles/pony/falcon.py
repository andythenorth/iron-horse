from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="falcon",
        base_numeric_id=17860,
        name="Falcon",
        subrole="super_heavy_express",
        subrole_child_branch_num=-2,
        replacement_model_id="rapid",  # this Joker ends with Rapid (switching child branch) - goal is to keep Falcon around for a while, because I like it
        power_by_power_source={
            "DIESEL": 2800,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=5,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_YELLOW"),
        ],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-1, 0), (1, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.define_description("""The big bird. Twin engines. Takes on anything.""")
    model_def.define_foamer_facts("""Brush / BR Class 53 <i>Falcon</i> prototype""")

    result.append(model_def)

    return result
