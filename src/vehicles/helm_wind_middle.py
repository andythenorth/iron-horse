from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricHighSpeedPaxUnit


def main(roster):
    consist = PassengerVeryHighSpeedMiddleEngineConsist(roster=roster,
                                                        id='helm_wind_middle',
                                                        base_numeric_id=2890,
                                                        name='Helm Wind - Middle',
                                                        role='pax_high_speed',
                                                        power=0,  # set power 0, when attached to correct cab, cab power will be increased
                                                        pantograph_type='z-shaped-single',
                                                        gen=5,
                                                        intro_date_offset=-3)  # introduce earlier than gen epoch by design

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=31,
                     vehicle_length=8,
                     capacity=40,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_articulated_32px',
                     repeat=2)

    return consist
