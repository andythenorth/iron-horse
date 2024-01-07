from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="rockhampton",
        base_numeric_id=10290,
        name="Rockhampton",
        role="universal",
        role_child_branch_num=-3,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1600,
        },
        gen=4,
        intro_year_offset=15,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=30,
        vehicle_length=8,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
