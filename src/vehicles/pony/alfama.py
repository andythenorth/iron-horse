from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="alfama",
        base_numeric_id=21670,
        name="0-4-4-0 Alfama",
        subrole="universal",
        subrole_child_branch_num=-2,
        base_track_type="NG",
        power_by_power_source={
            "STEAM": 600,
        },
        tractive_effort_coefficient=0.3,
        gen=2,
        # introduce early by design
        intro_year_offset=-10,
        random_reverse=True,
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=32,
        vehicle_length=6,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Dances with mid-power grace. Articulated finesse in every turn."""
    )
    model_def.define_foamer_facts(
        """Mallet locomotives used by Portugese narrow gauge railways"""
    )

    result.append(model_def)

    return result
