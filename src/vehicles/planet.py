from train import EngineConsist, DieselEngineUnit


def main():
    consist = EngineConsist(id='planet',
                            base_numeric_id=360,
                            name='Planet',
                            base_track_type='NG',
                            power=500,
                            intro_date=1950)

    consist.add_unit(type=DieselEngineUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
