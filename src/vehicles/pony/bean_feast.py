from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bean_feast",
        base_numeric_id=21040,
        name="2-6-4 Bean Feast",
        role="universal",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 400,
        },
        tractive_effort_coefficient=0.2,
        gen=1,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=20,
        vehicle_length=4,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """Great power and small size. We tested it in the field."""
    consist.foamer_facts = """generic narrow-gauge steam locomotives"""

    return consist
