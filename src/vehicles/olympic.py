from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='olympic',
                                                  base_numeric_id=3770,
                                                  name='Olympic',
                                                  role='express_emu',
                                                  power=750,
                                                  pantograph_type='z-shaped-single-with-base',
                                                  gen=5,
                                                  speed=110,
                                                  replacement_consist_id='revolution', # !!! hax
                                                  sprites_complete=False)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=55,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
