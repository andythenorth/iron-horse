from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="vigilant",
        base_numeric_id=4870,
        name="2-8-0 Vigilant",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 1850,
        },
        tractive_effort_coefficient=0.32,
        fixed_run_cost_points=245,  # cost malus, early heavy freight engines are too cheap to run relative to smaller engines
        gen=2,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=92,
        vehicle_length=6,
        spriterow_num=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=4, spriterow_num=1
    )

    model_def.define_description(
        """It's a big engine, it cost a lot of brass, get it to work."""
    )
    model_def.define_foamer_facts("""GCR Class 8K / ROD 2-8-0, GWR 2800 Class""")

    result.append(model_def)

    return result
