from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="plm_2cc2_3400",
        base_numeric_id=150,
        name="PLM 2CC2 3400",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={"OHLE": 4600},
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce much later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=8,
        rel_spriterow_index=0,
        repeat=2,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""PLM 2CC2 3400""")

    result.append(model_def)

    return result
