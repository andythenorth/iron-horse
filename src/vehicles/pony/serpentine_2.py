from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineMetroConsist(
        roster_id=roster_id,
        id="serpentine_2",
        base_numeric_id=1930,
        name="Serpentine 2",
        role="pax_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=False,
    )

    # should be 4 units not 2, would look nicer short, but eh, painting
    consist.add_unit(
        type=MetroUnit,
        weight=36,
        capacity=120,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """Does the money feel good? Do you like your life well."""
    consist.foamer_facts = """London Underground 'Gate' Stock, Standard Stock"""

    return consist
