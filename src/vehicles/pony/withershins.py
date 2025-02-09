from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        decor_spriterow_num=3,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=82, vehicle_length=6, repeat=2
    )

    model_def.define_description("""It's a rat pack. What more do you want?""")
    model_def.define_foamer_facts("""BR Class 24, BR Class 25""")

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=34910, unit_repeats=[1])

    model_def.complete_clone()

    result.append(model_def)

    return result
