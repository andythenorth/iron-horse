# coding=utf-8


def main(): from train import EngineConsist, DieselEngineUnit
# for rest of stats, look up GE Evolution
    consist = EngineConsist(roster=roster,
                            id='evolucao',
                            base_numeric_id=200,
                            name='Evolução',
                            power=4400,
                            intro_date=1995)

    consist.add_unit(type=DieselEngineUnit,
                     weight=40,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
