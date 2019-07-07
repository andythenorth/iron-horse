from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='medusa',
                            base_numeric_id=3250,
                            name='Medusa',
                            role='heavy_express_3',
                            power=3300,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=5,  # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=90,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
