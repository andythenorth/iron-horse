from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="keen",
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
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
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

    return result
