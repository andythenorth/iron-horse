from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='girt_licker',
                            base_numeric_id=70,
                            name='0-10-0 Girt Licker',
                            role='heavy_freight_1',
                            power=1800,
                            tractive_effort_coefficient=0.33,
                            gen=2,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=95,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
