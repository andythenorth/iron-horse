from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="fs_e636",
        base_numeric_id=140,
        name="FS E.636",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={"DC": 4200},
        random_reverse=True,
        gen=3,
        # pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    # !!! these are only 60 foot long IRL so 2x 4/8 units

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=4,
        rel_spriterow_index=0,
    )
    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""FS E.636""")

    result.append(model_def)

    return result
