from train import EngineConsist, SteamEngineUnit

def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='grub',
                            base_numeric_id=4010,
                            name='Grub',
                            role='gronk!',
                            role_child_branch_num=-1,
                            power=350,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            fixed_run_cost_points=100, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=1,
                            vehicle_life=60, # extended vehicle life for all gronks eh
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=36,
                     vehicle_length=4,
                     spriterow_num=0)

    consist.foamer_facts = """GER G15/C53 tramway locomotives."""

    return consist
