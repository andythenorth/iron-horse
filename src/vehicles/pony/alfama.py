from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="alfama",
        base_numeric_id=21670,
        name="0-4-4-0 Alfama",
        subrole="universal",
        subrole_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 600,
        },
        tractive_effort_coefficient=0.3,
        gen=2,
        # introduce early by design
        intro_year_offset=-10,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=32,
        vehicle_length=6,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.description = (
        """Dances with mid-power grace. Articulated finesse in every turn."""
    )
    consist_factory.foamer_facts = (
        """Mallet locomotives used by Portugese narrow gauge railways"""
    )

    return consist_factory
