from train import EngineConsist, DieselEngineUnit


def main():
    consist = EngineConsist(id='smokey_mountain',
                            base_numeric_id=1610,
                            name='Smokey Mountain',
                            power=3200,
                            intro_date=1950)

    consist.add_unit(type=DieselEngineUnit,
                     weight=112,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.add_unit(type=DieselEngineUnit,
                     weight=112,
                     vehicle_length=8,
                     spriterow_num=1)

    return consist
