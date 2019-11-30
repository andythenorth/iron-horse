from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='patagonia',
                            base_numeric_id=330,
                            name='Patagonia',
                            base_track_type='NG',
                            power=500,
                            intro_date=1960)

    consist.add_unit(type=DieselEngineUnit,
                     weight=20,
                     vehicle_length=7,
                     capacity=35,
                     spriterow_num=0)

    consist.add_unit(type=DieselEngineUnit,
                     weight=20,
                     vehicle_length=7,
                     capacity=35,
                     spriterow_num=1)

    return consist
