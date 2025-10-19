from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="high_power_railcar_4",
        base_numeric_id=35210,
        name="SOB ABe 4/4 71",
        subrole="high_power_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 2600,
        },
        random_reverse=True,
        gen=4,
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
    model_def.define_foamer_facts("""SBB RBe 4/4, SOB ABe 4/4 71""")

    result.append(model_def)

    return result
