from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='buffalo',
                            base_numeric_id=4900,
                            name='0-6-2 Buffalo',
                            role='freight',
                            role_child_branch_num=-1,
                            power=650,
                            tractive_effort_coefficient=0.2,
                            fixed_run_cost_points=100, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=1,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=46,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
