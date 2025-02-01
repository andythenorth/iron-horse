from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        id="canary",
        base_numeric_id=960,
        name="Canary",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1100,
        },
        gen=3,
        sprites_complete=True,
    )

    # should be 4 short units, not 2 long but eh
    consist_factory.add_unit(
        class_name="MetroUnit",
        weight=36,
        capacity=200,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_3",
        repeat=2,
    )

    consist_factory.add_description("""Do Mondays go on slow-time?""")
    consist_factory.add_foamer_facts("""London Underground S Stock""")

    result.append(consist_factory)

    return result
