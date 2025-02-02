from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        id="westbourne",
        base_numeric_id=360,
        name="Westbourne",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 850,
        },
        gen=2,
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=33,
        capacity=160,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.define_description("""Does the public want what the public gets?""")
    consist_factory.define_foamer_facts("""London Underground 1938/1949 Stock""")

    result.append(consist_factory)

    return result
