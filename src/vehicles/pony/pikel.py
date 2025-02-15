from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="pikel",
        base_numeric_id=21100,
        name="Pikel",
        subrole="universal",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 600,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=-2,  # introduce a bit earlier
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=22,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    model_def.define_description(
        """This diesel engine modernises our narrow gauge lines."""
    )
    model_def.define_foamer_facts(
        """FAUR L45H B-B, generic narrow-gauge diesel locomotives"""
    )

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=920, unit_repeats=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported
    # but the *buy menu* compositor does not support that as of Jan 2024, so hax
    model_def.unit_defs[0].spriterow_num = 1
    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=22, vehicle_length=4, spriterow_num=0
    )

    model_def.complete_clone()

    result.append(model_def)

    return result
