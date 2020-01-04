from train import PassengerEngineLuxuryRailcarConsist, ElectricLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(roster_id=roster_id,
                                                  id='sunshine_coast',
                                                  base_numeric_id=3040,
                                                  name='Sunshine Coast',
                                                  role='express_emu',
                                                  power=600,
                                                  pantograph_type='z-shaped-single-with-base',
                                                  gen=4,
                                                  speed=105,
                                                  replacement_consist_id='revolution', # !!! hax
                                                  sprites_complete=False)

    consist.add_unit(type=ElectricLuxuryRailcarPaxUnit,
                     weight=52,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
