from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="lynx",
        base_numeric_id=26810,
        name="Lynx",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        intro_year_offset=7,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description(
        """Old dog, new tricks. I've built these out of old Chinooks."""
    )
    consist_factory.add_foamer_facts("""DRS Class 20/3 (re-engineered)""")

    print("cabbage 939", consist_factory.kwargs["id"])
    """
    consist_factory.add_clone(base_numeric_id=820, clone_units=[1])

    # this is a JFDI thing, the Lynx 2-unit version needs a reversed sprite, but the buy menu compositor does not support that as of Jan 2024, so hax
    consist_factory.clones[0].add_unit(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, spriterow_num=1
    )

    # JFDI recalculate power to account for 2 units
    consist_factory.clones[0].set_clone_power_from_clone_source()

    # also JFDI, the default single unit should randomly reverse, the 2-unit version should not, so hax
    consist_factory.clones[0].random_reverse = False
    """
    result.append(consist_factory)

    consist_factory = consist_factory.clone(base_numeric_id=820)

    result.append(consist_factory)

    return result
