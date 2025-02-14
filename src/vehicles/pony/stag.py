# deprecated
from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="stag",
        base_numeric_id=17870,
        name="0-6-4 Stag",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 800,
        },
        gen=3,
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit", weight=60, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description("""Not the biggest, but quite a beast all the same.""")
    model_def.define_foamer_facts(
        """Metropolitan Railway G Class (LNER M2), GCR Class D (LNER M1)"""
    )

    result.append(model_def)

    return result
