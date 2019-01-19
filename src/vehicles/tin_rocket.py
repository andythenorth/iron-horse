from train import PassengerEngineRailcarConsist, DieselRailcarBaseUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='tin_rocket',
                                            base_numeric_id=530,
                                            name='Tin Rocket',
                                            role='pax_railcar',
                                            power=400,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=40,
                     vehicle_length=8,
                     capacity=40,
                     chassis='railcar')

    return consist
