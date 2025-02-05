from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="arrow",
        base_numeric_id=6420,
        name="2-6-2 Arrow",
        subrole="heavy_express",
        subrole_child_branch_num=-2,  # -ve because Joker
        power_by_power_source={
            "STEAM": 1900,  # slightly higher power, offset by higher weight
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        fixed_run_cost_points=130,  # give a small bonus to bring closer to Strongbow cost
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_DARK_GREEN"),
            ("COLOUR_GREY", "COLOUR_WHITE"),
            ("COLOUR_WHITE", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="SteamEngineUnit",
        weight=96,
        vehicle_length=7,
        effect_offsets=[(-3, 0)],
        spriterow_num=0,
    )

    model_type_factory.define_unit(
        class_name="SteamEngineTenderUnit", weight=44, vehicle_length=3, spriterow_num=1
    )

    model_type_factory.define_description(
        """Passengers, mail, fish, coal, steel, grain, this one'll haul anything and do it well."""
    )
    model_type_factory.define_foamer_facts("""LNER V2""")

    result.append(model_type_factory)

    return result
