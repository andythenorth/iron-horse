from train import EngineConsist, SteamEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='merrylegs',
                            base_numeric_id=500,
                            name='2-6-2 Merrylegs',
                            role='branch_express_1',
                            power=650,
                            tractive_effort_coefficient=0.2,
                            fixed_run_cost_points=120, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=2,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=49,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
