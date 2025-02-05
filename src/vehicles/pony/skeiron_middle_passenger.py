from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="TGVMiddlePassengerEngineConsist",
        id="skeiron_middle_passenger",
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

    model_type_factory.define_unit(
        class_name="ElectricHighSpeedPaxUnit",
        weight=54,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_type_factory.define_description(""".""")
    model_type_factory.define_foamer_facts(""" """)

    result.append(model_type_factory)

    return result
