from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='dragon',
                            base_numeric_id=420,
                            name='Dragon',
                            role='heavy_express_1',
                            power=2600,
                            random_reverse=True,
                            gen=4,
                            replacement_consist_id='thunderbird', # this line ends with Dragon and is merged to heavy_express_3
                            intro_date_offset=2,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=85,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
