from train import EngineConsist, DieselEngineUnit

# not used, maybe restore if there's a 'pointless trains' parameter :P

def main(roster):
    consist = EngineConsist(roster=roster,
                            id='gronk',
                            base_numeric_id=3970,
                            name='Gronk',
                            role='lolz',
                            power=400,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            joker=True,
                            gen=4,
                            intro_date_offset=-9, # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=55,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
