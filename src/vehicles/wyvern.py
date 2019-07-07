from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='wyvern',
                            base_numeric_id=2950,
                            name='Wyvern',
                            role='heavy_express_1',
                            power=2200,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-1,  # introduce earlier than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
