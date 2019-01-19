from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='chimera',
                            base_numeric_id=990,
                            name='Chimera',
                            role='heavy_freight_1',
                            power=4200,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=140,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
