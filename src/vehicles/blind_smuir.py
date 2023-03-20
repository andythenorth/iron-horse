from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="blind_smuir",
        base_numeric_id=4850,
        name="4-6-0 Blind Smuir",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1850,  # slightly less than the Strongbow eh
        },
        speed=75,  # for lolz
        tractive_effort_coefficient=0.22,
        fixed_run_cost_points=150,  # small cost bonus for balance against same gen larger engines
        gen=3,
        intro_year_offset=2,  # let's be a little bit later for this one
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
        sprites_additional_liveries_needed=True, # banger blue?
    )

    consist.add_unit(type=SteamEngineUnit, weight=96, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Mr. Stanier helped me out with these.  You'll probably want hundreds of em."""
    consist.foamer_facts = """LMS Class 5 <i>Black Five</i>, BR Standard 5 Class"""

    return consist
