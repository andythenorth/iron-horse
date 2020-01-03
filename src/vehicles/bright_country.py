from train import PassengerEngineExpressMUConsist, ElectricExpressMUPaxUnit


def main(roster_id):
    consist = PassengerEngineExpressMUConsist(roster_id=roster_id,
                                              id='bright_country',
                                              base_numeric_id=3800,
                                              name='Bright Country',
                                              role='express_emu',
                                              power=2200,
                                              pantograph_type='z-shaped-single-with-base',
                                              gen=6,
                                              sprites_complete=False,
                                              intro_date_offset=3)  # introduce later by design

    consist.add_unit(type=ElectricExpressMUPaxUnit,
                     weight=54,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist

