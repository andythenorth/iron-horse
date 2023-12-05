from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bone",
        base_numeric_id=13860,
        name="Bone",
        role="super_heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        intro_year_offset=-2,  # let's be a little bit earlier for this one
        gen=5,
        caboose_family="railfreight_1",
        #note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "RAILFREIGHT_RED_STRIPE",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "DB_SCHENKER",
            "EWS",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_CREAM"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=125,  # tiny nerf from Grid, because IRL reasons
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """Rome wasn't built in a day. But I wasn't on that particular job."""
    )
    # IRL the quote is Brian Clough
    consist.foamer_facts = """BR Class 58"""

    return consist
