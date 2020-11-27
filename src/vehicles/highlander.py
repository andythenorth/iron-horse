from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='highlander',
                            base_numeric_id=4250,
                            name='Highlander',
                            role='heavy_freight',
                            role_child_branch_num=2,
                            power=4550, # 900hp steps Revolution -> Blackthorn -> Toaster
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=-1,  # let's be a little bit earlier for this one
                            gen=6,
                            fixed_run_cost_points=220, # unrealism: run cost nerf for being so high-powered
                            alternative_cc_livery='FREIGHTLINER_GBRF',
                            default_livery_extra_docs_examples=[('COLOUR_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=128,
                     vehicle_length=8,
                     effect_offsets=[(1, 0)],
                     spriterow_num=0)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
