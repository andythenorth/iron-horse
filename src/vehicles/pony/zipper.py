from train import (
    PassengerEngineRailbusConsist,
    DieselRailcarCombineUnitPax,
    DieselRailcarCombineUnitMail,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="zipper",
        base_numeric_id=260,
        name="Zipper",
        role="pax_railbus",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 480,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist.description = """It's the same donkey, but with a new saddle."""
    consist.foamer_facts = """BR Class 144e <i>Pacer</i>, Vivarail D-Train"""

    return consist
