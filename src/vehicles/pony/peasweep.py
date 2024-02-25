from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="peasweep",
        base_numeric_id=1750,
        name="Peasweep",
        role="ultra_heavy_freight",
        role_child_branch_num=2,
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

    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """What we like about these is no fuss, no mess. Get in and off they go."""
    )
    consist.foamer_facts = """LNER EM1 (BR Class 76)"""

    consist.clone(base_numeric_id=34940, clone_units=[1, 0])

    return consist
