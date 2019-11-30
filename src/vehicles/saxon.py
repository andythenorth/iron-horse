from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='saxon',
                            base_numeric_id=1330,
                            name='0-8-0 Saxon',
                            role='branch_freight',
                            power=1000,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            gen=3,
                            intro_date_offset=-8, # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=65,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
