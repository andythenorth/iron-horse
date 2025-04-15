from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="boar_cat",
        base_numeric_id=21270,
        name="Boar Cat",
        subrole="universal",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 600,
        },
        random_reverse=True,
        base_track_type="NG",
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=23,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description("""This is a big small cat.""")
    model_def.define_foamer_facts(
        """Corsican CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=910, unit_repeats=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported
    # but the *buy menu* compositor does not support that as of Jan 2024, so hax
    model_def_clone.unit_defs[0].rel_spriterow_index = 1
    model_def_clone.add_unit_def(
        class_name="DieselEngineUnit",
        weight=23,
        vehicle_length=4,
        rel_spriterow_index=0,
    )

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
