from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="fs_e646",
        base_numeric_id=160,
        name="FS E.646",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={"DC": 4800},
        random_reverse=True,
        gen=4,
        # pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    # !!! these are only 60 foot long IRL so 2x 4/8 units
    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=0
    )
    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=4, spriterow_num=1
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """FS E.646"""

    return consist_factory
