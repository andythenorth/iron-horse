from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="pinhorse",
        base_numeric_id=12290,
        name="Pinhorse",
        role="branch_express",
        role_child_branch_num=-2,
        power=900,
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=2,
        intro_date_offset=3,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=60, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Mr. Bulleid and Mr. Raworth drew these up for me. For small jobs, you won't go far wrong with em."""
    consist.foamer_facts = """Metropolitan Railway electric locos, SR CC1/CC2"""

    return consist
