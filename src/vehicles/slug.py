from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="slug",
        base_numeric_id=10040,
        name="Slug",
        role="freight",
        role_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 2000, # there is no point not matching this to the Centaur
        },
        random_reverse=True,
        gen=5,
        # red stripe? Teeside steelmaster?
        additional_liveries=[
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "DB_SCHENKER",
            "LARGE_LOGO",
            "LOADHAUL",
            "SWOOSH_LESS",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_GREY", "COLOUR_YELLOW"),
            ("COLOUR_WHITE", "COLOUR_GREY"),
            ("COLOUR_GREY", "COLOUR_GREY"),
            ("COLOUR_PALE_GREEN", "COLOUR_PALE_GREEN"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
        ],
        caboose_family="railfreight_2",
        decor_spriterow_num=7,
        show_decor_in_purchase_for_variants=[2, 3],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=110, vehicle_length=8, spriterow_num=0
    )

    consist.description = """We made these by uprating the Growler engine.  New paint too, don't spoil it."""
    consist.foamer_facts = """refurbished BR Class 37, with new alternator and uprated engine (per 2,000hp 37292)"""

    return consist
