from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        # random_reverse=True, # tried random reverse, unsure if I liked the result, so nerfed it off
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        liveries=["CONVENTIONAL_WISDOM", "STOCK_STANDARD", "CLASSIC_LINES", "INDUSTRIAL_YELLOW"],
        decor_spriterow_num=8,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=78,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=78,
        vehicle_length=6,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Run it hard, put it away wet.""")
    model_def.define_foamer_facts(
        """Queensland Railways 1270 class, British Thomson-Houston <i>Explorer</i> class, BR Class 16"""
    )

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=20930, unit_repeats=[1, 0])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
