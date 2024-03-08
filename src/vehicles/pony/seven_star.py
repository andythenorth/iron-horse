from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="seven_star",
        base_numeric_id=30870,
        name="Higuma",
        role="express",
        role_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1500,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "SWOOSH"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=60,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # https://en.wikipedia.org/wiki/New_Zealand_DL_class_locomotive
    # https://en.wikipedia.org/wiki/New_Zealand_DM_class_locomotive
    consist.description = (
        """"""
    )
    consist.foamer_facts = """(Stadler / Mitsubishi bo-bo-bo)"""

    return consist
