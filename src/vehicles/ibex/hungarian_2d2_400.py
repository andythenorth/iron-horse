from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="hungarian_2d2_400",
        base_numeric_id=30800,
        name="Hungarian 2D2 400",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "OHLE": 4800,  # not linear steps in this line
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
    model_def.define_foamer_facts("""PO <i>Hungarian</i> 2D2 400 (or 2-B-B-2)""")

    result.append(model_def)

    return result
