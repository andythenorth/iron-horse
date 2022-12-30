from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tornado",
        base_numeric_id=14530,
        name="Tornado",
        role="branch_express",
        role_child_branch_num=-2,
        power_by_power_source={"DIESEL": 750, "AC": 1900},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=12,  # introduce later than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=70, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """The Boosters needed a boost. Rebuilt, repainted, off to the races we go."""
    )
    consist.foamer_facts = """BR Class 74, Class 73"""

    return consist
