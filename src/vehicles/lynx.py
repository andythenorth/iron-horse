from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lynx",
        base_numeric_id=15770,
        name="Lynx",
        role="branch_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        intro_year_offset=7,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=72, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """Old dog, new tricks. I've built these out of old Chinooks."""
    )
    consist.foamer_facts = """DRS Class 20/3 (re-engineered)"""

    consist.clone(base_numeric_id=820, clone_units=[1])

    # this is a JFDI thing, the Lynx 2-unit version needs a reversed sprite, but the buy menu compositor does not support that as of Jan 2024, so hax
    consist.clones[0].add_unit(
        type=DieselEngineUnit, weight=72, vehicle_length=6, spriterow_num=1
    )

    # JFDI recalculate power to account for 2 units
    consist.clones[0].set_clone_power_from_clone_source()

    # also JFDI, the default single unit should randomly reverse, the 2-unit version should not, so hax
    consist.clones[0].random_reverse=False

    return consist
