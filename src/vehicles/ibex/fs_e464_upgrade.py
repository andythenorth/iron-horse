from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="fs_e464_upgrade",
        base_numeric_id=32750,
        name="FS E.464 (upgraded)",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={"AC": 4800},
        random_reverse=True,
        gen=6,
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
    model_def.define_foamer_facts("""FS E.464 (upgraded)""")

    result.append(model_def)

    return result
