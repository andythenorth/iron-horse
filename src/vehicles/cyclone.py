from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cyclone",
        base_numeric_id=8440,
        name="Cyclone",
        role="express",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 2200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        additional_liveries=["SWOOSH", "SWOOSH_LESS", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=92, vehicle_length=8, spriterow_num=0
    )

    consist.description = """."""
    consist.foamer_facts = """ """

    return consist
