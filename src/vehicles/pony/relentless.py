from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="relentless",
        base_numeric_id=21460,
        name="Relentless",
        subrole="super_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.355,
        random_reverse=True,
        gen=6,
        fixed_run_cost_points=190,  # run cost nerf as light weight throws the cost too cheap
        liveries=["SURE_PACE", "STOCK_STANDARD"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=112,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Solid piece of kit these.""")
    model_def.define_foamer_facts(
        """Newag Griffin, Bombardier Traxx 2, Stadler Euro 4001, Siemens EuroRunner"""
    )

    result.append(model_def)

    return result
