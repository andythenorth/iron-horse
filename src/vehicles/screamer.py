from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="screamer",
        base_numeric_id=9490,
        name="Screamer",
        role="ultra_heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 5000,
        },
        random_reverse=False,
        gen=5,
        speed=125,
        pantograph_type="z-shaped-double",
        intro_year_offset=2,  # introduce later than gen epoch by design
        # railfreight grey, intercity, GNER?
        additional_liveries=["FREIGHTLINER_GBRF", "RES", "SWOOSH", "FREIGHTLINER_2"],
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_BLUE"),
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_DARK_BLUE"),
            ("COLOUR_WHITE", "COLOUR_RED"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_needed=True, # banger blue, railfreight grey, GNER?
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=85, vehicle_length=8, spriterow_num=0
    )

    consist.description = """We're knocking these out cheap enough. Look after them, they might last longer."""
    consist.foamer_facts = """BR Class 90"""

    return consist
