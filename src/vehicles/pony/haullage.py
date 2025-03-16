from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="haullage",
        base_numeric_id=39930,
        name="HAULLAGE",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 3650,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=10,  # let's be later for this one
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=132,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """"""
    )

    result.append(model_def)

    return result
