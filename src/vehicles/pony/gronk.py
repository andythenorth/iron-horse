from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="gronk",
        base_numeric_id=21490,
        name="Gronk",
        subrole="gronk",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        intro_year_offset=-9,  # introduce much earlier than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )

    consist_factory.description = (
        """The universal shunter.  Goes everywhere&hellip;slowly."""
    )
    consist_factory.foamer_facts = """BR Class 08/09"""

    print("cabbage 939", consist_factory.kwargs["id"])
    """
    consist_factory.add_clone(base_numeric_id=990, clone_units=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported, but the *buy menu* compositor does not support that as of Jan 2024, so hax
    consist_factory.clones[0].add_unit(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )
    consist_factory.clones[0].units[0].spriterow_num=1

    # JFDI recalculate power to account for 2 units
    consist_factory.clones[0].set_clone_power_from_clone_source()
    # also JFDI, the default single unit should randomly reverse, the 2-unit version should not, so hax
    consist_factory.clones[0].random_reverse = False
    """
    return consist_factory
