from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="strongbow",
        base_numeric_id=980,
        name="4-6-0 Strongbow",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,  # not an exact linear progression in this tree
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=96,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=34,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """Got this one off Mr. Stanier.  It'll go anywhere, do anything, for not too much brass."""
    )
    model_def.define_foamer_facts(
        """LMS Jubilee Class, original TTD Chaney 'Jubilee'"""
    )

    result.append(model_def)

    return result
