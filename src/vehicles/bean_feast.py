from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bean_feast",
        base_numeric_id=9280,
        name="2-6-4 Bean Feast",
        role="universal",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 400,
        },
        tractive_effort_coefficient=0.2,
        gen=2,
        random_reverse=True,
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=22,
        vehicle_length=4,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """Great power and small size. We tested it in the field."""
    consist.foamer_facts = """generic narrow-gauge steam locomotives"""

    return consist
