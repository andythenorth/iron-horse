from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="keen",
        base_numeric_id=470,
        name="0-6-0+0-6-0 Keen",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1800,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=-13,  # introduce much earlier than gen epoch by design
        fixed_run_cost_points=240,  # adjust to match similar engines of same gen
        liveries=["BANGER_BLUE", "FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=58,
        vehicle_length=5,
        rel_spriterow_index=0,
        repeat=2,
    )

    model_def.define_description("""Gallop apace, you fiery-footed steeds.""")
    model_def.define_foamer_facts(
        """18in Hunslet tanks, Austerity tanks, LNER J94 Class"""
    )

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=22560, unit_repeats=[1, 0])

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_def_clone.random_reverse = True

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
