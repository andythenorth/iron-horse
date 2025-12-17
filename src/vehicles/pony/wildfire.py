from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="wildfire",
        base_numeric_id=25970,
        name="Wildfire",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        intro_year_offset=7,  # introduce later than gen epoch by design
        liveries=[
            "STOCK_STANDARD",
            "INVERSIONS",
            "STOCK_STANDARD",
            "CLASSIC_LINES",
            "INDUSTRIAL_YELLOW",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=72,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """Indonesian Railways Co. GE CM20EMP, Vossloh G2000 BB"""
    )

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=15280, unit_repeats=[2])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
