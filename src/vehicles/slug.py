from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='slug',
                            base_numeric_id=1000,
                            name='Slug',
                            role='freight',
                            power=1750,
                            random_reverse=True,
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
