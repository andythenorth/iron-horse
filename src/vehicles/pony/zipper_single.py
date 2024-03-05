from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="zipper_single",
        base_numeric_id=25270,
        name="Zipper",
        role="pax_railbus",
        role_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 280,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="zipper",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
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
