from train import EngineConsist, DieselEngineUnit

# not used, maybe restore if there's a 'pointless trains' parameter :P

def main(roster):
    consist = EngineConsist(roster=roster,
                            id='grub',
                            base_numeric_id=4010,
                            name='Grub',
                            role='gronk!',
                            power=250,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            joker=True,
                            gen=1,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
