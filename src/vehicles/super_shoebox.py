from train import EngineConsist, ElectroDieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='super_shoebox',
                            base_numeric_id=880,
                            name='Super Shoebox',
                            role='branch_express',
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

    return consist
