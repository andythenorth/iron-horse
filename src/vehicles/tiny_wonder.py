from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tiny_wonder",
        base_numeric_id=2030,
        name="0-4-4-0 Tiny Wonder",
        role="universal",
        role_child_branch_num=2,
        base_track_type="NG",
        power=750,
        tractive_effort_coefficient=0.3,
        gen=2,
        random_reverse=True,
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=36,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """ """

    return consist
