from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVMiddlePassengerEngine",
        model_id="alize_middle_passenger",
        cab_id="alize_cab",
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

    model_def.add_unit_def(
        class_name="ElectricHighSpeedPaxUnit",
        weight=42,
        rel_spriterow_index=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """TGV Sud-Est, with TGV 001-style distributed traction"""
    )

    result.append(model_def)

    return result
