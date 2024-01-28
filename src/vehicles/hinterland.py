from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hinterland",
        base_numeric_id=14550,
        name="Hinterland",
        role="universal",
        role_child_branch_num=-4,
        power_by_power_source={
            "DIESEL": 1200,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=1,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=65,
        vehicle_length=8,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """"""
    # https://en.wikipedia.org/wiki/Queensland_Railways_1270_class
    # https://en.wikipedia.org/wiki/Queensland_Railways_1150_class
    consist.foamer_facts = (
        """"""
    )

    return consist
