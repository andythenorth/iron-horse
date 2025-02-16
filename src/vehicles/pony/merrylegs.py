from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="merrylegs",
        base_numeric_id=21310,
        name="2-6-2 Merrylegs",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 650,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=2,
        caboose_family="gwr_1",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=49,
        vehicle_length=6,
        spriterow_num=0,
    )

    model_def.define_description(
        """Larks were getting a bit past it.  These are right well balanced."""
    )
    model_def.define_foamer_facts("""GWR 4500 Class <i>Prairie Tank</i>""")

    result.append(model_def)

    return result
