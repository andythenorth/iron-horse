from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        liveries=["CONVENTIONAL_WISDOM"],
        decor_spriterow_num=2,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=78,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=78,
        vehicle_length=6,
        rel_spriterow_index=1,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """"""
    )  # BR Class 16, QR 1270 class, BTH Explorer class

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=20930, unit_repeats=[1, 0])

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_def_clone.random_reverse = True

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
