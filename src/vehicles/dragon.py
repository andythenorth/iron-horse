from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='dragon',
                            base_numeric_id=420,
                            name='Dragon',
                            role='heavy_express_3',
                            power=2750,  # one-off huge jump in HP compared to steam engine of same era
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=5,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=85,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
