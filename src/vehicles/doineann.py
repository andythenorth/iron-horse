from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doineann",
        base_numeric_id=10500,
        name="Doineann",
        # Marauder??
        # Prevails??
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2750, # within range of Resilient
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=-4,  # let's be a little earlier for this one
        additional_liveries=["BANGER_BLUE", "SWOOSH_LESS", "SWOOSH"],
        default_livery_extra_docs_examples=[
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=105, vehicle_length=8,
    )

    consist.description = """Let there be some more test made of my metal."""
    consist.foamer_facts = """Northern Ireland Railways Class 111"""

    return consist
