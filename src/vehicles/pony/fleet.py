from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineMetroConsist",
        id="fleet",
        base_numeric_id=210,
        name="Fleet",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 1050,
        },
        gen=3,
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_RED"),
            ("COLOUR_RED", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    # should be 4 short units, not 2 long but eh
    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=33,
        capacity=200,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.define_description(
        """Was the train door jammed? Was the time right?"""
    )
    consist_factory.define_foamer_facts("""London Underground 1996 Stock""")

    result.append(consist_factory)

    return result
