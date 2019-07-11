from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='pegasus',
                            base_numeric_id=300,
                            name='2-8-2 Pegasus',
                            role='heavy_express_1',
                            power=2000,
                            tractive_effort_coefficient=0.25,
                            buy_cost=81,
                            gen=3)

    consist.add_unit(type=SteamEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
