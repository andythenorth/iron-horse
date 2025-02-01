from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="avenger",
        base_numeric_id=21530,
        name="Avenger",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 6200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=-2,  # introduce slightly earlier than gen epoch by design
        lgv_capable=True,  # for lolz
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "WHITE_STRIPE",
            "SWOOSH",
            "SWOOSH_2000",
            "SWOOSH_2000",
            "RAILFREIGHT_TRIPLE_GREY",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=100, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """Daft as a brush if you ask me.  Or mad as a badger.  Goes like stink off a shovel though."""
    consist_factory.foamer_facts = """BR Class 89"""

    return consist_factory
