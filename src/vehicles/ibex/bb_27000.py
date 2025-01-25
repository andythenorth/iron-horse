from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bb_27000",
        base_numeric_id=17270,
        name="BB 27000",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={"DC": 5600, "AC": 5600},
        random_reverse=True,
        gen=5,
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
    consist.foamer_facts = """SNCF BB 27000 !! multisystem"""

    return consist
