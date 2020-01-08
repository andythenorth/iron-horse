from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='high_flyer',
                                                  base_numeric_id=4220,
                                                  name='High Flyer',
                                                  role='luxury_pax_railcar',
                                                  power=450,
                                                  pantograph_type='z-shaped-single-with-base',
                                                  gen=3,
                                                  intro_date_offset=2,  # introduce later by design
                                                  sprites_complete=False)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=51,
                     chassis='railcar_solid_32px',
                     tail_light='railcar_32px_3')

    return consist
