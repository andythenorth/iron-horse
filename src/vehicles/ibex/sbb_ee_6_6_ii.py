from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="sbb_ee_6_6_ii",
        base_numeric_id=35220,
        name="SBB Ee 6/6 ii",
        subrole="super_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 4600,
        },
        gen=4,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    # 63ft IRL is 8/8, surprisingly short
    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Ee 6/6 ii""")

    result.append(model_def)

    return result
