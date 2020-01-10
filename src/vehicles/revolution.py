from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='revolution',
                            base_numeric_id=3500,
                            name='Revolution',
                            role='heavy_express_2',
                            power=2800,
                            power_by_railtype={'RAIL': 2800, 'ELRL': 5400}, # big jump in elrl HP by design compared to Fury
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=6,
                            intro_date_offset=-2,  # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=95,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
