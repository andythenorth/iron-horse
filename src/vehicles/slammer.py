from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='slammer',
                                            base_numeric_id=470,
                                            name='Slammer',
                                            role='pax_railcar_1',
                                            power=300,
                                            gen=4,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=37,
                     chassis='railcar_32px')

    return consist
