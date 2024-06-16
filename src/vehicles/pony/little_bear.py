from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="little_bear",
        base_numeric_id=21220,
        name="Little Bear",
        role="branch_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1450,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        intro_year_offset=-6,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=68, vehicle_length=6, spriterow_num=0
    )

    consist.description = """I want no epitaphs of profound history and all that type of thing. I contributed - I would hope they would say that, and I would hope somebody liked me."""
    # IRL the quote is Brian Clough
    consist.foamer_facts = """BR Class 14, Clayton DHP1 prototype"""

    return consist
