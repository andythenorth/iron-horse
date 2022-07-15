from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="krokodil",
        base_numeric_id=100,
        name="SBB Ce 6/8 Krokodil",
        role="super_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 2200,
        },
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Ce 6/8 Krokodil"""

    return consist
