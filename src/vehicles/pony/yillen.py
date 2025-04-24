from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="yillen",
        base_numeric_id=6370,
        name="Yillen",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a little earlier for this one
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    # 2 separate units so that buy menu has reversed cabs
    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=67,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=67,
        vehicle_length=5,
        rel_spriterow_index=1,
    )

    model_def.define_description("""The universe is asymmetric. And so are these.""")
    model_def.define_foamer_facts("""BR Class 15, BR Class 16""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=29080, unit_repeats=[1, 0])

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_def_clone.random_reverse = True

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
