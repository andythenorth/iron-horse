from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='phoenix',
                            base_numeric_id=160,
                            name='Phoenix',
                            role='freight_1',
                            power=1900,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
