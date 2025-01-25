from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doubletide",
        base_numeric_id=220,
        name="Doubletide",
        role="heavy_freight",
        subrole_child_branch_num=-1,
        # no replacement by design - continues to game end as 10/8, especially for industrial use etc
        power_by_power_source={
            "DIESEL": 2750,  # within range of Resilient
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=9,  # let's be quite a bit later for this one, Yillen is long-lived
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    # 2 separate units so that buy menu has reversed cabs
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
