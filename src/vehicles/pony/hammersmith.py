from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        roster_id=roster_id,
        id="hammersmith",
        base_numeric_id=1890,
        name="Hammersmith",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        gen=2,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="MetroUnit",
        weight=36,
        capacity=160,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist_factory.description = """Do pigeons roost on rooftops? Do they watch us pass by?"""
    consist_factory.foamer_facts = """London Underground R Stock"""

    return consist_factory
