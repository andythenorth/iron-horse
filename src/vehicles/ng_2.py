from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ng_2",
        base_numeric_id=830,
        name="TEST",
        role="universal",
        role_child_branch_num=-3,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 750,
        },
        tractive_effort_coefficient=0.3,
        gen=2,
        intro_year_offset=15,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        #additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=65, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=29, vehicle_length=3, spriterow_num=1
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
