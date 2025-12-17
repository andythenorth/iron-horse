from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="re_430_lion",
        base_numeric_id=30520,
        name="Re 430 LION",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 7400,
        },
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Re 430 LION upgrade""")

    result.append(model_def)

    return result
