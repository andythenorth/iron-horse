from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='blackthorn',
                            base_numeric_id=3470,
                            name='Blackthorn',
                            role='heavy_freight',
                            role_child_branch_num=1,
                            power=3650, # progression calculated to maintain hp/speed ratio from previous gen
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """I've fitted a bigger engine into the Grid.  Still not bad at all."""
    consist.cite = """Mr. Train"""

    return consist
