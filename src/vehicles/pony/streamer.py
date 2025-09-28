from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="streamer",
        base_numeric_id=4840,
        name="4-6-4 Streamer",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,  # -ve because Joker
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        liveries=["RIDEWELL", "STOCK_STANDARD"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=111,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=39,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """Mr. Gresley did these. I'm sure he knows what he's doing."""
    )
    model_def.define_foamer_facts("""LNER W1 'Hush Hush'""")

    result.append(model_def)

    return result
