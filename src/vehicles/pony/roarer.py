from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="roarer",
        base_numeric_id=16870,
        name="Roarer",
        subrole="super_heavy_express",
        subrole_child_branch_num=-4,
        power_by_power_source={
            "AC": 3000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=2,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=80, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description(
        """They're right loud these are, but we've got the power right up on em too."""
    )
    consist_factory.add_foamer_facts("""BR 'AL' Classes 81-85""")

    result.append(consist_factory)

    return result
