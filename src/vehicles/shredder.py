from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='shredder',
                            base_numeric_id=2830,
                            name='Shredder',
                            role='express',
                            role_child_branch_num=1,
                            power=1800,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=76,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.foamer_facts = """BR Class 33, 	EMD JT42HW-HS (Class 67)."""

    return consist
