from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='thunderbird',
                            base_numeric_id=3090,
                            name='Thunderbird',
                            role='heavy_express_1',
                            power=2800,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=-4,  # let's not have everything turn up in 1990
                            fixed_run_cost_points=100, # give a bonus so this can be a genuine mixed-traffic engine
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
