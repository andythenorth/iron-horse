from train import EngineConsist, SteamEngineUnit


def main():
    consist = EngineConsist(id='saxon',
                            base_numeric_id=1330,
                            name='0-8-0 Saxon',
                            role='branch_freight',
                            power=1000,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                            gen=3,
                            intro_date_offset=-8)  # introduce earlier than gen epoch by design

    consist.add_unit(type=SteamEngineUnit,
                     weight=65,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
