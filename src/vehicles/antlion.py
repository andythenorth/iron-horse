from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='antlion',
                            base_numeric_id=1550,
                            name='Antlion',
                            power=350,
                            intro_date=1950)

    consist.add_unit(type=DieselEngineUnit,
                     weight=75,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
