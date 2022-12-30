from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="moor_gallop",
        base_numeric_id=9210,
        name="Moor Gallop",
        role="super_heavy_express",
        role_child_branch_num=3,
        power_by_power_source={
            "AC": 2400,
        },
        tractive_effort_coefficient=0.25,
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        additional_liveries=["BANGER_BLUE", "DUTCH_UNLIMITED"],
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """It's not so hurly-burly, but it's a nice new electric engine for you."""
    )
    consist.foamer_facts = """LNER EM2 (BR Class 77)"""

    return consist
