from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="growler",
        base_numeric_id=11280,
        name="Growler",
        role="freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        random_reverse=True,
        gen=4,
        caboose_family="railfreight_1",
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Sounds like a tractor, pulls like a train."""
    consist.foamer_facts = """BR Class 37, original TTD UU '37'"""

    return consist
