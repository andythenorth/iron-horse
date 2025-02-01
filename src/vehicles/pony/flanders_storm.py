from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="flanders_storm",
        base_numeric_id=25150,
        name="Flanders Storm",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 6200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RAILFREIGHT_TRIPLE_GREY", "DB_SCHENKER"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=120, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description(
        """This is a right proper engine.  Does work enough for two."""
    )
    consist_factory.add_foamer_facts("""BR Class 92""")

    result.append(consist_factory)

    return result
