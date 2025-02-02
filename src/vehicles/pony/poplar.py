from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        id="poplar",
        base_numeric_id=1930,
        name="Poplar",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=36,
        capacity=120,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist_factory.define_description(
        """Do dreams fade in the dawn? Lost in the city's waking."""
    )
    consist_factory.define_foamer_facts(
        """Metropolitan Railway electric multiple units"""
    )

    result.append(consist_factory)

    return result
