from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="wyvern",
        base_numeric_id=21370,
        name="Wyvern",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2200,  # not an exact linear progression in this tree
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-6,  # let's not have everything turn up in 1960
        fixed_run_cost_points=30,  # give a bonus so this can be a genuine mixed-traffic engine
        liveries=["CLASSIC_LINES", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=130,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Turn the key and it goes.  It's right heavy for what it is, but you can't argue with progress."""
    )
    model_def.define_foamer_facts("""BR Class 40 and Class 44/45/46 <i>Peaks</i>""")

    result.append(model_def)

    return result
