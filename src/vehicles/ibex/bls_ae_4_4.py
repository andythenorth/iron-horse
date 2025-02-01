from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="bls_ae_4_4",
        base_numeric_id=30930,
        name="BLS Ae 4/4",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 5300,  # unrealistically high, to fit to BLS Re 4/4 progression, which leans towards Swiss
        },
        random_reverse=True,
        gen=3,
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

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """BLS Ae 4/4"""

    return consist_factory
