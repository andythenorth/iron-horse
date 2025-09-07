from train.factory import ModelDef

# multi-system !!


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="obb_1014",
        base_numeric_id=20010,
        name="OBB 1014",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 4800,
        },
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""OBB 1014""")

    result.append(model_def)

    return result
