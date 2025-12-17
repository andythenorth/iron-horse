from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="bb_25200",
        base_numeric_id=34690,
        name="BB 25200",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={"OHLE": 4600},
        random_reverse=True,
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
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
    model_def.define_foamer_facts("""SNCF BB 25200 !! multisystem""")

    result.append(model_def)

    return result
