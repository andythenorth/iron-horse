from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='baby_boat',
                            base_numeric_id=1590,
                            name='Baby Boat',
                            power=1800,
                            intro_date=1978)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
