from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='scorcher',
                            base_numeric_id=2950,
                            name='Scorcher',
                            role='heavy_express_1',
                            power=6000,
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                            dual_headed=True,
                            intro_date_offset=-12,  # let's be a little bit earlier for this one
                            gen=6,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=70,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
