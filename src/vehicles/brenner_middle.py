from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricHighSpeedPaxUnit


def main(roster):
    consist = PassengerVeryHighSpeedMiddleEngineConsist(roster=roster,
                                                        id='brenner_middle',
                                                        base_numeric_id=2880,
                                                        name='Brenner - Middle',
                                                        role='pax_high_speed',
                                                        pantograph_type='z-shaped-single',
                                                        power=0,  # set power 0, when attached to correct cab, cab power will be increased
                                                        gen=6,
                                                        intro_date_offset=-3)  # introduce earlier than gen epoch by design

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=55,
                     vehicle_length=8,
                     capacity=40,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_articulated_32px',
                     repeat=2)

    return consist
