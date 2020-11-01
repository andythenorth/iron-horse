from train import EngineConsist, DieselEngineUnit

def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='chuggypig',
                            base_numeric_id=4980,
                            name='Chuggypig',
                            role='gronk!',
                            role_child_branch_num=-2,
                            power=400,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            fixed_run_cost_points=100, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=4,
                            vehicle_life=60, # extended vehicle life for all gronks eh
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=48,
                     vehicle_length=4,
                     spriterow_num=0)

    consist.description = """No prizes for speed, but it gets a job done."""
    consist.foamer_facts = """Thomas Hill <i>Steelman</i>, BR Class 07, miscellaneous industrial diesel shunters"""

    return consist
