from train import PassengerVeryHighSpeedCabEngineConsist, ElectricHighSpeedPaxUnit


def main(roster):
    consist = PassengerVeryHighSpeedCabEngineConsist(roster=roster,
                                                     id='helm_wind_cab',
                                                     base_numeric_id=3060,
                                                     name='Helm Wind - Cab',
                                                     role='pax_high_speed',
                                                     power=1600,
                                                     dual_headed=True,
                                                     pantograph_type='z-shaped-single',
                                                     gen=5,
                                                     intro_date_offset=-3)  # introduce earlier than gen epoch by design

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=31,
                     vehicle_length=8,
                     # no pax capacity on Helm Wind cabs
                     spriterow_num=0,
                     chassis='4_axle_solid_express_32px')

    return consist
