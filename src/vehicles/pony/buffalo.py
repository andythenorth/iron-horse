from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="buffalo",
        base_numeric_id=21720,
        name="0-6-2 Buffalo",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
        replacement_consist_id="saxon",  # this Joker ends with Saxon
        power_by_power_source={
            "STEAM": 650,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.3,
        fixed_run_cost_points=110,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=46, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description(
        """We were wanting a small engine for coal and that, this will do right well."""
    )
    model_def.define_foamer_facts("""LNWR Webb <i>Coal Tank</i>""")

    result.append(model_def)

    return result
