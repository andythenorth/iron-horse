from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="mainstay",
        base_numeric_id=6360,
        name="2-8-0 Mainstay",
        role="heavy_freight",
        role_child_branch_num=1,
        replacement_consist_id="intrepid",  # this Joker ends with Intrepid
        power=1850,  # slightly less than the Strongbow eh
        speed=60,
        tractive_effort_coefficient=0.23,
        gen=3,
        intro_date_offset=2,  # let's be a little bit later for this one
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=96, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=50, vehicle_length=4, spriterow_num=1
    )

    consist.description = """CABBASGE"""
    consist.foamer_facts = """CABBAGE"""

    return consist
