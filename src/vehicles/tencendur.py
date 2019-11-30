from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='tencendur',
                            base_numeric_id=890,
                            name='4-4-0 Tencendur',
                            role='express_1',
                            power=1250,
                            tractive_effort_coefficient=0.18,
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
