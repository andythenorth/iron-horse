from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="falcon",
        base_numeric_id=17860,
        name="Falcon",
        role="super_heavy_express",
        role_child_branch_num=-2,
        replacement_consist_id="rapid",  # this Joker ends with Rapid (switching child branch) - goal is to keep Falcon around for a while, because I like it
        power_by_power_source={
            "DIESEL": 2800,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=5,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_YELLOW"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-1, 0), (1, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.description = """The big bird. Twin engines. Takes on anything."""
    consist.foamer_facts = """Brush / BR Class 53 <i>Falcon</i> prototype"""

    return consist
