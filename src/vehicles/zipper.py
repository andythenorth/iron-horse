from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="zipper",
        base_numeric_id=14710,
        name="Zipper",
        role="pax_railbus",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power=280,
        gen=6,
        # introduce early by design
        intro_date_offset=-4,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=25,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = """It's the same donkey, but with a new saddle."""
    consist.foamer_facts = """BR Class 144e <i>Pacer</i>, Vivarail D-Train"""

    return consist
