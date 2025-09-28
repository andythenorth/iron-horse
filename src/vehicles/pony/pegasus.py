from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="pegasus",
        base_numeric_id=300,
        name="2-8-2 Pegasus",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.25,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        liveries=["SURE_PACE", "STOCK_STANDARD", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=110,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=40,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """A right big'un from Mr. Gresley. Put these in your pipe and smoke it."""
    )
    model_def.define_foamer_facts("""LNER P1, P2""")

    result.append(model_def)

    return result
