from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="stentor",
        base_numeric_id=21790,
        name="Stentor",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-3,  # Joker eh
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=-2,  # let's be a little bit earlier for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        # more liveries ought to be possible, but I couldn't make them work so eh.  EWS?
        liveries=[
            "CLASSIC_LINES",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "VANILLA",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=128,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description("""This one is loud, and packed with technology.""")
    model_def.define_foamer_facts("""BR Class 60 design mockups""")

    result.append(model_def)

    return result
