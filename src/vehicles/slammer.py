from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="slammer",
        base_numeric_id=9510,
        name="Slammer",
        role="pax_railcar",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist.description = (
        """Fast quiet trains for a new era. No more lurching Deasils."""
    )
    consist.foamer_facts = """BR Class 108/117/121 and similar units"""

    return consist
