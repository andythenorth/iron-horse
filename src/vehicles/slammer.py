from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main():
    consist = PassengerEngineRailcarConsist(id='slammer',
                                            base_numeric_id=470,
                                            name='Slammer',
                                            role='pax_railcar',
                                            power=300,
                                            gen=4,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=37,
                     vehicle_length=8,
                     capacity=40,
                     chassis='railcar')

    return consist
