from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="falcon",
        base_numeric_id=6430,
        name="Falcon",
        role="heavy_express",
        role_child_branch_num=-4,
        replacement_consist_id="onslaught",  # this Joker ends with Onslaught
        power=2800,
        random_reverse=True,
        gen=4,
        intro_date_offset=5, # introduce later than gen epoch by design
        fixed_run_cost_points=230,  # give a serious malus to this one (balancing eh?)
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_YELLOW"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-1, 0), (1, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.description = """."""
    consist.foamer_facts = (
        """ """
    )

    return consist
