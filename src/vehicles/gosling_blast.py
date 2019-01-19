from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='gosling_blast',
                            base_numeric_id=2960,
                            name='Gosling Blast',
                            role='heavy_freight_2',
                            power=8500,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                            gen=6,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=7,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=132,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
