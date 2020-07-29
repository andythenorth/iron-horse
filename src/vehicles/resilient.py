from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='resilient',
                            base_numeric_id=4940,
                            name='Resilient',
                            role='heavy_express',
                            role_child_branch_num=-1,
                            power=2550,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=4,  # let's not have everything turn up in 1990
                            fixed_run_cost_points=100, # give a bonus so this can be a genuine mixed-traffic engine
                            cc_livery_keys=['FREIGHTLINER', 'RAILFREIGHT_TRIPLE_GREY'], # tried liveries for RES, etc, not convinced
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
