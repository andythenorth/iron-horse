from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='duff',
                            base_numeric_id=4810,
                            name='Duff',
                            role='heavy_express',
                            role_child_branch_num=-1, # -ve because Joker
                            power=2200,
                            random_reverse=True,
                            gen=4,
                            fixed_run_cost_points=60, # give a bonus so this can be a genuine mixed-traffic engine
                            intro_date_offset=8,  # let's be quite a lot later for this one
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
