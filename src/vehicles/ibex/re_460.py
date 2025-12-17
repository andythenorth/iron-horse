from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="re_460",
        base_numeric_id=31840,
        name="Re 460",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=4,
        power_by_power_source={
            "OHLE": 8400,
        },
        random_reverse=True,
        gen=5,
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
    model_def.define_foamer_facts("""SBB Re 460""")

    result.append(model_def)

    return result
