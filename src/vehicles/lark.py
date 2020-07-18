from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='lark',
                            base_numeric_id=110,
                            name='4-4-2 Lark',
                            role='branch_express',
                            role_child_branch_num=1,
                            power=500,
                            tractive_effort_coefficient=0.2,
                            fixed_run_cost_points=100, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=1,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=35,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.description = """Sturdy tank engine!  Using a design licensed from Mr. William Adams, this engine will move small freight and passenger trains at low cost, and surprisingly high speed."""

    return consist
