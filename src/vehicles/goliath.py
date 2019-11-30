from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='goliath',
                            base_numeric_id=780,
                            name='Goliath',
                            role='branch_freight',
                            power=1450,
                            random_reverse=True,
                            gen=6,
                            intro_date_offset=2, # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=74,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
