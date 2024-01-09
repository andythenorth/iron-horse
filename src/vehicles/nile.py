from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="nile",
        base_numeric_id=14140,
        name="2-6-2+2-6-2 Nile",
        role="universal",
        role_child_branch_num=-4,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 1200,
        },
        tractive_effort_coefficient=0.3,
        gen=3,
        intro_year_offset=-15, # introduce early, even though wagons are not available at 55 mph, it's a long-lifed joker really
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=30,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (1, 0)],  # double the smoke eh?
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = (
        """"""
    )
    # https://en.wikipedia.org/wiki/Victorian_Railways_G_class#/media/File:Puffing_Billy_Garratt_G42_07.jpg
    # https://en.wikipedia.org/wiki/South_African_Class_NG_G16_2-6-2%2B2-6-2
    consist.foamer_facts = """"""

    return consist
