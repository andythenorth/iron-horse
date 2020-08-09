from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='ultra_shoebox',
                            base_numeric_id=2170,
                            name='Ultra Shoebox',
                            role='branch_express',
                            role_child_branch_num=1,
                            power=1600,
                            power_by_railtype={'RAIL': 1600, 'ELRL': 2600},
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=78,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.foamer_facts = """Network Rail / GBRF Class 73/9 (re-engineered)."""

    return consist
