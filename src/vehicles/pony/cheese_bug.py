from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="cheese_bug",
        base_numeric_id=21060,
        name="2-6-2 Cheese Bug",
        subrole="universal",
        subrole_child_branch_num=-1,
        base_track_type="NG",
        power_by_power_source={
            "STEAM": 400,
        },
        tractive_effort_coefficient=0.2,
        gen=1,
        random_reverse=True,
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=18,
        vehicle_length=4,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description("""I present you this trusty little engine.""")
    model_def.define_foamer_facts("""generic narrow-gauge steam locomotives""")

    result.append(model_def)

    return result
