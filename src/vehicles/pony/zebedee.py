from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="zebedee",
        base_numeric_id=21690,
        name="Zebedee",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "AC": 4850,  # 4850 not 5000 simply for rapid and obvious distinction from the nearby 3800 and 5800 power bands
        },
        random_reverse=True,
        gen=4,
        speed=120,
        pantograph_type="z-shaped-double",
        intro_year_offset=12,  # introduce much later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "WHITE_STRIPE",
            "RES",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "LOADHAUL",
        ],
        default_livery_extra_docs_examples=[("COLOUR_BLUE", "COLOUR_WHITE")],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=82, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """These were heavy on the track, but we had em back and fitted extra springs."""
    )
    model_def.define_foamer_facts("""BR Class 86 / Class 87""")

    result.append(model_def)

    return result
