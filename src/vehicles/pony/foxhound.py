from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="foxhound",
        base_numeric_id=27160,
        name="Foxhound",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description("""This one gets after it, no doubts at all.""")
    model_def.define_foamer_facts("""BR Class 21/22/29""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=810, unit_repeats=[2])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
