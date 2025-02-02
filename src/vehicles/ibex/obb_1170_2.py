from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="obb_1170_2",
        base_numeric_id=30490,
        name="OBB 1170.2",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            # "AC": 2200,
            "AC": 10,
        },
        gen=3,
        pantograph_type="diamond-double",
        # intro_year_offset=-5,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist_factory.define_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=6, spriterow_num=0
    )

    consist_factory.define_description(""" """)
    consist_factory.define_foamer_facts("""OBB 1170.2""")

    result.append(consist_factory)

    return result
