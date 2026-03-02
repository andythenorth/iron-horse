from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="magnum_vario",
        base_numeric_id=21680,
        name="Magnum Vario",
        subrole="gronk",
        subrole_child_branch_num=-4,
        power_by_power_source={
            "BATTERY_HYBRID": 900,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=6,
        intro_year_offset=-6,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        liveries=["LOWER_LINES", "BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="BatteryHybridEngineUnit",
        weight=90,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Even Gronks don't last forever.""")
    model_def.define_foamer_facts("""Clayton CBD90""")

    result.append(model_def)

    # !! as of Mar 2026, the clones have the same purchase cost and run cost as the source
    # !! that's likely fixable, but eh

    model_def_clone = model_def.begin_clone(base_numeric_id=17310, unit_repeats=[0])

    model_def_clone.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=67,
        vehicle_length=6,
        rel_spriterow_index=1,
    )
    model_def_clone.clone_stats_adjustment_factor = 0.75

    model_def_clone = model_def_clone.complete_clone()

    result.append(model_def_clone)

    model_def_clone = model_def.begin_clone(base_numeric_id=17250, unit_repeats=[0])

    model_def_clone.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=45,
        vehicle_length=4,
        rel_spriterow_index=2,
    )
    model_def_clone.clone_stats_adjustment_factor = 0.5

    model_def_clone = model_def_clone.complete_clone()

    result.append(model_def_clone)

    return result
