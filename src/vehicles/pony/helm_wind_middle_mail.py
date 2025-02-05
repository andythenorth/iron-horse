from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="TGVMiddleMailEngineConsist",
        id="helm_wind_middle_mail",
        base_numeric_id=6740,
        name="Helm Wind Mail Van",
        subrole="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Helm Wind middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="ElectricHighSpeedMailUnit",
        weight=42,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_type_factory.define_description(
        """Can we get there faster? That's what drives me."""
    )
    model_type_factory.define_foamer_facts(
        """BR InterCity 225 (Mk4 Coaches)), Shinkansen-style distributed traction"""
    )

    result.append(model_type_factory)

    return result
