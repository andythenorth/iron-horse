from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ae_3_5",
        base_numeric_id=9040,
        name="Ae 3/5",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            # "AC": 1100,
            "AC": 10,
        },
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=6, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Ae 3/5"""

    return consist
