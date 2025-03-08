from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="roarer",
        base_numeric_id=16870,
        name="Roarer",
        subrole="super_heavy_express",
        subrole_child_branch_num=-4,
        power_by_power_source={
            "AC": 3000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=2,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=80, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description(
        """They're right loud these are, but we've got the power right up on em too."""
    )
    model_def.define_foamer_facts("""BR 'AL' Classes 81-85""")

    result.append(model_def)

    return result
