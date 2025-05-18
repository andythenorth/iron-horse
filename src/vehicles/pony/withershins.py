from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="withershins",
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
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH", "RAILFREIGHT_RED_STRIPE"],
        decor_spriterow_num=4,
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=78, vehicle_length=6, repeat=2
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")  # BR Class 23, QR 1250 class, Ghana Henschel

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=20930, unit_repeats=[1])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
