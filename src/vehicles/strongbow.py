from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='strongbow',
                            base_numeric_id=4320,
                            name='4-6-0 Strongbow',
                            role='heavy_express',
                            role_child_branch_num=1,
                            power=1900, # not an exact linear progression in this tree
                            tractive_effort_coefficient=0.18,
                            gen=3,
                            fixed_run_cost_points=140, # give a bonus so this can be a genuine mixed-traffic engine
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=94,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=36,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
