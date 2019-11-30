from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='cheese_bug',
                            base_numeric_id=490,
                            name='2-6-2 Cheese Bug',
                            role='universal',
                            base_track_type='NG',
                            power=350,
                            tractive_effort_coefficient=0.2,
                            gen=1,
                            random_reverse=True,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=16,
                     vehicle_length=4,
                     effect_z_offset=10, # reduce smoke z position to suit NG engine height
                     spriterow_num=0)

    return consist
