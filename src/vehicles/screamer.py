from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='screamer',
                            base_numeric_id=450,
                            name='Screamer',
                            role='heavy_express_4',
                            power=6000,
                            random_reverse=True,
                            gen=5,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=3,   # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=85,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
