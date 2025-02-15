from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="reliance",
        base_numeric_id=4890,
        name="2-4-0 Reliance",
        subrole="express",
        subrole_child_branch_num=-1,
        replacement_model_base_id="carrack",  # this Joker ends with Carrack
        power_by_power_source={
            "STEAM": 950,
        },
        tractive_effort_coefficient=0.12,
        fixed_run_cost_points=140,  # minor cost bonus so it can make money
        gen=1,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=56, vehicle_length=5, spriterow_num=0
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=30, vehicle_length=3, spriterow_num=1
    )

    model_def.define_description("""Lots of these about, but ours are best uns.""")
    model_def.define_foamer_facts(
        """GWR 3201 <i>Stella</i> Class, generic 2-4-0 locomotives"""
    )

    result.append(model_def)

    return result
