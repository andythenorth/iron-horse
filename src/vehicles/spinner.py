from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='spinner',
                            base_numeric_id=480,
                            name='4-2-2 Spinner',
                            role='express_1',
                            power=950,
                            tractive_effort_coefficient=0.12,
                            fixed_run_cost_points=160, # minor cost bonus so it can make money
                            gen=1,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=48,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
