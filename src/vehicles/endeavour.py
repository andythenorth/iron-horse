from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='endeavour',
                            base_numeric_id=4250,
                            name='Endeavour',
                            role='heavy_freight',
                            role_child_branch_num=-1, # Joker eh, it's a 66
                            power=3600,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=-2,  # let's be a little bit earlier for this one
                            gen=6,
                            alternative_cc_livery='FREIGHTLINER_GBRF',
                            default_livery_extra_docs_examples=[('COLOUR_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """Cut-price version of the Cheddar Valley. Cheaper to buy. Cheaper to run. Less power mind you."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """EMD / Progress Rail JT42CWR (Class 66)."""

    return consist
