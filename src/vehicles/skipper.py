from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="skipper",
        base_numeric_id=5660,
        name="Skipper",
        role="pax_railbus",
        role_child_branch_num=1,
        power=225,
        gen=5,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=24,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_2",
    )

    consist.description = """Patience is the virtue of the donkeys."""
    consist.foamer_facts = """BR Class 142 <i>Pacer</i>"""

    return consist
