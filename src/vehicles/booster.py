from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="booster",
        base_numeric_id=5480,
        name="Booster",
        role="branch_express",
        role_child_branch_num=-2,
        power=600,
        power_by_railtype={"RAIL": 600, "ELRL": 1600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_date_offset=9,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = """I've rebuilt some of the Argus fleet to be more handy. Now we're sucking diesel."""
    consist.foamer_facts = """BR Class 71/74, Class 73"""

    return consist
