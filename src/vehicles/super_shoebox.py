from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="super_shoebox",
        base_numeric_id=880,
        name="Super Shoebox",
        role="express",
        role_child_branch_num=-1,
        power=1250,
        power_by_railtype={"RAIL": 1250, "ELRL": 2600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=72, vehicle_length=8, spriterow_num=0
    )

    consist.description = """It's a bigger Shoebox. Well not bigger. But we've got more power in it. Right nice new paint too."""
    consist.foamer_facts = """BR Class 71/74, Class 73"""

    return consist
