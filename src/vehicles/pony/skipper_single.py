from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="skipper_single",
        base_numeric_id=25260,
        name="Skipper",
        role="pax_railbus",
        role_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 225,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="skipper",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=24,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = """Patience is the virtue of the donkeys."""
    consist.foamer_facts = """BR Class 141/142/143/144 <i>Pacers</i>"""

    return consist
