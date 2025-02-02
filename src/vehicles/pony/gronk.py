from train import ConsistFactory


def main(**kwargs):
    result = []

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

    consist_factory.define_unit(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )

    consist_factory.define_description(
        """The universal shunter.  Goes everywhere&hellip;slowly."""
    )
    consist_factory.define_foamer_facts("""BR Class 08/09""")

    result.append(consist_factory)

    consist_factory = consist_factory.begin_clone(base_numeric_id=990, unit_repeats=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported
    # but the *buy menu* compositor does not support that as of Jan 2024, so hax
    consist_factory.unit_factories[0].kwargs["spriterow_num"] = 1
    consist_factory.define_unit(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )

    # JFDI, the single unit should randomly reverse, the 2-unit version should not, so hax
    consist_factory.kwargs["random_reverse"] = False

    consist_factory.complete_clone()

    result.append(consist_factory)

    return result
