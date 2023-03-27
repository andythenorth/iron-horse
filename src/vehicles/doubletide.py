from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doubletide",
        base_numeric_id=220,
        name="Doubletide",
        role="heavy_freight",
        role_child_branch_num=2,
        # no replacement by design - continues to game end as 10/8, especially for industrial use etc
        power_by_power_source={
            "DIESEL": 2750, # within range of Resilient
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=9,  # let's be quite a bit later for this one, Yillen is long-lived
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=68, vehicle_length=5, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=68, vehicle_length=5, spriterow_num=1
    )

    #  guess the quote?
    consist.description = """And ruined love when it is built anew grows fairer than at first, more strong, far greater."""
    consist.foamer_facts = """Re-engineered BR Class 15, BR Class 16"""

    return consist
