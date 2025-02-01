from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="drg_e_16",
        base_numeric_id=30920,
        name="DRG E 16",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 3600,
        },
        random_reverse=True,
        gen=2,
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

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """DRG E 16"""

    return consist_factory
