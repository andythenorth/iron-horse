from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="grub",
        base_numeric_id=21630,
        name="Grub",
        subrole="gronk",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 350,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        liveries=["CLASSIC_LINES", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=36,
        vehicle_length=4,
        rel_spriterow_index=0,
    )

    model_def.define_description("""It's for your little jobs, farms and that.""")
    model_def.define_foamer_facts("""GER G15/C53 tramway locomotives""")

    result.append(model_def)

    return result
