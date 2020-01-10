from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='vanguard',
                            base_numeric_id=3090,
                            name='Vanguard',
                            role='heavy_express_1',
                            power=2550,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=2,  # let's not have everything turn up in 1990
                            fixed_run_cost_points=100, # give a bonus so this can be a genuine mixed-traffic engine
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
