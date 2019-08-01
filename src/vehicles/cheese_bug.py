from train import EngineConsist, SteamEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='cheese_bug',
                            base_numeric_id=490,
                            name='2-4-2 Cheese Bug',
                            role='universal',
                            base_track_type='NG',
                            power=350,
                            tractive_effort_coefficient=0.2,
                            gen=1,
                            random_reverse=True,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=16,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
