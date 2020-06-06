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
                                                  intro_date_offset=1,  # introduce later by design
                                                  sprites_complete=True)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=47,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
