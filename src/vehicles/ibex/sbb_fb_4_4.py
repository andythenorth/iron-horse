from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="sbb_fb_4_4",
        base_numeric_id=35020,
        name="SBB Sb 4/4",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            # "OHLE": 1700,
            "OHLE": 10,
        },
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=-5,  # introduce earlier than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=75,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Fb 4/4""")

    result.append(model_def)

    return result
