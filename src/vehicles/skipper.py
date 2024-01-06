from train import PassengerEngineRailbusConsist, DieselRailcarCombineUnitPax, DieselRailcarCombineUnitMail


def main(roster_id):
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
        pax_car_capacity_type="railbus_combine", # specific to combined mail + pax consist
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_24px_2", # !!!!!!!!! CABBAGE
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_24px_2", # !!!!!!!!! CABBAGE
    )

    consist.description = """Patience is the virtue of the donkeys."""
    consist.foamer_facts = """BR Class 142 <i>Pacer</i>"""

    return consist
