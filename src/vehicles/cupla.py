from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cupla",
        base_numeric_id=6750,
        name="Cúpla",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3300,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=-12,  # let's be much earlier for this one
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=60, vehicle_length=6, repeat=2
    )

    consist.description = """Good horses make short miles."""
    consist.foamer_facts = """Irish Railways 181 Class"""

    return consist
