from train import ConsistFactory

# multi-system !!


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="bls_re_475",
        base_numeric_id=30790,
        name="BLS Re 475 !! Multi-system",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 7400,
            "DC": 7400,
        },
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        intro_year_offset=12,  # introduce later than gen epoch by design
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
    consist_factory.foamer_facts = """BLS Re 475 (Vectron)"""

    return consist_factory
