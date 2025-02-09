from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="diablo",
        base_numeric_id=4910,
        name="2-6-0 Diablo",
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1450,
        },
        tractive_effort_coefficient=0.22,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=4,  # introduce a bit later
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=36, vehicle_length=3, spriterow_num=1
    )

    model_def.define_description("""Right happy with the look of these.""")
    model_def.define_foamer_facts(
        """LMS <i>Hughes Crab</i>, BR Standard Class 4 2-6-0"""
    )

    result.append(model_def)

    return result
