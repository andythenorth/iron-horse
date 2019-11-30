from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='electrico',
                            base_numeric_id=180,
                            name='Electrico 2-B+B-2',
                            power=2400,
                            intro_date=1920)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=140,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
