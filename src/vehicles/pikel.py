from train import EngineConsist, DieselEngineUnit


def main():
    consist = EngineConsist(id='pikel',
                            base_numeric_id=430,
                            name='Pikel',
                            role='universal',
                            power=650,
                            random_reverse=True,
                            base_track_type='NG',
                            gen=3,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=18,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
