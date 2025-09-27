from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="cheddar_valley",
        base_numeric_id=21300,
        name="Cheddar Valley",
        subrole="super_heavy_freight",
        subrole_child_branch_num=3,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=3,  # let's be a little bit later for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        # unfinished EWS livery exists, but eh
        liveries=["CLASSIC_LINES", "CLASSIC_LINES", "FREIGHTLINER_GBRF", "SUPERGRAPHIC", "SUPERGRAPHIC"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=125,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """I shipped these in from overseas.  Pull you backwards through a wall this one will.  Right proper engine."""
    )
    model_def.define_foamer_facts(
        """GMD  / EMD Class 59, uprated GMD / EMD 710 series prime mover"""
    )

    result.append(model_def)

    return result
