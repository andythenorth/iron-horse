from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='bright_country',
                                                  base_numeric_id=3800,
                                                  name='Bright Country',
                                                  role='luxury_pax_railcar',
                                                  power=900,
                                                  pantograph_type='z-shaped-single-with-base',
                                                  gen=6,
                                                  sprites_complete=False)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=58,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
