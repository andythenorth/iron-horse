from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="pika",
        base_numeric_id=30670,
        name="0-4-0+0-4-0 Pika",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 800,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        speed=60,
        random_reverse=True,
        gen=2,
        intro_year_offset=15,
        liveries=["BANGER_BLUE", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
