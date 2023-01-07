from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="centaur",
        base_numeric_id=14810,
        name="Centaur",
        role="freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1950,  # progression calculated to maintain hp/speed ratio from previous gen
        },
        random_reverse=True,
        gen=5,
        # red stripe? Teeside steelmaster?
        additional_liveries=["RAILFREIGHT_TRIPLE_GREY"],
        default_livery_extra_docs_examples=[
            ("COLOUR_GREY", "COLOUR_YELLOW"),
            ("COLOUR_WHITE", "COLOUR_GREY"),
            ("COLOUR_GREY", "COLOUR_GREY"),
            ("COLOUR_PALE_GREEN", "COLOUR_PALE_GREEN"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
        ],
        caboose_family="railfreight_2",
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=110, vehicle_length=8, spriterow_num=0
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
