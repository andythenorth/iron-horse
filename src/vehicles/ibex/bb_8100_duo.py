from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="bb_8100_duo",
        base_numeric_id=190,
        name="BB 8100 / 9200 (duo)",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={"DC": 8700},
        speed=75,  # for lolz
        random_reverse=True,
        gen=3,  # spans gen 4 as well
        pantograph_type="diamond-double",
        intro_year_offset=8,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """SNCF BB 8100 / 9200 (duo)"""

    return consist_factory
