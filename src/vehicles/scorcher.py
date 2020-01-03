from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='scorcher',
                            base_numeric_id=3320,
                            name='Scorcher HST',
                            role='hst', # quite a specific role, may or may not scale to other rosters
                            power=6600,
                            dual_headed=True,
                            intro_date_offset=-10,  # let's be a little bit earlier for this one - keep match to HST coaches
                            gen=6,
                            fixed_run_cost_points=280, # give a malus to this one (balancing eh?)
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=70,
                     vehicle_length=8,
                     effect_offsets=[(0, 1), (0, -1)], # double the smoke eh?
                     spriterow_num=0,
                     tail_light='hst_32px_1')

    return consist
