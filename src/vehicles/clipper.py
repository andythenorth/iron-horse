from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="clipper",
        base_numeric_id=14690,
        name="Clipper",
        role="pax_railbus",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power=180,
        gen=4,
        # introduce early by design
        intro_date_offset=-4,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=22,
        chassis="railbus_swb_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = (
        """The horses of hope gallop, but the donkeys of experience go slowly."""
    )
    consist.foamer_facts = """BR 1st generation AC Cars/Wickham/Waggon-und Maschinenbau and similar railbuses"""

    return consist
