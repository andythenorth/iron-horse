
from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="class_23",
        base_numeric_id=39900,
        name="CABBAGE",
        subrole="branch_freight",
        subrole_child_branch_num=-3,
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
        decor_spriterow_num=3,
        show_decor_in_purchase_for_variants=[2],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)
    """
    model_def_clone = model_def.begin_clone(base_numeric_id=450, unit_repeats=[2])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)
    """
    return result
