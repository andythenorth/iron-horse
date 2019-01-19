from train import EngineConsist, DieselEngineUnit


def main():
    consist = EngineConsist(id='waterbuck',
                            base_numeric_id=2020,
                            name='Waterbuck',
                            power=2200,
                            base_track_type='NG',
                            intro_date=1990)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
