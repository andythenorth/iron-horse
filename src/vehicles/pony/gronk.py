from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="gronk",
        base_numeric_id=21490,
        name="Gronk",
        subrole="gronk",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        intro_year_offset=-9,  # introduce much earlier than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        liveries=["STOCK_STANDARD", "CONVENTIONAL_WISDOM", "BANGER_BLUE", "FREIGHT_BLACK", "SHOW_PONY", "INDUSTRIAL_YELLOW", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=55,
        vehicle_length=4,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """The universal shunter.  Goes everywhere&hellip;slowly."""
    )
    model_def.define_foamer_facts("""BR Class 08/09, BR Class 13""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=520, unit_repeats=[1])

    model_def_clone.unit_defs[0].rel_spriterow_index = 1
    model_def_clone.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=55,
        vehicle_length=4,
        rel_spriterow_index=0,
    )

    # JFDI, the single unit should randomly reverse, the 2-unit version should not, so hax
    model_def_clone.random_reverse = False

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
