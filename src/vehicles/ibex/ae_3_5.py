from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="ae_3_5",
        base_numeric_id=30780,
        name="Ae 3/5",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            # "OHLE": 1100,
            "OHLE": 10,
        },
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Ae 3/5""")

    result.append(model_def)

    return result
