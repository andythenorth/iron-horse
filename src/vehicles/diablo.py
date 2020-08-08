from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='diablo',
                            base_numeric_id=4910,
                            name='2-6-0 Diablo',
                            role='freight',
                            role_child_branch_num=-1,
                            replacement_consist_id='growler', # this Joker ends with Growler
                            power=1500, # same as Haar
                            speed=75, # for lolz
                            tractive_effort_coefficient=0.22,
                            fixed_run_cost_points=150, # small cost bonus for balance against same gen Haar
                            gen=3,
                            intro_date_offset=4, # introduce a bit later
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=70,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=36,
                     vehicle_length=3,
                     spriterow_num=1)

    consist.foamer_facts = """LMS <i>Hughes Crab</i>, BR Standard Class 4 2-6-0."""

    return consist
