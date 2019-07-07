from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='haar',
                            base_numeric_id=1880,
                            name='0-8-0 Haar',
                            role='freight_1',
                            power=1450,
                            tractive_effort_coefficient=0.24,
                            gen=3,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=70,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
