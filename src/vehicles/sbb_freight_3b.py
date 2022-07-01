from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sbb_freight_3b",
        base_numeric_id=110,
        name="SBB Ae 8/14",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power=3700,
        gen=3,
        pantograph_type="diamond-double",
        #intro_date_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """SBB Ae 8/14"""

    return consist
