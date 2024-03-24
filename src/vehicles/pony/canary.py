from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineMetroConsist(
        roster_id=roster_id,
        id="canary",
        base_numeric_id=960,
        name="Canary",
        role="pax_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1100,
        },
        gen=3,
        sprites_complete=True,
    )

    # should be 4 short units, not 2 long but eh
    consist.add_unit(
        type=MetroUnit,
        weight=36,
        capacity=200,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_3",
        repeat=2,
    )

    consist.description = """Do Mondays go on slow-time?"""
    consist.foamer_facts = """London Underground S Stock"""

    return consist
