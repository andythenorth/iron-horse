from train import PassengerEngineRailcarConsist, DieselRailcarBaseUnit


def main():
    consist = PassengerEngineRailcarConsist(id='deasil',
                                            base_numeric_id=1770,
                                            name='Deasil',
                                            role='pax_railcar',
                                            power=200,
                                            gen=3,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=30,
                     vehicle_length=8,
                     capacity=36,
                     chassis='railcar')

    return consist
