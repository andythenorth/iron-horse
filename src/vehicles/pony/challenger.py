from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="challenger",
        base_numeric_id=14020,
        name="4-6-6-4 Challenger",
        subrole="heavy_freight",
        subrole_child_branch_num=-3,
        power=6000,
        tractive_effort_coefficient=0.4,
        gen=4,
        sprites_complete=False,
    )

    model_def.add_unit(
        class_name="SteamEngineUnit", weight=60, vehicle_length=6, spriterow_num=0
    )

    model_def.add_unit(
        class_name="SteamEngineTenderUnit",
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=1,
    )

    model_def.add_unit(
        class_name="SteamEngineUnit", weight=60, vehicle_length=6, spriterow_num=2
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts(""" """)

    result.append(model_def)

    return result
