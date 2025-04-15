from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="lebeche",
        base_numeric_id=30570,
        name="Lebeche",
        subrole="universal",
        subrole_child_branch_num=5,
        power_by_power_source={
            "DIESEL": 1200,
        },
        random_reverse=True,
        base_track_type="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        # additional_liveries=["SWOOSH", "INDUSTRIAL_YELLOW"],
        liveries=["VANILLA"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=52,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description("""For new times. This is the zippy one.""")
    model_def.define_foamer_facts("""Euskotren TD 2000 Series""")

    result.append(model_def)

    return result
