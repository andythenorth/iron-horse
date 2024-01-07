from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ng_4",
        base_numeric_id=14150,
        name="TEST",
        role="universal",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=4,
        intro_year_offset=11,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=30,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """"""
    consist.foamer_facts = (
        """"""
    )

    return consist
