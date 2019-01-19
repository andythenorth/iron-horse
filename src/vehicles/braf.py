from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='braf',
                            base_numeric_id=0,
                            name='2-6-0 Braf',
                            role='freight',
                            power=1250,
                            tractive_effort_coefficient=0.24,
                            gen=2)

    consist.add_unit(type=SteamEngineUnit,
                     weight=68,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
