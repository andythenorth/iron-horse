from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="pikel",
        base_numeric_id=21100,
        name="Pikel",
        role="universal",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 600,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=-2,  # introduce a bit earlier
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
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

    consist.clone(base_numeric_id=920, clone_units=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported, but the *buy menu* compositor does not support that as of Jan 2024, so hax
    consist.clones[0].add_unit(
        type=DieselEngineUnit, weight=22, vehicle_length=4, spriterow_num=1
    )

    # JFDI recalculate power to account for 2 units
    consist.clones[0].set_clone_power_from_clone_source()

    return consist
