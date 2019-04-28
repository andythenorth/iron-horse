from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='tin_rocket',
                                            base_numeric_id=530,
                                            name='Tin Rocket',
                                            role='pax_railcar_1',
                                            power=400,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=40,
                     vehicle_length=8,
                     chassis='railcar_32px')

    return consist
