from train import (
    PassengerEngineRailbusConsist,
    DieselRailcarCombineUnitPax,
    DieselRailcarCombineUnitMail,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="clipper",
        base_numeric_id=250,
        name="Clipper",
        role="pax_railbus",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    consist.description = (
        """The horses of hope gallop, but the donkeys of experience go slowly."""
    )
    consist.foamer_facts = """BR 1st generation AC Cars/Wickham/Waggon-und Maschinenbau and similar railbuses"""

    return consist
