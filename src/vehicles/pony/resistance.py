from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="resistance",
        base_numeric_id=20990,
        name="Resistance",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "AC": 5200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=-4,  # earlier than the IRL introduction of this never-built train...
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "RAILFREIGHT_RED_STRIPE",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "DB_SCHENKER",
            "EWS",
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=120, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description("""A hard-charging bag of bones.""")
    consist_factory.add_foamer_facts(
        """Proposed BR Class 88, derived from Class 58 design"""
    )

    return consist_factory
