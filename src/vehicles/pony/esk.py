from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="esk",
        base_numeric_id=4050,
        name="2-6-0+0-6-2 Esk",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 2400,
        },
        tractive_effort_coefficient=0.4,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="SteamEngineTenderUnit", weight=60, vehicle_length=3, spriterow_num=0
    )

    model_def.add_unit(
        class_name="SteamEngineUnit",
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0)],
        spriterow_num=1,
    )

    model_def.add_unit(
        class_name="SteamEngineTenderUnit", weight=60, vehicle_length=3, spriterow_num=2
    )

    model_def.define_description("""Well it's a big bugger isn't it.""")
    model_def.define_foamer_facts("""LMS Garratt""")

    result.append(model_def)

    return result
