from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='sizzler',
                            base_numeric_id=2180,
                            name='Sizzler',
                            role='heavy_express_2',
                            power=6800,
                            random_reverse=True,
                            gen=6,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=5,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=82,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
