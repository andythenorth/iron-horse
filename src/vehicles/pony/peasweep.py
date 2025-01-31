from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="peasweep",
        base_numeric_id=1750,
        name="Peasweep",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 3700,
        },
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        # additional_liveries=["FREIGHT_BLACK", "BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # nightshade / nighthawk?
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist_factory.description = (
        """What we like about these is no fuss, no mess. Get in and off they go."""
    )
    consist_factory.foamer_facts = """LNER EM1 (BR Class 76)"""

    consist_factory.add_clone(base_numeric_id=34940, clone_units=[1, 0])

    return consist_factory
