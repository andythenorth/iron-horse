from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='super_shoebox',
                            base_numeric_id=880,
                            name='Super Shoebox',
                            role='branch_express',
                            role_child_branch_num=2,
                            power=1100,
                            power_by_railtype={'RAIL': 1100, 'ELRL': 2200},
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=66,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.foamer_facts = """BR Class 71/74, Class 73."""

    return consist
