from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="argus",
        base_numeric_id=21780,
        name="Argus",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 1300,
        },
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=67, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description("""Zoooom.""")
    consist_factory.add_foamer_facts("""SR CC1/CC2, BR Class 71""")

    return consist_factory
