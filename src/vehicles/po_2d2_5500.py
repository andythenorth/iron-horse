from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="po_2d2_5500",
        base_numeric_id=14820,
        name="PO 2D2 5500",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={"DC": 3700},
        speed=75,
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=-8,  # introduce much later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=105,
        vehicle_length=8,
        spriterow_num=0,
    )

    consist.description = """ """
    consist.foamer_facts = """PO 2D2 5500"""

    return consist
