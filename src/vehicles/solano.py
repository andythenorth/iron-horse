from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="solano",
        base_numeric_id=14220,
        name="Solano",
        role="universal",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW", "BANGER_BLUE", "INDUSTRIAL_YELLOW"], # different cab heights, for lolz :P
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=40,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """"""
    # https://en.wikipedia.org/wiki/New_Zealand_DE_class_locomotive, also NZ Di class
    # nah it's CP_Class_9020 now, and rename from Silverfern
    # see also https://trainspo.com/photo/98083/
    consist.foamer_facts = (
        """"""
    )

    return consist
