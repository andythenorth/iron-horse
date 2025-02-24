from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="krokodil_be_6_8",
        base_numeric_id=32850,
        name="SBB Be 6/8 ii Krokodil",
        subrole="super_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 3700,
        },
        gen=3,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        liveries=["VANILLA"],
        cabbage_new_livery_system=True,
        sprites_complete=False,
    )

    # 63ft IRL is 8/8, surprisingly short
    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Be 6/8 ii <i>Krokodil</i>""")

    result.append(model_def)

    return result
