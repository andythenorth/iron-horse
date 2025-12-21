from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="backbone",
        base_numeric_id=15300,
        name="2-8-2 Backbone",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 2400,
        },
        tractive_effort_coefficient=0.29,
        gen=3,
        liveries=["WORKHORSE", "STOCK_STANDARD", "FREIGHT_BLACK"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=110,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=50,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Put it on the job and let it work.""")
    model_def.define_foamer_facts("""LMS Stanier 8F, WD Austerity 2-10-0, LNER P1 2-8-2""")

    result.append(model_def)

    return result
