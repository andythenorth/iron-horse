from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='cheddar_valley',
                            base_numeric_id=220,
                            name='Cheddar Valley',
                            role='heavy_freight',
                            role_child_branch_num=2,
                            power=4450, # 850hp steps Revolution -> Endeavor -> Toaster
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=3,  # let's be a little bit later for this one
                            gen=5,
                            fixed_run_cost_points=210, # unrealism: run cost nerf for being so high-powered
                            alternative_cc_livery='YEOMAN',
                            default_livery_extra_docs_examples=[('COLOUR_GREEN', 'COLOUR_WHITE'), ('COLOUR_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """I shipped these in from overseas.  Pull you backwards through a wall this one will.  Right proper engine."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """GMD  / EMD Class 59, uprated GMD / EMD 710 series prime mover."""

    return consist
