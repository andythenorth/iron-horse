from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hurly_burly",
        base_numeric_id=9430,
        name="Hurly Burly",
        role="super_heavy_express",
        role_child_branch_num=3,
        power_by_power_source={
            "AC": 1800,
        },
        tractive_effort_coefficient=0.25,
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        fixed_run_cost_points=180,  # substantial cost bonus for balance against same-era steam engines
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_PINK"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=90, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """By eck, it's a big electric.  Better put some pennies in the meter."""
    )
    consist.foamer_facts = """NER Class EE1"""

    return consist
