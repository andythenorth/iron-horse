from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="vulcan",
        base_numeric_id=21700,
        name="Vulcan",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_ORANGE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=105,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
    )

    model_def.define_description(
        """These aren't bad at all. Clever electronics they tell me."""
    )
    model_def.define_foamer_facts("""English Electric DP2 prototype""")

    result.append(model_def)

    return result
