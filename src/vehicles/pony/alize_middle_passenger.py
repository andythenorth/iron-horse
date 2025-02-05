from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="TGVMiddlePassengerEngineConsist",
        id="alize_middle_passenger",
        base_numeric_id=350,
        name="Alizé Passenger Coach",
        subrole="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Alizé middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="ElectricHighSpeedPaxUnit",
        weight=42,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_type_factory.define_description("""""")
    model_type_factory.define_foamer_facts(
        """TGV Sud-Est, with TGV 001-style distributed traction"""
    )

    result.append(model_type_factory)

    return result
