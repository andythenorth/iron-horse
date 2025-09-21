from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="toaster",
        base_numeric_id=21510,
        name="Toaster",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.39,
        random_reverse=True,
        gen=6,
        # introduce as gen 6 by design, but then make it early
        intro_year_offset=-15,
        fixed_run_cost_points=220,  # unrealism: run cost nerf for being so high-powered
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=130,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """I've heard these might catch fire, but we're getting them cheap."""
    )
    model_def.define_foamer_facts("""GE Class 70 <i>Powerhaul</i>""")

    result.append(model_def)

    return result
