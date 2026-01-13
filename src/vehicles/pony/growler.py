from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="growler",
        base_numeric_id=20940,
        name="Growler",
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        fixed_run_cost_points=40,  # give a huge bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=4,
        liveries=["BANGER_BLUE", "CONVENTIONAL_WISDOM", "SUPERGRAPHIC", "RAILFREIGHT_RED_STRIPE", "CLASSIC_LINES"],
        decor_spriterow_num=5,
        show_decor_in_purchase_for_variants=[2],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=100,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Sounds like a tractor, pulls like a train.""")
    model_def.define_foamer_facts("""BR Class 37, original TTD UU '37'""")

    result.append(model_def)

    return result
