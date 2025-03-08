from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="proper_job",
        base_numeric_id=21280,
        name="2-6-2 Proper Job",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 800,
        },
        gen=3,
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        caboose_family="gwr_1",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=57,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """For when you need proper engine at proper price. Proper Job."""
    )
    model_def.define_foamer_facts(
        """BR Standard Class 3, LMS Ivatt Class 2 and GWR 5101/6100 Class <i>Prairie Tanks</i>"""
    )

    result.append(model_def)

    return result
