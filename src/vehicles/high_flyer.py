from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='high_flyer',
                                                  base_numeric_id=4220,
                                                  name='High Flyer',
                                                  role='luxury_pax_railcar',
                                                  role_child_branch_num=-1, # joker to hide them from simplified mode
                                                  power=450,
                                                  pantograph_type='diamond-single-with-base',
                                                  gen=3,
                                                  intro_date_offset=2,  # introduce later by design
                                                  sprites_complete=True)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=48,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    consist.description = """"""
    consist.cite = """Dr. Constance Speed"""
    consist.foamer_facts = """SR 5-BEL <i>Brighton Belle</i>."""

    return consist
