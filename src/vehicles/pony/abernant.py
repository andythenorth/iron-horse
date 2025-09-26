from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="abernant",
        base_numeric_id=30080,
        name="0-8-4 Abernant",
        subrole="freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1250,
        },
        random_reverse=True,
        speed=60,  # bumped to last 2 generations
        tractive_effort_coefficient=0.24,
        gen=2,
        intro_year_offset=5,  # let's be a little bit later for this one
        extended_vehicle_life=True,
        liveries=["STOCK_STANDARD", "VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=99,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """LNWR 380 Class 'Beames Tank', Port Talbot Railway Cooke Tank"""
    )

    result.append(model_def)

    return result
