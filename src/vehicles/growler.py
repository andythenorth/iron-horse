from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='growler',
                            base_numeric_id=2240,
                            name='Growler',
                            role='freight',
                            power=1600,
                            random_reverse=True,
                            gen=4,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
