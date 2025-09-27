from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="tencendur",
        base_numeric_id=890,
        name="4-4-0 Tencendur",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1450,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        liveries=["SHOW_PONY", "STOCK_STANDARD"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=40,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Tidy, fast, nowt wrong with these.""")
    model_def.define_foamer_facts("""SR V <i>Schools</i> Class""")

    result.append(model_def)

    return result
