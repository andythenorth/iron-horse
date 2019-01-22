from train import PassengerVeryHighSpeedCabEngineConsist, ElectricHighSpeedPaxUnit


def main(roster):
    consist = PassengerVeryHighSpeedCabEngineConsist(roster=roster,
                                                     id='brenner_cab',
                                                     base_numeric_id=130,
                                                     name='Brenner - Cab',
                                                     role='pax_high_speed',
                                                     dual_headed=True,
                                                     power=3000,
                                                     gen=6,
                                                     intro_date_offset=-3)  # introduce earlier than gen epoch by design

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=55,
                     vehicle_length=8,
                     # add pax capacity on Brenner cabs
                     capacity=40,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_32px')

    return consist
