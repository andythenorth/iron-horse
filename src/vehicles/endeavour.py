from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='endeavour',
                            base_numeric_id=4250,
                            name='Endeavour',
                            role='heavy_freight',
                            role_child_branch_num=-2, # -ve because Joker
                            power=4650,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=3,  # let's be a little bit later for this one
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """An up-to-date version of the Cheddar Valley.  I was right glad about this one."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """EMD / Progress Rail JT42CWR (Class 66), uprated Cat C series primer mover."""

    return consist
