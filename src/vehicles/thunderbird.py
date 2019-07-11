from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='thunderbird',
                            base_numeric_id=3090,
                            name='Thunderbird',
                            role='heavy_express_3',
                            power=2600,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=-5,  # let's not have everything turn up in 1990
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=90,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
