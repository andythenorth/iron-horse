from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="kelpie",
        base_numeric_id=21130,
        name="Kelpie",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        gen=4,
        caboose_family="railfreight_1",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        cabbage_new_livery_system=True,
        decor_spriterow_num=3,
        show_decor_in_purchase_for_variants=[2],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description("""Neat these are, to my mind.""")
    model_def.define_foamer_facts("""BR Class 26/27/33""")

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=450, unit_repeats=[2])

    model_def.complete_clone()

    result.append(model_def)

    return result
