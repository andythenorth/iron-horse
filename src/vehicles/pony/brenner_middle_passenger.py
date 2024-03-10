from train import TGVMiddlePassengerEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id, **kwargs):
    consist = TGVMiddlePassengerEngineConsist(
        roster_id=roster_id,
        id="brenner_middle_passenger",
        base_numeric_id=2880,
        name="Brenner Passenger Coach",
        role="very_high_speed",
        pantograph_type="z-shaped-single-with-base",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricHighSpeedPaxUnit,
        weight=52,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={}, # suppress visual effects
    )

    consist.description = """And you shall know this velocity."""
    consist.foamer_facts = """Alstom Class 390 <i>Pendolino</i>"""

    return consist
