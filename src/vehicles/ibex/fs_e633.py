from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="fs_e633",
        base_numeric_id=20860,
        name="FS E.633 Tigre",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "OHLE": 6000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce earler than gen epoch by design
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
    model_def.define_foamer_facts("""FS E.633 Bo-Bo-Bo Tigre""")

    result.append(model_def)

    return result
