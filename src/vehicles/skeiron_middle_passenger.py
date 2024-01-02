from train import TGVMiddlePassengerEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id):
    consist = TGVMiddlePassengerEngineConsist(
        roster_id=roster_id,
        id="skeiron_middle_passenger",
        base_numeric_id=420,
        name="Skeiron Passenger Coach",
        role="very_high_speed",
        pantograph_type="z-shaped-single-with-base",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricHighSpeedPaxUnit,
        weight=54,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
    )

    consist.description = """."""
    consist.foamer_facts = """ """

    return consist
