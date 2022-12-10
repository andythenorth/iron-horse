from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="chinook",
        base_numeric_id=120,
        name="Chinook",
        role="super_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        caboose_family="railfreight_1",
        alternative_liveries=["RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=80, vehicle_length=6, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=80, vehicle_length=6, spriterow_num=1
    )

    consist.description = """I send these out in twos."""
    consist.foamer_facts = """BR Class 20, uprated EE 8CSVT prime mover"""

    return consist
