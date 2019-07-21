from train import EngineConsist, SteamEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='lark',
                            base_numeric_id=110,
                            name='4-4-2 Lark',
                            role='branch_express_1',
                            power=500,
                            tractive_effort_coefficient=0.2,
                            fixed_run_cost_points=105, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=1)

    consist.add_unit(type=SteamEngineUnit,
                     weight=35,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
