from train import EngineConsist


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="obb_1044",
        base_numeric_id=35160,
        name="OBB 1044",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=4,
        power_by_power_source={
            "AC": 7500,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="diamond-double",
        intro_year_offset=9,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """OBB 1044"""

    return consist
