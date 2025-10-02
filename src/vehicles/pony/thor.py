from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="thor",
        base_numeric_id=21330,
        name="0-4-4-0 Thor",
        subrole="universal",
        subrole_child_branch_num=2,
        base_track_type="NG",
        power_by_power_source={
            "STEAM": 600,
        },
        tractive_effort_coefficient=0.3,
        gen=1,
        intro_year_offset=15,
        random_reverse=True,
        liveries=["SHOW_PONY", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=30,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (1, 0)],  # double the smoke eh?
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """You could say it's twice the train. A god amongst engines."""
    )
    model_def.define_foamer_facts("""Fairlie locomotives""")

    result.append(model_def)

    return result
