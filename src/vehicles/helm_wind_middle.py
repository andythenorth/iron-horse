from train import PassengerVeryHighSpeedMiddleEngineConsist, ElectricHighSpeedPaxUnit


def main():
    consist = PassengerVeryHighSpeedMiddleEngineConsist(id='helm_wind_middle',
                                                        base_numeric_id=2890,
                                                        name='Helm Wind - Middle',
                                                        role='pax_high_speed',
                                                        power=0,  # set power 0, when attached to correct cab, cab power will be increased
                                                        pantograph_type='z-shaped-single',
                                                        gen=4,
                                                        intro_date_offset=20)  # introduce later than gen epoch by design

    # 4 units (2-tiles) because building these is annoying if the units are too small?
    # or 2 units (1-tile) to make any integer length?

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=31,
                     vehicle_length=8,
                     capacity=40,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_articulated_32px',
                     repeat=2)

    return consist
