from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="constance",
        base_numeric_id=20950,
        name="Constance",
        subrole="heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
            "OHLE": 4200,  # yes it's the very close on both, just the effect changes; this is a tech tree cheat to get an extra ~3450 hp diesel and to get a 4200 hp electric
        },
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        liveries=["STOCK_STANDARD"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=95,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Runs like a Swiss watch.""")
    model_def.define_foamer_facts("""Siemens Vectron Dual Mode""")

    result.append(model_def)

    return result
