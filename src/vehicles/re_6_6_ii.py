from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="re_6_6_ii",
        base_numeric_id=50,
        name="SBB Re 6/6 ii",
        role="ultra_heavy_freight",
        role_child_branch_num=2,
        power=10700,
        gen=5,
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
    consist.foamer_facts = """SBB Re 6/6"""

    return consist
