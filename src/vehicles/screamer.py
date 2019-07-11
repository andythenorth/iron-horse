from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='screamer',
                            base_numeric_id=450,
                            name='Screamer',
                            role='heavy_express_2',
                            power=5000,
                            random_reverse=True,
                            gen=5,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=5,   # introduce later than gen epoch by design
                            replacement_consist_id='revolution', # this line ends with Screamer and is merged to heavy_express_3
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=85,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
