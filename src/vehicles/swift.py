from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='swift',
                            base_numeric_id=230,
                            name='4-4-2 Swift',
                            role='heavy_express',
                            role_child_branch_num=1,
                            power=1550,
                            tractive_effort_coefficient=0.18,
                            gen=2,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=90,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
