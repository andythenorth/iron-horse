from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        role="super_heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        # alternative_liveries=["RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=82, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """It's a rat pack. What more do you want?"""
    consist.foamer_facts = """BR Class 24, BR Class 25"""

    return consist
