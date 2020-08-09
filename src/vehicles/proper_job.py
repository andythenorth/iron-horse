from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='proper_job',
                            base_numeric_id=1300,
                            name='2-6-2 Proper Job',
                            role='branch_express',
                            role_child_branch_num=1,
                            power=800,
                            gen=3,
                            tractive_effort_coefficient=0.2,
                            fixed_run_cost_points=120, # substantial cost bonus so it can make money
                            random_reverse=True,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=57,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.description = """For when you need proper engine at proper price. Proper Job."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """BR Standard Class 3, LMS Ivatt Class 2 and GWR 5101/6100 Class <i>Prairie Tanks</i>."""

    return consist
