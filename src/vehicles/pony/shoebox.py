from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="shoebox",
        base_numeric_id=21020,
        name="Shoebox",
        subrole="heavy_express",
        subrole_child_branch_num=-3,
        power_by_power_source={"DIESEL": 950, "AC": 2500},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_year_offset=3,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "BANGER_BLUE",
            "INTERCITY_RASPBERRY_RIPPLE",
            "RES",
            "RAILFREIGHT_TRIPLE_GREY",
            "SWOOSH",
            "DB_SCHENKER",
        ],  # "RAILFREIGHT_TRIPLE_GREY"
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectroDieselEngineUnit",
        weight=80,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist_factory.add_description(
        """This one can go on electric or diesel. Madder than a box of frogs."""
    )
    consist_factory.add_foamer_facts("""BR Class 73, Class 71/74, proposed Class 75""")

    result.append(consist_factory)

    return result
