from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineMetroConsist(
        roster_id=roster_id,
        id="hammersmith",
        base_numeric_id=1890,
        name="Hammersmith",
        role="pax_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        gen=2,
        sprites_complete=False,
    )

    consist.add_unit(
        type=MetroUnit,
        weight=36,
        capacity=160,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """."""
    consist.foamer_facts = """ """

    return consist