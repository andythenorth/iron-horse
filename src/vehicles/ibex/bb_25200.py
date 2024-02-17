from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bb_25200",
        base_numeric_id=14830,
        name="BB 25200",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={"DC": 4600, "AC": 4600},
        random_reverse=True,
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SNCF BB 25200 !! multisystem"""

    return consist
