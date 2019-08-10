from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='pegasus',
                            base_numeric_id=300,
                            name='2-8-2 Pegasus',
                            role='heavy_express_1',
                            power=2000,
                            tractive_effort_coefficient=0.25,
                            gen=3,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     effect_offsets=[(-3, 0), (-2, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
