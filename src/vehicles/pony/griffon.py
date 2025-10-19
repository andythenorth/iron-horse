from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="griffon",
        base_numeric_id=21360,
        name="Griffon",  # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        liveries=[
            "CONVENTIONAL_WISDOM",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY", # coal
            "LOWER_LINES",
            "STOCK_STANDARD",
        ],
        decor_spriterow_num=5,
        show_decor_in_purchase_for_variants=[0, 1, 2],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=74,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Kelpie were right good, this is the rebuilt version."""
    )
    model_def.define_foamer_facts("""BR Class 33""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=800, unit_repeats=[2])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
