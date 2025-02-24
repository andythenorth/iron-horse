from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="dreadnought",
        base_numeric_id=16510,
        name="Dreadnought",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=False,  # Dreadnought has asymmetric logo pixels that don't look great when running reversed
        gen=5,
        replacement_model_model_type_id="defiant",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_GREEN", "COLOUR_ORANGE"),
        ],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=102,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.define_description("""This one, it does go some.""")
    model_def.define_foamer_facts("""Porterbrook Leasing Class 55 <i>Deltic</i>'""")

    result.append(model_def)

    return result
