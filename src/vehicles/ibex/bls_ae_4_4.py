from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="bls_ae_4_4",
        base_numeric_id=30930,
        name="BLS Ae 4/4",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "OHLE": 5300,  # unrealistically high, to fit to BLS Re 4/4 progression, which leans towards Swiss
        },
        random_reverse=True,
        gen=3,
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
    model_def.define_foamer_facts("""BLS Ae 4/4""")

    result.append(model_def)

    return result
