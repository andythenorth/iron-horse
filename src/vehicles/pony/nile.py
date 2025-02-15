from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="nile",
        base_numeric_id=21820,
        name="2-6-0+0-6-2 Nile",
        subrole="universal",
        subrole_child_branch_num=-5,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 900,
        },
        tractive_effort_coefficient=0.31,
        gen=2,
        intro_year_offset=10,  # introduce a bit later
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEngineUnit",
        weight=65,
        vehicle_length=8,
        effect_offsets=[(-1, 0)],  # non-standard smoke position
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    model_def.define_description("""Is twice as nice.""")
    model_def.define_foamer_facts("""Victorian Railways G class Garratt locomotives""")

    result.append(model_def)

    return result
