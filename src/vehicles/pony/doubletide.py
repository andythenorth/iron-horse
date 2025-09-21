from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="doubletide",
        base_numeric_id=220,
        name="Doubletide",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        # no replacement by design - continues to game end as 10/8, especially for industrial use etc
        power_by_power_source={
            "DIESEL": 2750,  # within range of Resilient
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=9,  # let's be quite a bit later for this one, Yillen is long-lived
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    # 2 separate units so that buy menu has reversed cabs
    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=68,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=68,
        vehicle_length=5,
        rel_spriterow_index=1,
    )

    #  guess the quote?
    model_def.define_description(
        """And ruined love when it is built anew grows fairer than at first, more strong, far greater."""
    )
    model_def.define_foamer_facts("""Re-engineered BR Class 15, BR Class 16""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=29090, unit_repeats=[1, 0])

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_def_clone.random_reverse = True

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
