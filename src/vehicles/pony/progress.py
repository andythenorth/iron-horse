from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="progress",
        base_numeric_id=16860,
        name="Progress",
        subrole="gronk",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        liveries=["VANILLA", "BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=48,
        vehicle_length=4,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Punchy little number.""")
    model_def.define_foamer_facts(
        """GEC <i>Stephenson</i> industrial shunters, BR Class 07"""
    )

    result.append(model_def)

    return result
