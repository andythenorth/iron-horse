from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="higuma",
        base_numeric_id=16910,
        name="Higuma",
        subrole="universal",
        subrole_child_branch_num=-6,
        base_track_type="NG",
        power_by_power_source={
            "DIESEL": 1600,  # breaks the 300 hp step size, but eh, lots of precedent  1800 hp would be too much?
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        liveries=["CLASSIC_LINES", "SHOW_PONY", "SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=60,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    # https://en.wikipedia.org/wiki/New_Zealand_DL_class_locomotive
    # https://en.wikipedia.org/wiki/New_Zealand_DM_class_locomotive
    model_def.define_description("""A tiny mighty bear.""")
    model_def.define_foamer_facts(
        """KiwiRail Stadler SALi locomotives, Kawasaki (Japan) Class DF200-7000 bo-bo-bo (dedicated locomotive for JR Kysushu <i>Seven Stars in Kyushu</i> luxury train)"""
    )

    result.append(model_def)

    return result
