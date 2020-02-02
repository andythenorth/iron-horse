from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='olympic',
                                                  base_numeric_id=3770,
                                                  name='Olympic',
                                                  role='luxury_pax_railcar',
                                                  power=750,
                                                  pantograph_type='z-shaped-single-with-base',
                                                  gen=5,
                                                  intro_date_offset=1,  # introduce later by design
                                                  sprites_complete=True)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=55,
                     chassis='railcar_solid_32px',
                     tail_light='railcar_32px_3')

    return consist
