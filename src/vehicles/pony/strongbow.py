from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="strongbow",
        base_numeric_id=4320,
        name="4-6-0 Strongbow",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,  # not an exact linear progression in this tree
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=96, vehicle_length=6, spriterow_num=0
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=34, vehicle_length=4, spriterow_num=1
    )

    model_def.define_description(
        """Got this one off Mr. Stanier.  It'll go anywhere, do anything, for not too much brass."""
    )
    model_def.define_foamer_facts(
        """LMS Jubilee Class, original TTD Chaney 'Jubilee'"""
    )

    result.append(model_def)

    return result
