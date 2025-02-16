from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="higuma",
        base_numeric_id=30870,
        name="Higuma",
        subrole="express",
        subrole_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1600,  # breaks the 300 hp step size, but eh, lots of precedent  1800 hp would be too much?
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "SWOOSH", "SWOOSH"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=60,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # https://en.wikipedia.org/wiki/New_Zealand_DL_class_locomotive
    # https://en.wikipedia.org/wiki/New_Zealand_DM_class_locomotive
    model_def.define_description("""A tiny mighty bear.""")
    model_def.define_foamer_facts(
        """KiwiRail Stadler SALi locomotives, Kawasaki (Japan) Class DF200-7000 bo-bo-bo (dedicated locomotive for JR Kysushu <i>Seven Stars in Kyushu</i> luxury train)"""
    )

    result.append(model_def)

    return result
