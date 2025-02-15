from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="fireball",
        base_numeric_id=23990,
        name="0-6-0 Fireball",
        subrole="gronk",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "STEAM": 350,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=101,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=35, vehicle_length=4, spriterow_num=0
    )

    model_def.define_description("""Your typical pint-sized workhorse.""")
    model_def.define_foamer_facts("""GWR 1366 Class pannier tanks""")

    result.append(model_def)

    return result
