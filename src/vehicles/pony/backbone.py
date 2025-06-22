from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
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
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=110,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=50,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""LMS Stanier 8F, WD Austerity 2-10-0""")

    result.append(model_def)

    return result
