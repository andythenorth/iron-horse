from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='griffon',
                            base_numeric_id=2840,
                            name='Griffon',
                            role='express_1',
                            power=1650,
                            random_reverse=True,
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=74,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
