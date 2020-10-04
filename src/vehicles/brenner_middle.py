from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id):
    consist = PassengerVeryHighSpeedMiddleEngineConsist(roster_id=roster_id,
                                                        id='brenner_middle',
                                                        base_numeric_id=2880,
                                                        name='Brenner Middle',
                                                        role='very_high_speed',
                                                        role_child_branch_num=2,
                                                        pantograph_type='z-shaped-single-with-base',
                                                        power=0,  # set power 0, when attached to correct cab, cab power will be increased
                                                        gen=6,
                                                        intro_date_offset=-3,  # introduce earlier than gen epoch by design
                                                        sprites_complete=True)

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=52,
                     spriterow_num=0,
                     chassis='jacobs_solid_express_32px',
                     repeat=2)

    consist.description = """And you shall know our velocity."""
    consist.foamer_facts = """Alstom Class 390 <i>Pendolino</i>."""

    return consist
