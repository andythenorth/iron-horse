from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="screamer",
        base_numeric_id=21090,
        name="Screamer",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 5000,
        },
        random_reverse=False,
        gen=5,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        # railfreight grey, intercity, GNER?
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "BANGER_BLUE",
            "FREIGHTLINER_GBRF",
            "RES",
            "SWOOSH",
            "DB_SCHENKER",
            "FREIGHTLINER_GBRF",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_BLUE"),
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_DARK_BLUE"),
            ("COLOUR_WHITE", "COLOUR_RED"),
        ],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="ElectricEngineUnit", weight=85, vehicle_length=8, spriterow_num=0
    )

    consist_factory.define_description(
        """We're knocking these out cheap enough. Look after them, they might last longer."""
    )
    consist_factory.define_foamer_facts("""BR Class 90""")

    result.append(consist_factory)

    return result
