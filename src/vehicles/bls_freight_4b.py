from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sbb_freight_4b",
        base_numeric_id=130,
        name="BLS Ae 8/8",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power=8700,
        gen=4,
        pantograph_type="diamond-double",
        #intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """BLS Ae 8/8"""

    return consist
