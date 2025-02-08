from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="grub",
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
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_BROWN"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="SteamEngineUnit", weight=36, vehicle_length=4, spriterow_num=0
    )

    model_def.define_description("""It's for your little jobs, farms and that.""")
    model_def.define_foamer_facts("""GER G15/C53 tramway locomotives""")

    result.append(model_def)

    return result
