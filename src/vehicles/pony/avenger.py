from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="avenger",
        base_numeric_id=21530,
        name="Avenger",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 6200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=-2,  # introduce slightly earlier than gen epoch by design
        lgv_capable=True,  # for lolz
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=[
            "VANILLA",
            "WHITE_STRIPE",
            "SWOOSH",
            "SWOOSH_2000",
            "SWOOSH_2000",
            "RAILFREIGHT_TRIPLE_GREY",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
        ],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=100, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """Daft as a brush if you ask me.  Or mad as a badger.  Goes like stink off a shovel though."""
    )
    model_def.define_foamer_facts("""BR Class 89""")

    result.append(model_def)

    return result
