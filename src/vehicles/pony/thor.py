from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="thor",
        base_numeric_id=21330,
        name="0-4-4-0 Thor",
        subrole="universal",
        subrole_child_branch_num=2,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 600,
        },
        tractive_effort_coefficient=0.3,
        gen=1,
        intro_year_offset=15,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=30,
        vehicle_length=6,
        effect_offsets=[(-3, 0), (1, 0)],  # double the smoke eh?
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.description = (
        """You could say it's twice the train. A god amongst engines."""
    )
    consist_factory.foamer_facts = """Fairlie locomotives"""

    return consist_factory
