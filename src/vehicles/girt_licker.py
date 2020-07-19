from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='girt_licker',
                            base_numeric_id=70,
                            name='0-10-0 Girt Licker',
                            role='heavy_freight',
                            role_child_branch_num=-2,
                            replacement_consist_id='blind_smuir', # this Joker ends with Blind Smuir
                            power=1950,
                            tractive_effort_coefficient=0.33,
                            gen=2,
                            intro_date_offset=6, # introduce a bit later
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=100,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=45,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
