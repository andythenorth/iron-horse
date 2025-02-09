from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="hercules",
        base_numeric_id=380,
        name="0-6-0 Hercules",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1100,
        },
        tractive_effort_coefficient=0.24,
        gen=1,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=59, vehicle_length=5, spriterow_num=0
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=30, vehicle_length=3, spriterow_num=1
    )

    model_def.define_description(
        """Cheap to build, cheap to run.  I'll take a dozen at once."""
    )
    model_def.define_foamer_facts(
        """GWR 2301 Dean Goods Class, generic 0-6-0 freight locomotives"""
    )

    result.append(model_def)

    return result
