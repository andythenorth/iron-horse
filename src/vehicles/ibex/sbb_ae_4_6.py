from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="sbb_ae_4_6",
        base_numeric_id=34960,
        name="Ae 4/6",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 4800,  # not linear steps in this line
        },
        random_reverse=True,
        gen=3,
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
    model_def.define_foamer_facts("""SBB Ae 4/6""")

    result.append(model_def)

    return result
