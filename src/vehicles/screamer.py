from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='screamer',
                            base_numeric_id=450,
                            name='Screamer',
                            role='heavy_express_4',
                            power=6000,
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
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
