from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='vigilant',
                            base_numeric_id=4870,
                            name='2-8-0 Vigilant',
                            role='heavy_freight',
                            role_child_branch_num=1,
                            power=1850,
                            tractive_effort_coefficient=0.32,
                            fixed_run_cost_points=245, # cost malus, early heavy freight engines are too cheap to run relative to smaller engines
                            gen=2,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=92,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
