from train import PassengerEngineExpressMUConsist, ElectricRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineExpressMUConsist(roster_id=roster_id,
                                              id='olympic',
                                              base_numeric_id=3040,
                                              name='Olympic',
                                              role='express_emu',
                                              power=1200, # balanced against Roarer somewhat
                                              pantograph_type='z-shaped-single-with-base',
                                              gen=4,
                                              sprites_complete=False,
                                              intro_date_offset=3)  # introduce later by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=52,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
