from train import TGVMiddlePassengerEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id, **kwargs):
    consist = TGVMiddlePassengerEngineConsist(
        roster_id=roster_id,
        id="rapide_middle_passenger",
        base_numeric_id=440,
        name="Rapide Passenger Coach",
        role="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Alizé middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricHighSpeedPaxUnit,
        weight=42,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={}, # suppress visual effects
    )

    consist.description = """"""
    consist.foamer_facts = """TGV Sud-Est, with TGV 001-style distributed traction"""

    return consist
