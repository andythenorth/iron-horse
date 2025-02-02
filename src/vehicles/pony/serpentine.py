from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        id="serpentine",
        base_numeric_id=460,
        name="Serpentine",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 550,
        },
        gen=1,
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=33,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.define_description(
        """Does the money feel good? Do you like your life well."""
    )
    consist_factory.define_foamer_facts(
        """London Underground 'Gate' Stock, Standard Stock"""
    )

    result.append(consist_factory)

    return result
