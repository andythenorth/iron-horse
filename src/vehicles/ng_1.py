from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ng_1",
        base_numeric_id=14010,
        name="TEST",
        role="universal",
        role_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 600,
        },
        tractive_effort_coefficient=0.3,
        gen=1,
        intro_year_offset=15,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=30,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (1, 0)],  # double the smoke eh?
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
