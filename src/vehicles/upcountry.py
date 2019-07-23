from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='upcountry',
                            base_numeric_id=230,
                            name='4-6-0 Upcountry',
                            role='heavy_express_1',
                            power=1500,
                            tractive_effort_coefficient=0.18,
                            gen=2,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=90,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
