from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineMetroConsist(
        roster_id=roster_id,
        id="fleet",
        base_numeric_id=210,
        name="Fleet",
        role="pax_metro",
        role_child_branch_num=1,
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
    consist.add_unit(
        type=MetroUnit,
        weight=33,
        capacity=200,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist.description = """Was the train door jammed? Was the time right?"""
    consist.foamer_facts = """London Underground 1996 Stock"""

    return consist
