from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='pullman',
                            base_numeric_id=3830,
                            name='Pullman',
                            role='hst', # quite a specific role, may or may not scale to other rosters
                            power=2500, # it's quite under-powered, only for short trains
                            dual_headed=True,
                            gen=4,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=65,
                     vehicle_length=8,
                     effect_offsets=[(0, 1), (0, -1)], # double the smoke eh?
                     spriterow_num=0,
                     tail_light='hst_32px_1')

    return consist
