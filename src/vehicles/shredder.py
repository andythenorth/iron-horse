from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='shredder',
                            base_numeric_id=2830,
                            name='Shredder',
                            role='express_1',
                            power=1850,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=76,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
