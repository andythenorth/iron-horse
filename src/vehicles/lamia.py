from train import EngineConsist, SteamEngineUnit

def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='lamia',
                            base_numeric_id=4880,
                            name='0-6-0 Lamia', # the name is the Basque mythical creature, not the Greek https://en.wikipedia.org/wiki/Lamia_(Basque_mythology)
                            role='gronk!',
                            role_child_branch_num=-2,
                            replacement_consist_id='gronk', # this Joker ends with Gronk
                            power=350,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            fixed_run_cost_points=109, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=2,
                            vehicle_life=60, # extended vehicle life for all gronks eh
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=0)

    consist.foamer_facts = """GWR Pannier Tanks, original TTD Kirby Paul Tank"""

    return consist
