from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='grid_2',
                            base_numeric_id=3470,
                            name='Grid 2',
                            role='heavy_freight_1',
                            power=3500,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
