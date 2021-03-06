from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="shoebox",
        base_numeric_id=280,
        name="Shoebox",
        role="branch_express",
        role_child_branch_num=1,
        power=950,
        power_by_railtype={"RAIL": 950, "ELRL": 1800},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=67, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """This one can go on electric or diesel. Madder than a box of frogs."""
    )
    consist.foamer_facts = """BR Class 71/74, Class 73"""

    return consist
