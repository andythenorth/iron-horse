from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="pikel",
        base_numeric_id=9470,
        name="Pikel",
        role="universal",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 500,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=22,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """This diesel engine modernises our narrow gauge lines."""
    consist.foamer_facts = """FAUR L45H B-B, generic narrow-gauge diesel locomotives"""

    return consist
