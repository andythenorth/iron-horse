from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="happy_train",
        base_numeric_id=9140,
        name="Happy Train",
        role="pax_railcar",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 500,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist.description = (
        """Fast quiet trains for a new era. No more life-expired Tin Rockets."""
    )
    consist.foamer_facts = """Siemens <i>Desiro</i>"""

    return consist
