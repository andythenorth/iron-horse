from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='badenoch',
                            base_numeric_id=4840,
                            name='2-8-2 Badenoch',
                            role='heavy_express',
                            role_child_branch_num=-2, # -ve because Joker
                            power=2250,
                            tractive_effort_coefficient=0.25,
                            gen=3,
                            intro_date_offset=6, # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     effect_offsets=[(-3, 0), (-2, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
