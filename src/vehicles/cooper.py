from train import EngineConsist, DieselEngineUnit


def main():    # GE Shovelnose - meter gauge ish
    consist = EngineConsist(roster=roster,
                            id='cooper',
                            base_numeric_id=1440,
                            name='Cooper',
                            power=1000,
                            base_track_type='NG',
                            intro_date=1949)

    consist.add_unit(type=DieselEngineUnit,
                     weight=85,
                     vehicle_length=7,
                     spriterow_num=0)

    return consist
