from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="rapid",
        base_numeric_id=21440,
        name="Rapid",
        subrole="heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2800,  # significant jump from previous gen
        },
        # dibble, assume super-slip control, intent is to give higher TE as a non-significant variation from Resilient
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # let's not have everything turn up in 1990
        fixed_run_cost_points=45,  # give a bonus so this can be a genuine mixed-traffic engine
        liveries=["STOCK_STANDARD", "RES"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=105,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """They said they wanted these for a freight engine.  No I said.  We need a general purpose engine I said.  We talked about it for twenty minutes then we decided I was right."""
    )
    model_def.define_foamer_facts("""proposed BR Class 41/48, NIR 201 Class""")

    result.append(model_def)

    return result
