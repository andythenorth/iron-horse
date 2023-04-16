from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cc_7100",
        base_numeric_id=16200,
        name="CC 7100",
        role="ultra_heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={"DC": 5300},
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
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
    consist.foamer_facts = """SNCF CC 7100"""

    return consist
