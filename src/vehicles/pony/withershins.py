from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="withershins",
        base_numeric_id=6390,
        name="Withershins",
        role="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        decor_spriterow_num=3,
        sprites_complete=True,
    )

    consist.add_unit(type=DieselEngineUnit, weight=82, vehicle_length=6, repeat=2)

    consist.description = """It's a rat pack. What more do you want?"""
    consist.foamer_facts = """BR Class 24, BR Class 25"""

    consist.clone(base_numeric_id=34910, clone_units=[1, 0])

    return consist
