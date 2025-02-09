from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="sbb_fb_4_4",
        base_numeric_id=35020,
        name="SBB Sb 4/4",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            # "AC": 1700,
            "AC": 10,
        },
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=-5,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""SBB Fb 4/4""")

    result.append(model_def)

    return result
