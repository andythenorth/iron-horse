from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="cc_7100",
        base_numeric_id=31140,
        name="CC 7100",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={"OHLE": 5300},
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
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
    model_def.define_foamer_facts("""SNCF CC 7100""")

    result.append(model_def)

    return result
