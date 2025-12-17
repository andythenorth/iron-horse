from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="braf",
        base_numeric_id=0,
        name="2-6-0 Braf",  # Welsh for "fine, nice, pleasant" https://omniglot.com/language/weather/welsh.htm
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=5,  # introduce later than gen epoch by design
        liveries=["STOCK_STANDARD", "WORKHORSE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=65,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=29,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Solid little number these. No bother.""")
    model_def.define_foamer_facts("""GWR 4300 Class, LBSCR K Class""")

    result.append(model_def)

    return result
