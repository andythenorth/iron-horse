from train import EngineConsist, ElectroDieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='electro_turtle',
                            base_numeric_id=3500,
                            name='Electro Turtle',
                            role='heavy_express_1',
                            power=2750,
                            power_by_railtype={'RAIL': 2750, 'ELRL': 4500},
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=6,
                            sprites_complete=False)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=86,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
