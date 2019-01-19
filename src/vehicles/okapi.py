from train import EngineConsist, DieselEngineUnit


def main():
    consist = EngineConsist(id='okapi',
                            base_numeric_id=1960,
                            name='Okapi',
                            power=1850,
                            base_track_type='NG',
                            intro_date=1958)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100,
                     vehicle_length=7,
                     spriterow_num=0)

    return consist
