from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='blind_smuir',
                            base_numeric_id=4850,
                            name='4-6-0 Blind Smuir',
                            role='heavy_freight',
                            role_child_branch_num=-1,
                            replacement_consist_id='duff', # this Joker ends with Duff
                            power=1850, # slightly less than the Strongbow eh
                            speed=75, # for lolz
                            tractive_effort_coefficient=0.22,
                            fixed_run_cost_points=150, # small cost bonus for balance against same gen larger engines
                            gen=3,
                            intro_date_offset=2,  # let's be a little bit later for this one
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=96,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=40,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
