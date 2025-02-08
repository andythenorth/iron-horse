from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="cringle",
        base_numeric_id=24480,
        name="Cringle",
        subrole="metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        random_reverse=True,
        gen=2,
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="MetroUnit", weight=48, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """Engines stop running, do I have no fear?"""
    )
    model_def.define_foamer_facts(
        """London Underground battery-electric locos"""
    )

    result.append(model_def)

    return result
