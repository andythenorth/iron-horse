from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="arrow",
        base_numeric_id=6420,
        name="2-6-2 Arrow",
        role="heavy_express",
        role_child_branch_num=-2,  # -ve because Joker
        power=1850,
        tractive_effort_coefficient=0.18,
        gen=3,
        intro_date_offset=4,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_DARK_GREEN"),
            ("COLOUR_GREY", "COLOUR_WHITE"),
            ("COLOUR_WHITE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=94,
        vehicle_length=7,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=36, vehicle_length=3, spriterow_num=1
    )

    consist.description = (
        """."""
    )
    consist.foamer_facts = """LNER V2"""

    return consist
