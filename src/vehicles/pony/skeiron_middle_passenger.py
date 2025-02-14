from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVMiddlePassengerEngineConsist",
        base_id="skeiron_middle_passenger",
        base_numeric_id=420,
        name="Skeiron Passenger Coach",
        subrole="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricHighSpeedPaxUnit",
        weight=54,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description(""".""")
    model_def.define_foamer_facts(""" """)

    result.append(model_def)

    return result
