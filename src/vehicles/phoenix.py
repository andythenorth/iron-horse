from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='phoenix',
                            base_numeric_id=160,
                            name='Phoenix',
                            role='freight',
                            role_child_branch_num=1,
                            power=2150, # progression calculated to maintain hp/speed ratio from previous gen
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """The Slugs were right knackered, so we've put a new engine in to make this."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """Class 37, re-engineered with new prime mover."""

    return consist
