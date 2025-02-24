from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="trient",
        base_numeric_id=32700,
        name="Trient",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 4050,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=3,  # let's be a little bit later for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        liveries=["VANILLA"],
        cabbage_new_livery_system=True,
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_GREEN"),
            ("COLOUR_ORANGE", "COLOUR_RED"),
        ],
        requires_high_clearance=True,
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=125,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
