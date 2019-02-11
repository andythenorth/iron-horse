from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='deasil',
                                            base_numeric_id=1770,
                                            name='Deasil',
                                            role='pax_railcar_1',
                                            power=200,
                                            gen=3,
                                            sprites_complete=False,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=30,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
