from train import (
    PassengerEngineRailbusConsist,
    DieselRailcarCombineUnitPax,
    DieselRailcarCombineUnitMail,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="skipper",
        base_numeric_id=240,
        name="Skipper",
        role="pax_railbus",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_2",
    )

    consist.description = """Patience is the virtue of the donkeys."""
    consist.foamer_facts = """BR Class 141/142/143/144 <i>Pacers</i>"""

    return consist
