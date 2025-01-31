from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="cheese_bug",
        base_numeric_id=21060,
        name="2-6-2 Cheese Bug",
        subrole="universal",
        subrole_child_branch_num=-1,
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

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=18,
        vehicle_length=4,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.description = """I present you this trusty little engine."""
    consist_factory.foamer_facts = """generic narrow-gauge steam locomotives"""

    return consist_factory
