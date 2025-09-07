from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="de_6_6",
        base_numeric_id=34760,
        name="De 6/6 Seetal Krokodil",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 1200,
        },
        speed=60,  # spans 2 generations
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB De 6/6 <i>Seetal Krokodil</i>""")

    result.append(model_def)

    return result
