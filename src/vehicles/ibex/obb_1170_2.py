from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
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

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """OBB 1170.2"""

    return consist_factory
