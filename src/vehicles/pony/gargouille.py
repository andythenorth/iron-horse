from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="gargouille",
        base_numeric_id=21400,
        name="Gargouille",
        subrole="universal",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type="NG",
        gen=3,
        intro_year_offset=-2,  # introduce a bit earlier
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        liveries=["CONVENTIONAL_WISDOM", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=40,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Le petit train du jour. I've imported a few of these."""
    )
    model_def.define_foamer_facts(
        """Corsican CFD Locotracteur BB-400, New Zealand DSG class"""
    )

    result.append(model_def)

    return result
