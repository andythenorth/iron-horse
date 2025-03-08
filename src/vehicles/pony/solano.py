from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="solano",
        base_numeric_id=21810,
        name="Solano",
        subrole="universal",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=42,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description("""Let a bit of sun in, I say.""")
    # https://en.wikipedia.org/wiki/New_Zealand_DE_class_locomotive, also NZ Di class
    # nah it's CP_Class_9020 now, and rename from Silverfern
    # see also https://trainspo.com/photo/98083/
    model_def.define_foamer_facts(""" Portugese CP Class 9020 (Alstom AD 12 B)""")

    result.append(model_def)

    return result
