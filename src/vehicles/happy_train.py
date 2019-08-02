from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='happy_train',
                                            base_numeric_id=100,
                                            name='Happy Train',
                                            role='pax_railcar_1',
                                            power=500,
                                            gen=6,
                                            intro_date_offset=-5,  # introduce early by design
                                            sprites_complete=True)

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=40,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
