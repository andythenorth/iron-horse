from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='carrack',
                            base_numeric_id=1040,
                            name='4-4-0 Carrack',
                            role='express_1',
                            joker=True,  # this engine doesn't fit the intro date pattern, to mix things up a bit
                            power=1050,
                            tractive_effort_coefficient=0.18,
                            gen=2,
                            intro_date_offset=-3,  # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=60,
                     vehicle_length=5,
                     visual_effect_offset=-4,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
