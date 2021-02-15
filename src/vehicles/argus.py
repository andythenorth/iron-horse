from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="argus",
        base_numeric_id=5400,
        name="Argus",
        role="branch_express",
        role_child_branch_num=-2,
        power=1400, # yes it's quite low power eh
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=3,
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=67, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """Zoooom."""
    )
    consist.foamer_facts = """BR Class 71"""

    return consist
