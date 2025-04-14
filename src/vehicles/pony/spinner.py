from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="spinner",
        base_numeric_id=480,
        name="4-2-2 Spinner",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 950,
        },
        tractive_effort_coefficient=0.12,
        fixed_run_cost_points=160,  # minor cost bonus so it can make money
        gen=1,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=48,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=30,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """I told them they need a big engine, not big wheels.  But they pay the piper, so they call the tune.  It does go fast, I'll give it that."""
    )
    model_def.define_foamer_facts(
        """Midland Railway 115 Class <i>Spinner</i>, GNR <i>Stirling Single</i>"""
    )

    result.append(model_def)

    return result
