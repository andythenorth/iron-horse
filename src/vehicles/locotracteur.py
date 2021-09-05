from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="locotracteur",
        base_numeric_id=2960,
        name="Locotracteur",
        role="universal",
        role_child_branch_num=2,
        power=800,
        random_reverse=True,
        base_track_type="NG",
        gen=3,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=30,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """ """
    consist.foamer_facts = """ """

    return consist
