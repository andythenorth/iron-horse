from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="hawkinge",
        base_numeric_id=6410,
        name="4-8-2 Hawkinge",
        subrole="super_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 2350,
        },
        tractive_effort_coefficient=0.25,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["SURE_PACE", "STOCK_STANDARD", "WORKHORSE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=124,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=32,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Mr. Bulleid designed these. Do you like 'em?""")
    model_def.define_foamer_facts(
        """SR Merchant Navy / West Country / Battle of Britain classes"""
    )

    result.append(model_def)

    return result
