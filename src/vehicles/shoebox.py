from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="shoebox",
        base_numeric_id=280,
        name="Shoebox",
        role="express",
        role_child_branch_num=-1,
        power=950, # yes it's quite low power initially eh
        power_by_railtype={"RAIL": 950, "ELRL": 2300},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_date_offset=5,  # introduce later than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=67, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """This one can go on electric or diesel. Madder than a box of frogs."""
    )
    consist.foamer_facts = """BR Class 70, Class 73"""

    return consist
