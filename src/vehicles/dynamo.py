from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="dynamo",
        base_numeric_id=8310,
        name="Dynamo",
        role="express",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 1800,
        },
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        fixed_run_cost_points=180,  # substantial cost bonus for balance against same-era steam engines
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_PINK"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=92, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Nowt to fuss about with this one."""
    consist.foamer_facts = """SR CC1/CC2 locomotives, English Electric Class EP01 exported from UK to Poland"""

    return consist
