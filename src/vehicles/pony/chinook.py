from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="chinook",
        base_numeric_id=120,
        name="Chinook",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        gen=4,
        intro_year_offset=-1,  # let's not have everything turn up in 1960
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        liveries=[
            "CONVENTIONAL_WISDOM",
            "BANGER_BLUE",
            "STOCK_STANDARD",
            "RAILFREIGHT_RED_STRIPE",
            "SHOW_PONY",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=80,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=80,
        vehicle_length=6,
        rel_spriterow_index=1,
    )

    model_def.define_description("""I send these out in twos.""")
    model_def.define_foamer_facts("""BR Class 20, uprated EE 8CSVT prime mover""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=16720, unit_repeats=[1, 0])

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_def_clone.random_reverse = True

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
