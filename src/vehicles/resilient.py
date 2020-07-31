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
                            alternative_cc_livery='FREIGHTLINER', # tried liveries for RES, etc, not convinced
                            default_livery_extra_docs_examples=[('COLOUR_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """I've completely rebuilt some Intrepids, we might get another fifty years out of them."""
    consist.cite = """Mr. Train"""

    return consist
