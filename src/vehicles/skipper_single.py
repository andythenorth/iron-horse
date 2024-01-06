from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="skipper_single",
        base_numeric_id=14700,
        name="Skipper",
        role="pax_railbus",
        role_child_branch_num=-2,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 225,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="skipper", # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        pax_car_capacity_type="high_capacity", # specific to standard gauge pony railbuses
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
