from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="mighty",
        base_numeric_id=14150,
        name="Mighty",
        role="universal",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 800, # designed so it can replace 8/8 previous gen engines if so desired
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=8,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=31,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """"""
    consist.foamer_facts = (
        """"""
    )

    return consist
