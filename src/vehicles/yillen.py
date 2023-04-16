from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="yillen",
        base_numeric_id=6370,
        name="Yillen",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a little earlier for this one
        additional_liveries=["INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=67, vehicle_length=5, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=67, vehicle_length=5, spriterow_num=1
    )

    consist.description = """The universe is asymmetric. And so are these."""
    consist.foamer_facts = """BR Class 15, BR Class 16"""

    return consist
