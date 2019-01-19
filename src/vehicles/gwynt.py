from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main():
    consist = EngineConsist(id='gwynt',
                            base_numeric_id=380,
                            name='0-6-0 Gwynt',
                            role='freight',
                            power=1100,
                            tractive_effort_coefficient=0.24,
                            gen=1)

    consist.add_unit(type=SteamEngineUnit,
                     weight=59,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
