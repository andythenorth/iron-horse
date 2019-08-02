from train import EngineConsist, DieselEngineUnit

# deprecated Dec 2018
# - can't make the 16/8 length work in a way that fits power progression + fits buy menu
# - shorter lengths run up against problem that HSTs 'only look right with all lux cars', but then integer lengths fail

# no wagon attach cb should be used, let them eat cake etc.


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='blaze',
                            base_numeric_id=3330,
                            name='Blaze HST',
                            role='hst', # quite a specific role, may or may not scale to other rosters
                            power=5500,
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                            dual_headed=True,
                            intro_date_offset=-10,  # let's be a little bit earlier for this one - keep coaches matched
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=70,
                     vehicle_length=8,
                     spriterow_num=0,
                     tail_light='hst_32px_1')

    return consist
