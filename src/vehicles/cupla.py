from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cupla",
        base_numeric_id=6750,
        name="Cúpla",
        role="heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2250,
        },
        speed=87,  # continues past gen 5, so go faster
        random_reverse=True,
        gen=4,
        intro_year_offset=8,  # let's be quite a bit later for this one
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=60, vehicle_length=5, repeat=2
    )

    consist.description = """"""
    consist.foamer_facts = """Irish Railways 181 Class"""

    return consist
