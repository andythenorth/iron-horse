from train import EngineConsist, ElectroDieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='revolution',
                            base_numeric_id=3500,
                            name='Revolution',
                            role='heavy_express_3',
                            power=2800,
                            power_by_railtype={'RAIL': 2800, 'ELRL': 5400},
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=86,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
