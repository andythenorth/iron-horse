from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="lark",
        base_numeric_id=20340,
        name="4-4-2 Lark",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 500,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=35, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description(
        """These'll do right nicely for small lines.  I stole the design from Mr. Adams, but I won't tell him if you won't."""
    )
    model_def.define_foamer_facts("""LSWR 415 Class <i>Radial Tank</i>""")

    result.append(model_def)

    return result
