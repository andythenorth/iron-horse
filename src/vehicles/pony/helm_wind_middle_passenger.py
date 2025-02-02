from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="TGVMiddlePassengerEngineConsist",
        id="helm_wind_middle_passenger",
        base_numeric_id=2890,
        name="Helm Wind Passenger Coach",
        subrole="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Helm Wind middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="ElectricHighSpeedPaxUnit",
        weight=42,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    consist_factory.define_description(
        """Can we get there faster? That's what drives me."""
    )
    consist_factory.define_foamer_facts(
        """BR InterCity 225 (Mk4 Coaches)), Shinkansen-style distributed traction"""
    )

    result.append(consist_factory)

    return result
