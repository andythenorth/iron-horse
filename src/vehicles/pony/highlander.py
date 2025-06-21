from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="highlander",
        base_numeric_id=15220,
        name="Highlander",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # let's not have everything turn up in 1960
        extended_vehicle_life=True,
        speed=87,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=[
            "VANILLA",
            "BANGER_BLUE",
            "FREIGHT_BLACK",
            #"RAILFREIGHT_RED_STRIPE",
            #"LARGE_LOGO",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=79,
        vehicle_length=6,
        rel_spriterow_index=0,
        repeat=2,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """CIÉ (Irish Transport System) 141 Class and 181 Class"""
    )

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=26330, unit_repeats=[1])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
