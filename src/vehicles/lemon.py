from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='lemon',
                            base_numeric_id=270,
                            name='4-8-0 Lemon',
                            role='heavy_freight_1',
                            power=2400,
                            tractive_effort_coefficient=0.29,
                            gen=3,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=115,
                     vehicle_length=8,
                     effect_offsets=[(-3, 0), (-2, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=50,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
