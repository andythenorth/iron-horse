from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="peasweep",
        base_numeric_id=1750,
        name="Peasweep",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 3700,
        },
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        # additional_liveries=["FREIGHT_BLACK", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=75,
        vehicle_length=6,
        rel_spriterow_index=0,
        repeat=2,
    )

    model_def.define_description(
        """What we like about these is no fuss, no mess. Get in and off they go."""
    )
    model_def.define_foamer_facts("""LNER EM1 (BR Class 76)""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=34940, unit_repeats=[1])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
